from twilio.rest import Client
import random
from .models import User
import threading

account_sid = "AC6de8118f35ee3b8a65c941caabcd1061"
auth_token = "158dab50bcc69e41ce7b548cff880769"
client = Client(account_sid, auth_token)

class SMS():
	def emergency_message(message):
		msg= client.messages.create(
			"+14074219805",
			body=message,
			from_="+13213254478",
		)

		print(msg.sid)

	def encouragement_message(message, user):
		msg= client.messages.create(
			"+1" + user.phone,
			body=message,
			from_="+13213254478",
		)

		print(msg.sid)

	def random_message():
		string = random.choice(["I believe in you. You can and will get through this!","You won't feel this way forever. I promise.",
			"Remember to take a break!","You are stronger than anything you are afraid of!"])
		return string

#	def interval_message(user):
#		threading.Timer(10.0, interval_message()).start()
#		encouragement_message(SMS.random_message(), user)


