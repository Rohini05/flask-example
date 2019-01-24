from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    name="abc"
    list=[1,2,3]
    return render_template('url.html', name = name, list = list)

if __name__== '__main__':
    app.run(debug=True)
