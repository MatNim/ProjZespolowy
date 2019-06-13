from flask_wtf import FlaskForm
#from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms import *
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, ValidationError,Optional,NumberRange
from ProjZespolowy.models import Osoba,Firma,Pracownicy_firmy
from ProjZespolowy import db
from flask_login import current_user, logout_user, login_user, login_required

class RegistrationForm(FlaskForm):
    newcompany = StringField('Nowa Firma (Podaj nazwe firmy)')
    company = SelectField('Istniejaca Firma',coerce=int, choices=[],validators=[])
    name = StringField('Imię',
                           validators=[DataRequired(), Length(min=2, max=20, message='Pole powinno zawierać od 2 do 20 znaków') ])
    last_name = StringField('Nazwisko',
                           validators=[DataRequired(), Length(min=2, max=20, message='Pole powinno zawierać od 2 do 20 znaków')])
    username = StringField('Login',
                           validators=[DataRequired(), Length(min=3, max=20, message='Login powinien zawierać od 3 do 20 znaków')])
    email = StringField('Email',
                        validators=[DataRequired(), Email(message='Nieprawidłowy adres Email')])
    password = PasswordField('Hasło', validators=[InputRequired(),Length(min=7, message='Hasło powinno zawierać co najmniej 7 znaków')])
    confirm_password = PasswordField('Powtórz hasło ',
                                     validators=[DataRequired(), EqualTo('password',message='Hasła nie są identyczne')])
    submit = SubmitField('Zarejestruj')

    def validate_username(self, username):
        user = db.Osoba.get(login=username.data)
        if user:
            raise ValidationError('Ten login jest zajety')




class ModifyEmployeeForm(FlaskForm):
    name = StringField('Imię',
                           validators=[DataRequired(), Length(min=2, max=20, message='Pole powinno zawierać od 2 do 20 znaków') ])
    last_name = StringField('Nazwisko',
                           validators=[DataRequired(), Length(min=2, max=20, message='Pole powinno zawierać od 2 do 20 znaków')])
    username = StringField('Login',
                           validators=[DataRequired(), Length(min=3, max=20, message='Login powinien zawierać od 3 do 20 znaków')])
    email = StringField('Email',
                        validators=[DataRequired(), Email(message='Nieprawidłowy adres Email')])
    phonenumber=StringField('Telefon',
                           validators=[ Optional(),Length(min=9, max=10, message='Nieprawidlowy numer telefonu')])
    submit = SubmitField('Zmodyfikuj')

    def validate_username(self, username):
        if current_user.login!=username.data:
            user = db.Osoba.get(login=username.data)
            if user:
                raise ValidationError('Ten login jest zajety')


    '''
    def validate_name(self, name):                  #Custom validator wyswietlajacy pole wymagane jesli puste imie
        if name.data=='':
            raise ValidationError('Pole wymagane')
    '''
class ModifyCompanyForm(FlaskForm):
    name = StringField('Nazwa',
                           validators=[DataRequired(), Length(min=2, max=20, message='Pole powinno zawierać od 2 do 20 znaków') ])
    description = TextAreaField('Opis', render_kw={"rows": 10, "cols": 5})

    email = StringField('Email',
                        validators=[Optional(), Email(message='Nieprawidłowy adres Email')])
    city=StringField('Miejscowosc',validators=[ Optional()])
    street=StringField('Ulica',validators=[ Optional()])
    building=StringField('Adres budynku',validators=[ Optional()])
    flat=StringField('Adres mieszkania',validators=[ Optional()])
    submit = SubmitField('Zmodyfikuj')

    def validate_email(self, email):
        user = db.Osoba.get(email=email.data)
        if user:
            raise ValidationError('Ten email jest zajety')


