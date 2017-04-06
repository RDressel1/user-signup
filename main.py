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
			username = """
			<form>
				<label>
					Username:
					<input type="text" name="username"/>
				</label>
			</form>
			"""
			
			password = """
			<form>
				<label>
					Password:
					<input type="text" name="password"/>
				</label>
			</form>
			"""
			
			verifypassword = """
			<form>
				<label>
					Verify Password:
					<input type="text" name="password_verify"/>
				</label>
			</form>
			"""
			
			email = """
			<form>
				<label>
					Email (optional):
					<input type="text" name="email_address"/>
				</label>
			</form>
			"""
			forms = username + password + verifypassword + email
			content = page_header + forms + page_footer
			self.response.write(content)
	
	


app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
