from flask import Flask, request, render_template
from caesar import rotate_string

app = Flask(__name__, static_url_path='/static')

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

page_header = """
    <html lang="en">
<head>
    <link rel="stylesheet" href="static/stylesheet.css">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Web Caesar</title>
</head>
<body>
        <div class="wrapper">
                <h1>WEB CAESAR</h1>
"""

page_footer = """
    </body>
</html>
"""

#a form for code input
input_form = """
    <form action="/output" class="form1" method="post">
        <p>1. Enter the text you want to encipher.</p>
        <textarea id='orig' type="text" name="text" class="original_text" placeholder="ORIGINAL TEXT"></textarea>
        <p>2. Enter the number of rotations.</p>
        <div id='rotobj'>
            <input id='rot' type="text" name="rot" class="rot" placeholder="ROTS">
        </div>
        <div class="submit">
            <input type="submit" class="submit" value="CLICK TO ENCIPHER!">
        </div>
    </form>
    </div>

"""

# output form
output_form = """
        <p>Enciphered Text Below:</p>
      <textarea id='enciphered' type="text" class="original_text" placeholder="ENCIPHERED TEXT">{}</textarea>
  </div>
"""

@app.route("/output",methods=['POST'])

def out_form():
    text = request.form['text']
    rot = int(request.form['rot'])
    enciphered = rotate_string(text,rot)
    content = page_header + output_form.format(enciphered) + page_footer
    return content



# basic index.html first page
@app.route("/")
def index():
    content = page_header + input_form + page_footer
    return content

    # response string

app.run()
