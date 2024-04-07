from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///db.sqlite3"
app.config['SQLALCHEMY_TRACK_NOTIFICATION']=False

db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20))
    notes=db.relationship('Notes',backref='user')

    '''
back ref ek back reference create karta hai jisey ham kehte hai  k dusre table se bhi ham pehle waale table k instances ko access kar sakey uss colum k naam se jisme back ref diya hua hai
    '''

    def __repr__(self) -> str:
        return f"<User:{self.name}>"


class Notes(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    note=db.Column(db.String(20))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id', ondelete="CASCADE")
    )
    '''
    on delete = cascade se yeh samajhna chahiye ki jab bhi user agar delete kar diya jaaey toh ussey related notes ya koi bhi related chiz delete ho jaani chahiye
    '''
 
    def __repr__(self) -> str:
        return f"<Note:{self.note}>"


if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)