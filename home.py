from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def fun1():
    return render_template('index.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')

app.run()

