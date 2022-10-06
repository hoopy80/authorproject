# Import

from unicodedata import category
from urllib import request
from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

# Config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydata.db'
db = SQLAlchemy(app)

# Schema

class Author(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    category = db.relationship('Category',backref='all_categories')

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String)
    category = db.relationship('Author',backref='all_authors')
    author = db.Column(db.ForeignKey('author.id'))
    
     # DB Execution

db.create_all()
c1 = Author(id=1,name='Andrew Cartmel',)
c2 = Author(id=2,name='Peter Ackroyd',)
db.session.add(c1)
db.session.add(c2)
db.session.commit()

d1 = Category(id=1,name='Fiction' ,description='Fantasy')
d2 = Category(id=2,name='Non-Fiction' ,description='History') 
db.session.add(d1)
db.session.add(d2)
db.session.commit()

# Read operation

#all_author = Author.query.all()
#fic_author = Author.query.filter_by(Name='Andrew Cartmel')
#nonfic_author = Author.query.filter_by(Name='Peter Ackroyd')
#for aut in all_authors:
 #   print(aut.id,aut.name)
#aut2= Author.query.get(2)
#print(aut2.id,aut2.author)

# Update operation

#c1 = Author.query.get(1)
#c2 = Author.query.get(2)
#d1.genre = 'Fantasy'
#d2.genre = 'History'
#db.session.commit()

#non_object = Category.query.filter_by(name='Fiction')[0]
#d1 = .query.get(2)
#d1.category = non_object.id
#db.session.commit()

# Delete operation

#aut_to_del = Author.query.get(2)
#db.session.delete(aut_to_del)
#db.session.commit()

# HTML
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home_fun():
    if request.method == 'POST' and request.form.get('action') == 'Create':
        id = int(request.form.get('id'))
        author = request.form.get('author')
        category = request.form.get('category')
        c_new = Author(id=id,author=author,category=category)
        db.session.add(c_new)
        db.session.commit()
        return redirect(url_for('home_fun'))

    if request.method == 'POST' and request.form.get('action') == 'Search':
        search_query = request.form.get('genre')
        data_to_show = Author.query.filter_by(category=search_query)
    else:
        data_to_show = Author.query.all()

    if request.method == 'POST' and request.form.get('action') == 'Search':
        search_query = request.form.get('genre')
        data_to_show = Author.query.filter_by(category=search_query)
    else:
        data_to_show = Author.query.all()
    return render_template("home.html",list_of_data=data_to_show)


@app.route('/author/<int:id')
def author_fun(id):
        author_object = Author.query.get(id)
        return render_template("authors.html",data=author_object)

@app.route('/home_url')
def workex_fun():
        return render_template("home.html")

@app.route('/genres_url')
def education_fun():
	# processing
        return render_template("genres.html")

if __name__== '__main__': 
   app.run(debug=True,host='0.0.0.0',port=8000)
