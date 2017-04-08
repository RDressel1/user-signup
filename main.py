#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import re

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        Signup
    </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
	def get(self):
			forms = """
			<form action="/verify" method="post">
				<label>
					Username:
					<input type="text" name="username"/>
				</label>
				<br>

				<label>
					Password:
					<input type="password" name="password"/>
                    <span class = "error"></span>
				</label>
				<br>

				<label>
					Verify Password:
					<input type="password" name="password_verify"/>
				</label>
				<br>

				<label>
					Email (optional):
					<input type="text" name="email_address"/>
				</label>
				<br>

				<input type="submit" value="Submit"/>
			</form>
			"""

			content = page_header + forms + page_footer
			self.response.write(content)

class Verification(webapp2.RequestHandler):
    def post(self):
    	username = self.request.get("username")
    	password = self.request.get("password")
    	ver_password = self.request.get("password_verify")
    	email = self.request.get("email_address")


        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    	def valid_username(username):
    		return username and USER_RE.match(username)

    	PASS_RE = re.compile(r"^.{3,20}$")
    	def valid_password(password):
    		return password and PASS_RE.match(password)

    	EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
    	def valid_email(email):
    		return not email or EMAIL_RE.match(email)

    	if not valid_username(username):
    		error = "Invalid username!"
    		self.redirect("/?error=" + error)

        if not valid_password(password):
            error = "Invalid password!"
            self.redirect("/?error=" + error)

        if password != ver_password:
            error = "Passwords did not match"
            self.redirect("/?error=" + error)

        if not valid_email(email):
            error = "Invalid email!"
            self.redirect("/?error=" + error)

    	self.response.write("Welcome " + username + "!")




app = webapp2.WSGIApplication([
    ('/', Index),
	('/verify', Verification)
], debug=True)
