from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from .forms import LessonForm, LoginForm, AttendanceForm
from .models import User, Lesson, db
from datetime import datetime, date

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
  form = LoginForm()
  return render_template("login.html", form=form, user=current_user)

@views.route('/teacher', methods=['GET', 'POST'])
@login_required
def teacher():
  form = LessonForm()
  students = User.query.filter_by(is_teacher='aluno').all()
  if form.validate_on_submit():
    # Create a lesson
    lesson = Lesson(name=form.name.data, teacher_id=current_user.id, date=form.date.data)
    db.session.add(lesson)
    db.session.commit()

    flash('Aula criada com sucesso!', category='success')
    return redirect(url_for('views.teacher'))
  return render_template("teacher.html", form=form, user=current_user, lessons=Lesson.query.filter_by(teacher_id=current_user.id), students=students)
  
@views.route('/student', methods=['GET', 'POST'])
@login_required
def student():
  users = User.query.all()
  form = AttendanceForm()
  lessons = Lesson.query.all()
  today = datetime.combine(date.today(), datetime.min.time())
  return render_template("student.html", form=form, user=current_user, lessons=lessons, today=today, users=users)

@views.route('/present/<int:lesson_id>', methods=['GET', 'POST'])
@login_required
def present(lesson_id):
  lesson = Lesson.query.filter_by(id=lesson_id).first()
  current_user.lessons_attended.append(lesson)
  db.session.commit()
  return redirect(url_for('views.student'))