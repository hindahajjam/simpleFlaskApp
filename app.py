from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def index():
    name = "hind"
    date = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
    return render_template("index.html", name=name, date=date)


if __name__ == '__main__':
    app.run(debug=True)
