from twilio.rest import Client

# importing necessary functions from dotenv library
# loading variables from .env file
# accessing and printing value
# print(os.getenv("MY_KEY"))
import os
# from dotenv import load_dotenv, dotenv_values
load_dotenv()


def sms_noinput(number, message):
	account_sid = os.getenv("TWILIO_ACCOUNT_SID")
	auth_token = os.getenv("TWILIO_AUTH_TOKEN")

	client = Client(account_sid, auth_token)

	message = client.messages.create(
		body=message,
		from_=os.getenv("TWILIO_PHONE_NUMBER"),
		to=number
	)

	print(f"Message sent with SID: {message.sid}")


def sms_input():
	number = input("Enter number with the country code: ")
	message = input("Enter the message you want to send: ")
	sms_noinput(number, message)
