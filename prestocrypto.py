import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import argparse
import sys
import base64

parser = argparse.ArgumentParser(description='Simple encryption/decryption tool.')
group = parser.add_mutually_exclusive_group(required=False)
group.add_argument('--send', action="store_true")
group.add_argument('--receive', action="store_true")

args = parser.parse_args()

if not (args.receive or args.send):
	print
	sr = raw_input("Are you sending a message or receiving a message? Type S or R: ")
	if 's' in sr.lower() and not 'r' in sr.lower():
		args.send = True
		print
		print "You're sending a message. Ok."
		print
	elif 'r' in sr.lower() and not 's' in sr.lower():
		args.receive = True
		print
		print "You're receiving a message. Ok."
		print
	else:
		print
		print "I didn't understand that input. Next time type S or R, or use the command line arguments."
		print
		sys.exit(2)

if args.receive == True:
	print "Generating a new ID for you to send to the person who is sending you a message..."

	random_generator = Random.new().read
	key = RSA.generate(2048, random_generator)

	publicKey = key.publickey()
	publicKeyNum = publicKey.exportKey('DER')
	publicKeyText = publicKeyNum.encode("hex")

	print
	print "Done! Ok, send this ID to the person who wants to send you a secret message: "
	print 
	print publicKeyText
	print

	encryptedText = raw_input("When they send you the encrypted message, paste it here: ")
	encryptedNum = encryptedText.decode("hex")
	messageText = key.decrypt(encryptedNum)

	print
	print "Here's the secret message: "
	print messageText
	print

	raw_input("Press enter to continue...")

elif args.send == True:
	publicKeyText = raw_input("Copy & paste the receiver's ID: ")

	publicKeyNum = publicKeyText.decode("hex")

	try:	
		publicKey = RSA.importKey(publicKeyNum)
	except:
		print "Didn't understand that ID! Ask the sender for his/her ID. Rerun this program to try again"
		sys.exit(2)

	print
	messageText = raw_input("That ID looks good! Now enter the secret message you would like to send: ")

	if len(messageText) > 128:
		print "Sorry! Only messages 128 characters or less are accepted at this time"
		sys.exit(2)

	encryptedNum = publicKey.encrypt(messageText, "Whales Do Not Exist")[0]
	encryptedText = encryptedNum.encode("hex")

	print
	print "Here is the encrypted message: "
	print
	print encryptedText
	print
	
	raw_input("Press enter to continue...")

