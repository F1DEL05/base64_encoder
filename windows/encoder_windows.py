import base64
import os
import time

def encode_base64(text):
    message_bytes = text.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode('ascii')

def decode_base64(base64_text):
    base64_bytes = base64_text.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('ascii')

# Base64'e çevirmek için
while True:
	os.system("cls")
	print("\nBASE64 Message Application")
	print("\n1.Encryption \n2.Decryption\n3.Close\n\n")
	a=input("---> ")
	if a=="1":
		text = input("\nYour Message : ")
		base64_text = encode_base64(text)
		print(f"\nEncrypted Message : {base64_text}")
		b=input("\n\nYou can press ENTER for continue ...")
		os.system("cls")
		continue
	elif a=="2":
		text_decode=input("\nEncrypted Message: ")
		decoded_text = decode_base64(text_decode)
		print(f"\nYour Message: {decoded_text}")
		b=input("\n\nYou can press ENTER for continue ...")
		os.system("cls")
		continue
	elif a=="3":
		os.system("cls")
		print("Program is closing...")
		time.sleep(0.5)
		break
	else:
		print("\n\ninvalid number !")
exit()
