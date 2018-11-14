from flask import Flask,render_template
from data import Students

s=Students()
app=Flask(__name__)

@app.route('/')
def _index():
    return render_template('index.html')
@app.route('/details')
def _display():
    return render_template('details.html',getdet=s)


if(__name__=='__main__'):
    app.run(debug=True)


