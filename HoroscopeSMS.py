# Import all the libraries we will be using.
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from bs4 import BeautifulSoup
import requests
import re

# Set up Flask to connect this code to the local host, which will later be connected to the internet through Ngrok.
app = Flask(__name__)

# Main method. When a POST request is sent to our local host through Ngrok (which creates a tunnel to the web), this code will run.
# The Twilio service number sends the POST request - we will set this up on the Twilio website. So when message is sent over SMS to our Twilio number, this code will run.
@app.route('/', methods=['POST'])
def sms():
    # Function to get the text in the message sent.
    message_body = request.form['Body']

    # Create a Twilio response object to be able to send a reply back.
    resp = MessagingResponse()

    # Send the message body to the getReply message, where we will query the string and formulate a response.
    replyText = getReply(message_body)

    # Text back our response!
    resp.message('Hello, below is your daily horoscope for the day.\n\n' + replyText )
    return str(resp)

def getReply(message):
	# Function to formulate a response based on message input.
    # This is the variable where we will store our response. 
    message = message.lower().strip() # Make the message lower case and without spaces on the end for easier handling.
    horoscope = {'aries': 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=1', 'gemini': 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=3', 'taurus': 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=2', 'cancer': 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=4', 'leo': 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=5', 'virgo': 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=6', 'libra': 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=7', 'scorpio': 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=8', 'sagittarius': 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=9', 'capricorn':'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=10', 'aquarius':'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=11', 'pisces':'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=12' }

    # Extracts the daily horoscope paragraph from horoscope.com.
    if message in message: # Is there a valid horoscope in the message? Ex: "aries".
        try:
            html = requests.get(horoscope.get(message)).content # Will replace the horoscope dictionary item with the horoscope dictionary value (website).
            unicode_str = html.decode("utf8")
            encoded_str = unicode_str.encode("ascii",'ignore')
            news_soup = BeautifulSoup(encoded_str, "html.parser")
            message = ""
            a_text = news_soup.find_all('p', limit=1) # Extracts only the first paragraph of the daily horoscope webpage for selected horoscope sign.
            remove = [re.sub(r'<.+?>',r'',str(a)) for a in a_text] # Removes unneeded text from webpage
            for x in remove: 
                message += x # Converts the list into a string.
            return message # Returns the new string.
        except: # Handle errors or non specificity errors.
            answer = "Please spell check and re-send your horoscope sign. For example try 'Aries'. "

    # The message contains no keyword. Display a help prompt to identify possible.
    else:
        answer = "Please spell check and re-send your horoscope sign. For example try 'Aries'. "

    # Twilio can not send messages over 1600 characters in one message.
    # Horoscope daily summaries may have way more than this.
    if len(answer) > 1500:
        answer = message[0:1500] + "..."

    # Return the formulated answer.
    return answer

# When you run the code through terminal, this will allow Flask to work.
if __name__ == '__main__':
    app.run()

#Final step: run ngrok.exe and enter "ngrok http localhost:5000"