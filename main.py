from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def render_home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
