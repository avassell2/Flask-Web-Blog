from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User










class RegistrationForm(FlaskForm): #inherits from FlaskForm
    username = StringField('Username',
    validators=[DataRequired(), Length(min =2, max=20)])

    email = StringField('Email',
    validators=[DataRequired(), Email()])

    password = PasswordField('PasswordField',
    validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',
    validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username): #check if username is unique upon registration
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already in use. Please choose a different one.')

    def validate_email(self, email): #check if email is unique upon registration
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already in use. Please choose a different one.')







class LoginForm(FlaskForm): #inherits from FlaskForm
        #username = StringField('Username',
        #validators=[DataRequired(), Length(min =2, max=20)])

        email = StringField('Email',
        validators=[DataRequired(), Email()])

        password = PasswordField('PasswordField',
        validators=[DataRequired()])

        #confirm_password = PasswordField('Confirm Password',
        #validators=[DataRequired(), EqualTo('password')])

        remember = BooleanField('Remember Me') #Remember is a user logged in

        submit = SubmitField('Login')



class UpdateAccountForm(FlaskForm): #inherits from FlaskForm
    username = StringField('Username',
    validators=[DataRequired(), Length(min =2, max=20)])

    email = StringField('Email',
    validators=[DataRequired(), Email()])


    picture = FileField('Change Profile Picture', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])]) #allowed file extensions for input file

    submit = SubmitField('Update')

    def validate_username(self, username): #check if username is unique upon update
        if username.data != current_user.username: #only does validation check if data entered is different from current data
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already in use. Please choose a different one.')

    def validate_email(self, email): #check if email is unique upon update
        if email.data != current_user.email: #only does validation check if data entered is different from current data
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use. Please choose a different one.')



class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first() #checks if username exists
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
