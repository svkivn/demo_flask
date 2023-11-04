from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[Length(min=4, max=15,
                                              message='Це поле має бути довжиною між 4 та 15 символів'),
                                       DataRequired(message="Це поле обов'язкове")])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[Length(min=6,
                                                message='Це поле має бути більше 6 cимволів'),
                                         DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    # style = SelectField('Choose the sock style',
    #                     choices=[('', ''), ('ankle', 'Ankle'),
    #                              ('knee-high', 'Knee-high'),
    #                              ('mini', 'Mini'),
    #                              ('other', 'Other')])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
