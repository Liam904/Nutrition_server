from app.models import Meal, db
from app import create_app
from datetime import datetime, time, timedelta
from threading import Timer

app = create_app()


def reset_database():
    with app.app_context():
        Meal.query.delete()
        db.session.commit()


Timer(
    (
        datetime.combine(datetime.today(), time(14, 26, 59)) - datetime.now()
    ).total_seconds(),
    reset_database,
).start()
