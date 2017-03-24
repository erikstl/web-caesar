import webapp2
import caesar

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Web Caesar</title>
</head>
<body>
    <h1> Web Caesar</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""


class Index(webapp2.RequestHandler):

    def get(self):
        message = "Hello World!"
        encrypted_message = caesar.encrypt(message, 13)

        self.response.write(page_header + encrypted_message + page_footer)


app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
