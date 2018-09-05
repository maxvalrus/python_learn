from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField

class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[validators.Length(min=4, max=25)])
    email = StringField(label='E-mail', validators=[validators.Length(min=4, max=35), validators.Email()])
    job = StringField(validators=[validators.Required(), validators.AnyOf(("IT", "Bank", "HR"))])
    month = IntegerField(validators=[validators.data_required(), validators.NumberRange(min=1, max=12)])

app = Flask(__name__)
app.config.update(DEBUG=True, SECRET_KEY='This key must be secret!', WTF_CSRF_ENABLED=False)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form = ContactForm(request.form)

        if form.validate():
            if int(request.form['month']) == 5:
                return ('Cool!', 200)
            else:
                return ('Month != 5', 400)
        else:
            return ('invalid', 400)

    if request.method == 'GET':
        return 'hello world!', 200

if __name__ == '__main__':
    app.run()
