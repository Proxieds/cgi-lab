import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import secret
import os
from http.cookies import SimpleCookie

# CREATE SIMPLE LOGIN FORM

# Set up cgi form
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

# Check if correct login info is provided to cgi form
form_ok = username == secret.username and password == secret.password

# Setup cookie
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value

# Chek if cookie username and password equals secret username and password
cookie_ok = cookie_username == secret.username and cookie_password == secret.password

# Then set username and password to cookie's username and password
if cookie_ok:
    username = cookie_username
    password = cookie_password

if form_ok:
    # Set cookie if login information was correct
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")