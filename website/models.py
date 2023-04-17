from . import db
from flask_login import UserMixin
from datetime import date
from sqlalchemy.sql import func

attendance = db.Table('attendance',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('lesson_id', db.Integer, db.ForeignKey('lessons.id'), primary_key=True),
    db.Column('is_present', db.Boolean, default=False)
)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    matricula = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    is_teacher = db.Column(db.String(10), default='Aluno')
    lessons_attended = db.relationship('Lesson', secondary=attendance, back_populates='students_attending')

class Lesson(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=date.today)
    students_attending = db.relationship('User', secondary=attendance, back_populates='lessons_attended')
