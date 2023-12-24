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

class ghetto_db:
    def __init__(self) -> None:
        self.db = {}
        self.group_id = 0
    
    def add_data(self, owner: str, groupname: str, coursecode: str) -> str:
        group_id = coursecode+str(self.group_id)
        self.db[group_id] = {'group_id': group_id, 'owner': owner, 'groupname': groupname, 'coursecode': coursecode, 'members': []}
        self.group_id += 1
        return group_id
    
    def find_data(self, coursecode: str) -> list:
        found = []
        for group_id in self.db:
            if coursecode in group_id:
                found.append(self.db[group_id])
        return found
    
    def join_group(self, group_id: str, memeber: str) -> None:
        self.db[group_id]['members'].append(memeber)


db = ghetto_db()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        group_id = db.add_data(request.form['username'], request.form['groupname'], request.form['coursecode'])
        data = db.find_data(group_id)
        return render_template('group.html', data=data)
    else:
        return render_template('create.html')

@app.route('/find', methods=['POST', 'GET'])
def find():
    if request.method == 'POST':
        data = db.find_data(request.form['coursecode'])
        return render_template('group.html', data=data)
    else:
        return render_template('find.html')


@app.route('/notes')
def notes():
    return render_template('notes.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()