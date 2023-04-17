from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, DateField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp

class RegisterForm(FlaskForm):
  role = SelectField('Você é Aluno ou Professor?', choices=[('aluno', 'Aluno'), ('professor', 'Professor')])
  email = StringField('Email', render_kw={"placeholder": "nome@gmail.com"}, validators=[DataRequired(), Regexp('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', message='Email inválido')])
  matricula = StringField('Matricula', render_kw={"placeholder": "Sua Matricula"}, validators=[DataRequired(), Length(min=9, max=9, message='Matricula deve ter 9 digitos')])
  firstName = StringField('Nome', render_kw={"placeholder": "Seu Nome"}, validators=[DataRequired(), Length(min=2, max=20, message='Nome deve ter entre 2 e 20 caracteres')])
  lastName = StringField('Sobrenome', render_kw={"placeholder": "Seu Sobrenome"}, validators=[DataRequired(), Length(min=2, max=20, message='Sobrenome deve ter entre 2 e 20 caracteres')])
  password1 = PasswordField('Senha', render_kw={"placeholder": "Sua Senha"}, validators=[DataRequired(), Length(min=8, max=20, message='Senha deve ter entre 8 e 20 caracteres')])
  password2 = PasswordField('Confirme a Senha:', render_kw={"placeholder": "Confirme sua Senha"}, validators=[DataRequired(), EqualTo('password1', message='Senhas não conferem')])
  submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
  # role = SelectField('Você é Aluno ou Professor?', choices=[('aluno', 'Aluno'), ('professor', 'Professor')])
  matricula = StringField('Matricula', render_kw={"placeholder": "Sua Matricula"}, validators=[DataRequired(), Length(min=9, max=9, message='Matricula deve ter 9 digitos')])
  password = PasswordField('Senha', render_kw={"placeholder": "Sua Senha"}, validators=[DataRequired(), Length(min=8, max=20, message='Senha deve ter entre 8 e 20 caracteres')])
  submit = SubmitField('Login')

class LessonForm(FlaskForm):
  name = StringField('Nome da Aula', render_kw={"placeholder": "Nome da Aula"}, validators=[DataRequired(), Length(min=2, max=20, message='Nome da aula deve ter entre 2 e 20 caracteres')])
  date = DateField('Data da Aula', render_kw={"placeholder": "Data da Aula"}, validators=[DataRequired()])
  submit = SubmitField('Criar Aula')

class AttendanceForm(FlaskForm):
  present = BooleanField('Presença', default='unchecked')