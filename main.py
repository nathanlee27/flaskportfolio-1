from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL to a function
@app.route('/')
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html")
    
@app.route('/templates/socials.html')
def socials():
    return render_template("socials.html")

@app.route('/templates/hello.html')
def hello():
    return render_template("hello.html")

@app.route('/templates/flask.html')
def flask():
    return render_template("flask.html")

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='3000', host='0.0.0.0')