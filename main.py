import webapp2
import caesar

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Web Caesar</title>
    <link rel="stylesheet" type="text/css" href="/css/styles.css" media="all">
</head>
<body>
    <h1>Web Caesar</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

def build_page(textarea_content, rotation_content):
    message_label = "<label><p>Enter text to encrypt:</p></label>"
    message_input = "<textarea rows='4' cols='50' name='secret-message'>" + textarea_content + "</textarea>"

    rot_label = "<label><p>Rotate by</p></label>"
    rot_input = "<input type='number' name='rotation' value='" + rotation_content + "'/>"

    submit_button = "<input type='submit' value='Encrypt!'>"

    form = ("<form method='post'>" +
            message_label + message_input +
            rot_label + rot_input +
            "<br>" + submit_button +
            "</form>")

    return form

class Index(webapp2.RequestHandler):

    def get(self):
        content = build_page("", "")
        self.response.write(page_header + content + page_footer)

    def post(self):
        message = self.request.get("secret-message")
        rot = self.request.get("rotation")
        encrypted_message = caesar.encrypt(message, rot)

        content = build_page(encrypted_message, rot)

        self.response.write(page_header + content + page_footer)



app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
