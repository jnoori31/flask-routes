from application import db


class Todos(db.model)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    state = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime, default=datetime.datetime.now)