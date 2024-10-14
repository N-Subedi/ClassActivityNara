from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <html>
    <body>
        <h1>Hello, Narayan</h1>
        <p>The greatest player of all time (GOAT) is Lionel Messi</p>
        <img src="https://media.newyorker.com/photos/63a0b8e018f0244bba9fd613/master/pass/Mochkofsky-Messi.jpg" alt="Lionel Messi" width="500">
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
