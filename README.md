# Horoscope SMS

This Python Program will create a bot that can receive and send SMS (short message service) to the user containing their daily horoscope for the day depending on their astrological sign.

## Getting Started

These instructions will setup Flask to connect the code to the local host, which will later be connected to the internet through Ngrok. The Twilio service number sends the POST request so when the message is sent over SMS to our Twilio number, this code will run. Then when the Twilio number receives a SMS from the user the code will use the BeautifulSoup module to web scrap the astrological sign's daily horoscope from Horoscope.com and return a SMS back to the user.

## Prerequisites

Horoscope SMS requires Python 3.5.3+ to run, with the following libraries: flask, twilio.twiml.messaging_response, bs4, requests, and re.

The following software is required:
1. [Python 3.5.3+](https://www.python.org/downloads/)
2. [PyCharm 2019.1.1+](https://www.jetbrains.com/pycharm/download/#section=windows) or any IDE of your choice.
3. [Ngrok](https://ngrok.com/)
4. [Phone number from Twilio](https://www.twilio.com/)


## Running

1. Run HoroscopeSMS.py
2. Run ngrok.exe and enter "Run ngrok http localhost:5000"
3. Copy one of the forwarding addresses then enter it in your Twilio's Active Numbers -> Messaging 
4. Text horoscope sign to your Twilio phone number.

## Thanks
Thank you for the following resources for help:
1. [Liz Petrov](https://makezine.com/projects/sms-bot/)
2. [Horoscope.com](https://www.horoscope.com/)
3. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
