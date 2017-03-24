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
    <h1>Web Caesar</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""


class Index(webapp2.RequestHandler):

    def get(self):
        content = """
            <form action="/encrypt" method="post">
                <label><p>Enter text to encrypt:</p>
                <textarea rows="4" cols="50" name="secret-message"></textarea>
                <p>Rotation factor:</p>
                <input type="text" name="rotation"/>
                <input type="submit" value="Encrypt!"/>
            </form>
        """
        self.response.write(page_header + content + page_footer)

class CaesarEncrypt(webapp2.RequestHandler):
    def post(self):
        #message = "Hello World!"
        message = self.request.get("secret-message")
        rot = self.request.get("rotation")
        encrypted_message = caesar.encrypt(message, rot)
        content = page_header + "<p>Your encrypted message:</p>" + encrypted_message + page_footer

        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/encrypt', CaesarEncrypt)
], debug=True)
