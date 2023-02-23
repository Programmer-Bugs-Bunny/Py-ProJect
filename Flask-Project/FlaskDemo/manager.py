from flask import Flask, render_template
from flask_ckeditor import CKEditor, CKEditorField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

ckeditor = CKEditor(app)

app.config['CKEDITOR_PKG_TYPE'] = 'full-all'
app.config["SECRET_KEY"] = "123456"


class TestForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField('Publish')


@app.route('/')
def hello_world():  # put application's code here
    form = TestForm()
    return render_template('test-rich-text.html', form=form)


if __name__ == '__main__':
    app.run()
