from flask import Flask, render_template, url_for, request, redirect
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#db = SQLAlchemy(app)

#class Todo(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    owner = db.Column(db.String(20), nullable=False)
#    coursecode = db.Column(db.String(20), nullable=False)
#    groupname = db.Column(db.String(20), nullable=False, unique=True)
#    members = db.Column(db.String(20), nullable=False)
#
#
#    def __repr__(self):
#        return '<Task %r>' % self.id

class getto_db:
    def __init__(self) -> None:
        self.db = {}
        self.group_id = 0
    
    def add_data(self, owner, groupname, coursecode):
        pass



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        pass
    else:
        return render_template('create.html')

@app.route('/find')
def find():
    return render_template('find.html')


@app.route('/notes')
def notes():
    return render_template('notes.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()