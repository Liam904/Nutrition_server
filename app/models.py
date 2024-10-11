from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


class Meal(db.Model):

    __tablename__ = "meals"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    food_items = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Float, default=1, nullable=False)
    meal_type = db.Column(db.String(50), nullable=False)
    date_logged = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text, nullable=True)

    total_calories = db.Column(db.Float, default=0)
    total_protein = db.Column(db.Float, default=0)
    total_fat = db.Column(db.Float, default=0)
    total_carbohydrates = db.Column(db.Float, default=0)
    total_fiber = db.Column(db.Float, nullable=True, default=0)
    total_sugar = db.Column(db.Float, nullable=True, default=0)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class Goal(db.Model):
    __tablename__ = "goals"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    calories_goal = db.Column(db.Float, nullable=True)
    protein_goal = db.Column(db.Float, nullable=True)
    fat_goal = db.Column(db.Float, nullable=True)
    carbohydrates_goal = db.Column(db.Float, nullable=True)
    fiber_goal = db.Column(db.Float, nullable=True)
    sugar_goal = db.Column(db.Float, nullable=True)

    weight_goal = db.Column(db.Float, nullable=True)
    exercise_goal = db.Column(db.Float, nullable=True)

    current_progress = db.Column(db.Float, default=0)
    start_date = db.Column(db.Date, default=datetime.utcnow)
    end_date = db.Column(db.Date, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    is_achieved = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
