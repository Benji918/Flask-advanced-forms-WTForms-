from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import Forms

app = Flask(__name__)
app.secret_key = 'THIS IS MY SECRET KEY'
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Forms(meta={'csrf': True})
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == '12345678':
            return render_template('success.html')
        return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
