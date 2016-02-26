import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import argparse
import sys
import base64

parser = argparse.ArgumentParser(description='Simple encryption/decryption tool.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--send', action="store_true")
group.add_argument('--receive', action="store_true")

args = parser.parse_args()

if args.send == True:
	print "Generating a new ID for you to send to the person you are receiving a message from..."

	random_generator = Random.new().read
	key = RSA.generate(4096, random_generator)

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

elif args.receive == True:
	publicKeyText = raw_input("Copy & paste the sender's ID: ")

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
	
