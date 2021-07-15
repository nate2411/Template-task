from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<table>')
def homepage(table):
    students = {"Nathan": 22, "Ashton": 18, "Demi": 26, "Luyanda": 22, "Kamogelo": 20}
    return render_template('home_page.html', table=students)


@app.route('/loopy/<int:number>')
def loopy(number):
    return render_template('numbers_page.html', number=number)


if __name__ == '__main__':
    app.debug = True
    app.run()