class RegistrationFormPWR(FlaskForm):
    name = StringField('Imię',
                           validators=[DataRequired(), Length(min=2, max=20, message='Pole powinno zawierać od 2 do 20 znaków') ])
    last_name = StringField('Nazwisko',
                           validators=[DataRequired(), Length(min=2, max=20, message='Pole powinno zawierać od 2 do 20 znaków')])
    username = StringField('Login',
                           validators=[DataRequired(), Length(min=3, max=20, message='Login powinien zawierać od 3 do 20 znaków')])
    email = StringField('Email',
                        validators=[DataRequired(), Email(message='Nieprawidłowy adres Email')])
    password = PasswordField('Hasło', validators=[InputRequired(),Length(min=7, message='Hasło powinno zawierać co najmniej 7 znaków')])
    confirm_password = PasswordField('Powtórz hasło ',
                                     validators=[DataRequired(), EqualTo('password',message='Hasła nie są identyczne')])
    submit = SubmitField('Zarejestruj')

    def validate_username(self, username):
        user = db.Osoba.get(login=username.data)
        if user:
            raise ValidationError('Ten login jest zajety')

    def validate_email(self, email):
        user = db.Osoba.get(email=email.data)
        if user:
            raise ValidationError('Ten email jest zajety')

class RegistrationFormStudent(FlaskForm):
    name = StringField('Imię',
                           validators=[DataRequired(), Length(min=2, max=20, message='Pole powinno zawierać od 2 do 20 znaków') ])
    last_name = StringField('Nazwisko',
                           validators=[DataRequired(), Length(min=2, max=20, message='Pole powinno zawierać od 2 do 20 znaków')])
    username = StringField('Login',
                           validators=[DataRequired(), Length(min=3, max=20, message='Login powinien zawierać od 3 do 20 znaków')])

    indeks = IntegerField('Numer indeksu',validators=[Optional()])

    email = StringField('Email',
                        validators=[DataRequired(), Email(message='Nieprawidłowy adres Email')])
    password = PasswordField('Hasło', validators=[InputRequired(),Length(min=7, message='Hasło powinno zawierać co najmniej 7 znaków')])
    confirm_password = PasswordField('Powtórz hasło ',
                                     validators=[DataRequired(), EqualTo('password',message='Hasła nie są identyczne')])
    submit = SubmitField('Zarejestruj')

    def validate_username(self, username):
        user = db.Osoba.get(login=username.data)
        if user:
            raise ValidationError('Ten login jest zajety')

    def validate_indeks(self, indeks):
        user = db.Osoba.get(numer_indeksu=indeks.data)
        if user:
            raise ValidationError('Ten numer indeksu jest zajety')
    def validate_email(self, email):
        user = db.Osoba.get(email=email.data)
        if user:
            raise ValidationError('Ten email jest zajety')



class ProjectForm(FlaskForm):

    title = StringField('Tytul', validators=[DataRequired()])
    description = TextAreaField('Opis projektu', render_kw={"rows": 10, "cols": 5})
    comment = TextAreaField('Dodatkowe uwagi (np. wymóg przekazania majątkowych praw autorskich, podpisania NDA,wskazanie pracownika uczelni do wspólnej realizacji tematu, itp.)')
    time_nedded = StringField('Naklad czasu (w osobogodzinach, typowa grupa projektowa to 4-5 osób, około 80-100h pracy na osobę)',validators=[DataRequired()] )
    max_students = IntegerField('Maksymalna liczba studentow w grupie',validators=[DataRequired(),NumberRange(min=1, max=10,message='Pole musi zawierac liczbe od 1 do 10')])
    min_students = IntegerField('Minimalna liczba studentow w grupie',validators=[DataRequired(),NumberRange(min=1, max=10,message='Pole musi zawierac liczbe od 1 do 10')])
    max_groups = IntegerField('Maksymalna ilosc grup',validators=[DataRequired(),NumberRange(min=1, max=10,message='Pole musi zawierac liczbe od 1 do 10') ])
    semester = StringField('Semestr', validators=[Optional()])
    submit = SubmitField('Udostepnij projekt')
    save = SubmitField('Zapisz wersje robocza')

class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    remember = BooleanField('Zapamiętaj mnie')
    submit = SubmitField('Login')

class VerifyForm(FlaskForm):
    verify=BooleanField()

class ModifyGroupForm(FlaskForm):
    email = StringField('Podaj email studencki osoby do dodania', validators=[DataRequired(), Email(message='Nieprawidłowy adres Email')])
    submit = SubmitField('Dodaj osobe')
    delete = SubmitField('Usun osobe')

class RequestResetForm(FlaskForm):
    login = StringField('Podaj adres email:',validators=[DataRequired(), Email()])
    submit = SubmitField('Zresetuj hasło')

    def validate_email(self, email):
        user = db.Osoba.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Nie ma takiego adresu email. Najpierw musisz się zarejestrować!')
