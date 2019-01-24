from flask import Flask
app = Flask(__name__)

@app.route('/hi/<int:no>')
def hello_name(no):
    return 'administrator area guest not allowed!"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Guest User %s not having admin rights' %guest
@app.route('/user/<nmae>')
def hello_user(name):
    if name =='admin':
        return redirect(url_for('hello_admin'))
    else:
     return redirect(url_for('hello_guest',guest = name))   
if __name__=="__main__":
    app.run(debug=True)
                                                                                        
