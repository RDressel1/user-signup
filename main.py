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

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
	return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
	return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
	return not email or EMAIL_RE.match(email)

class Index(webapp2.RequestHandler):
    def get(self):
        forms = """
        <form method="post">
        	<label>
        		Username:
        		<input type="text" name="username"/ value="{{username}}">
        	</label>
        	<br>

        	<label>
        		Password:
        		<input type="password" name="password" value=""/>
                <span class = "error"></span>
        	</label>
        	<br>

        	<label>
        		Verify Password:
        		<input type="password" name="password_verify" value=""/>
        	</label>
        	<br>

        	<label>
        		Email (optional):
        		<input type="text" name="email_address"/ value="">
        	</label>
        	<br>

        	<input type="submit" value="Submit"/>
        </form>
        """
        content = page_header + forms + page_footer
        self.response.write(content)

    def post(self):
    	username = self.request.get("username")
        global_user = username
    	password = self.request.get("password")
    	ver_password = self.request.get("password_verify")
    	email = self.request.get("email_address")
        error_ind = False

        params = dict(username = username, email = email)

        if not valid_username(username):
            params['error_username'] = "Invalid username!"
            error_ind = True

        if not valid_password(password):
            params['error_password'] = "Invalid password!"
            error_ind = True

        if password != ver_password:
            params['error_match'] = "Passwords did not match"
            error_ind = True

        if not valid_email(email):
            params['error_email'] = "Invalid email!"
            error_ind = True

        if error_ind == False:
            self.redirect('/welcome?username=' + username)

class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        self.response.write("Welcome " + username + "!")


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/welcome', Welcome)
], debug=True)
