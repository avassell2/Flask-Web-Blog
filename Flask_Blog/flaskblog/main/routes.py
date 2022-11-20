from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__) # passing in name


@main.route("/") #routes the home/root page of website are what is typed in browsers to go to different pages
@main.route("/home")
def home():
    #posts = Post.query.all() #list all posts in user homepage
    page = request.args.get('page',1,type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5) #show set number of posts on homepage
    return render_template('home.html', posts=posts) #renders a html file



@main.route("/about") #about page
def about():
    return render_template('about.html')
    #"<h1>About Page</h1>"
