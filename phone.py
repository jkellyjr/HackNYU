from twilio.rest import Client
import random
from .models import User
import threading

account_sid = "spooky"
auth_token = "super-secret"
client = Client(account_sid, auth_token)

class SMS():
	def emergency_message(message):
		msg= client.messages.create(
			"sender",
			body=message,
			from_="from_phone",
		)

		print(msg.sid)

	def encouragement_message(message, user):
		msg= client.messages.create(
			"+1" + user.phone,
			body=message,
			from_="",
		)

		print(msg.sid)

	def random_message():
		string = random.choice(["I believe in you. You can and will get through this!","You won't feel this way forever. I promise.",
			"Remember to take a break!","You are stronger than anything you are afraid of!"])
		return string

#	def interval_message(user):
#		threading.Timer(10.0, interval_message()).start()
#		encouragement_message(SMS.random_message(), user)
