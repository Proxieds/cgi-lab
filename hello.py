#!/usr/bin/env python3
import os
import json


# Serves the data back as JSON
# print("Content-Type: application/json")
# print()
# print(json.dumps(dict(os.environ), indent= 2))

# Prints the query parameter data in HTML
if os.environ['QUERY_STRING']:
    print("Content-Type: text/html\r\n")
    print("<h1>Query String Provided</h1>")
    print()
    print(f"<p>Query_String = {os.environ['QUERY_STRING']}")

else:
# PART 3: Modify script to report the user's browser information
    print("Content-Type: text/html\r\n")
    print("<h1>Showing Browser Information</h1>")
    print()
    print(f"<p>User_Browser = {os.environ['HTTP_USER_AGENT']}")