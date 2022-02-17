# since the forms are already designed using html the models here would only be used for validation
# but the model might not be important since the validations here are just INPUTREQUIRED()


# from flask_wtf import FlaskForm
# from wtforms import PasswordField
# from wtforms import validators
# from wtforms.fields.core import StringField
# from wtforms.validators import InputRequired, Length

# #creating a schema for the Login form
# class LoginForm(FlaskForm):
#     email = StringField('email',validators=[InputRequired()])
#     password = PasswordField('password',validators=[InputRequired()])
    
# #creating a schema for the signup page
# class SignUpForm(FlaskForm):
#     fullname = StringField('fullname',validators=[InputRequired()])
#     spassword = PasswordField('password', validators=[InputRequired()])
    
# class Comment(FlaskForm):
#     email = StringField('email',validators=[InputRequired()])
#     body = StringField('body', validators=[InputRequired(),Length(min=30,max=400)])
    