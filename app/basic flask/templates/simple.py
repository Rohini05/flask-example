from flask import Flask,render_template
app= Flask(__name__)

@app.route('/')
def index():
    return render_template('abcd.html')
if__name__=='__main__':
    app.run(debug=True)