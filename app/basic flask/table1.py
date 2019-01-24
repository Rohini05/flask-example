from flask import Flask,render_template
app=Flask(__name__)

@app.route('/result')
def table():
    mydict ={
    'maths':80,
    'c':70,
    'Java':60,
        }
    print(mydict)
    return render_template('table.html',result=mydict)

if __name__=="__main__":
    app.run(degun=True)
