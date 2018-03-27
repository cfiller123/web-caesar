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
                height:120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="post">
            <label>
                Rotate by:
                <input type="text" value="0" name="rot"/>
                <textarea rows="4" cols="50" name="text">{0}</textarea>
            </label>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>

"""

@app.route("/", methods=['POST'])
def encrypt():
    rotation = int(request.form['rot'])
    text = request.form['text']
    rotated_string = rotate_string(text,rotation)
    encrypted_string = '<h1>' + rotated_string + '</h1>'
    return form.format(encrypted_string)

@app.route("/")
def index():
    return form.format("")

app.run()
