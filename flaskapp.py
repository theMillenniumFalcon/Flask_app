from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)


app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'author': 'Nishank Priydarshi',
        'title': 'Blog Post 1',
        'content': 'First blog content',
        'date_posted': 'April 20, 2021'
    },
    {
        'author': 'Sanskar Modi',
        'title': 'Blog Post 2',
        'content': 'Second blog content',
        'date_posted': 'May 20, 2021'
    },
    {
        'author': 'Shivansh Joshi',
        'title': 'Blog Post 3',
        'content': 'Third blog content',
        'date_posted': 'June 20, 2021'
    }
]  # a list of dictionaries and each dictionary will have a single blog post


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
