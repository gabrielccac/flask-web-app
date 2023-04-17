from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import LoginForm, RegisterForm
from .models import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    matricula = form.matricula.data
    password = form.password.data
    
    user = User.query.filter_by(matricula=matricula).first()
    if user:
      if check_password_hash(user.password, password):
        flash('Logado com sucesso!', category='success')
        login_user(user, remember=True)
        if user.is_teacher == 'professor':
          return redirect(url_for('views.teacher'))
        if user.is_teacher == 'aluno':
          return redirect(url_for('views.student'))
        
      else:
        flash('Senha incorreta, tente novamente', category='error')
    else:
      flash('Matricula não cadastrada.', category='error')

  if form.errors:
    print(form.errors)
  return render_template("login.html", form=form, user=current_user)
  
@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  form = RegisterForm()
  if form.validate_on_submit():
    # Check if user already exists in database
    userMat = User.query.filter_by(matricula=form.matricula.data).first()
    userEmail = User.query.filter_by(email=form.email.data).first()
    if userMat:
      flash('Matricula já cadastrada.', category='error')
      return render_template("sign_up.html", form=form)
    elif userEmail:
      flash('Email já cadastrado', category='error')
      return render_template("sign_up.html", form=form)
    else:
      new_user = User(email=form.email.data, first_name=form.firstName.data, last_name=form.lastName.data, matricula=form.matricula.data, password=generate_password_hash(form.password1.data, method='sha256'), is_teacher=form.role.data)
      db.session.add(new_user)
      db.session.commit()
      flash('Conta criada com sucesso!', category='success')
      return redirect(url_for('auth.login'))
  if form.errors:
        for error in form.errors.values():
            flash(error[0], category='error')
        return render_template("sign_up.html", form=form)
    
  return render_template("sign_up.html", form=form, user=current_user)
    
  