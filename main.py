from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            p.error {{
                color: red;
            }}
        </style>
    </head>
    <body>
        <form method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="0">
                <p class="error"></p>
            </div>
            <h1><textarea type="text" name="text">{0}</textarea></h1>
            <br>
            <input type="submit">
        </form>
    </body>
</html>
"""


@app.route("/")
def index():
    return form.format("")

@app.route("/",methods=["POST"])
def encrypt():
    text = request.form['text']
    rot = int(request.form['rot'])
    return "<h1>" + form.format(rotate_string(text,rot)) + "</h1>"

app.run()