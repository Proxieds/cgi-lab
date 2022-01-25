#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import secret
import os
from http.cookies import SimpleCookie

# LOGIN FORM

# Set up cgi form
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

# Check if the correct login information is provided to the cgi form
form_ok = username == secret.username and password == secret.password

# Initialize simple cookie using environment cookie variable
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = cookie.get("username").value if cookie.get("username") else None
cookie_password = cookie.get("password").value if cookie.get("password") else None

# Check if the cookie username and password equals the secret username and password
cookie_ok = cookie_username == secret.username and cookie_password == secret.password

# Sets form username and password to the cookie's username and password if it is valid
if cookie_ok:
    username = cookie_username
    password = cookie_password

if form_ok:
    # Saves cookie if a valid login was performed
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")

# Set to print as html
print("Content-Type: text/html\r\n")
print()
print("<h1>Simple Login Form</h1>")

# Load Simple Login Pages
if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())