from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Do something with the text input here
        text_input = request.form['text_input']
        print(text_input)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
