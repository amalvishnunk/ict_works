from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)

@app.route('/')
def fun():
    return render_template('sample.html')
@app.route('/home')
def _home():
    return render_template('sample.html')
    
@app.route('/about')
def _about():
    return render_template('about.html')
@app.route('/contact')
def _contact():
    return render_template('contact.html')
# for reciving data from form
@app.route('/send',methods=['GET','POST'])
def _action():
    if(request.method=='POST'):
        name=request.form['getname']
        mail=request.form['getmail']
        mob=request.form['getmob']
        sub=request.form['getsub']
        msg=request.form['getmsg']
# passing data to frontend
        return render_template('result.html',newname=name,newmail=mail,newmob=mob,newsub=sub,newmsg=msg)
    

if(__name__=='__main__'):
    app.run(debug=True)