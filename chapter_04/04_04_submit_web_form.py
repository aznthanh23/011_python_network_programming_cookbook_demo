#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 4
# This program is optimized for Python 2.7.
# It may run on any other Python version with/without modifications.

import requests
import urllib
import urllib2

ID_USERNAME = 'signup-user-name'
ID_EMAIL = 'signup-user-email'
ID_PASSWORD = 'signup-user-password'
USERNAME = 'username'
EMAIL = 'you@email.com'
PASSWORD = 'yourpassword'
#SIGNUP_URL = 'https://twitter.com/account/create'
SIGNUP_URL = 'https://passport.jd.com/new/login.aspx'

def submit_form():
    """ Submit a form """
    payload = {ID_USERNAME : USERNAME,
            ID_EMAIL : EMAIL,
            ID_PASSWORD : PASSWORD,}

    # make a get request
    resp = requests.get(SIGNUP_URL)
    print "Response to GET request: %s" %resp.content

    # send POST request
    resp = requests.post(SIGNUP_URL, payload)
    print "Headers from a POST request response: %s" %resp.headers
    # print "HTML response: %s" %resp.read()

if __name__ == '__main__':
    submit_form()

