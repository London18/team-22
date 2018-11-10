from flask import Flask, render_template,request
app = Flask(__name__)

generatedStatement = "something"

@app.route('/')
def hello_name():
   return render_template('hello.html', name = generatedStatement)

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['Text']
    processed_text = text.upper()
    return render_template('hello.html',name= text)

if __name__ == '__main__':
   app.run(debug = True)
