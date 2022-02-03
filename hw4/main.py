from distutils.debug import DEBUG
from distutils.log import debug
from operator import truediv
from pickle import TRUE
import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    list_TVshows=["Game of Thrones","Record of Ragnarok","Lucifer","The Good Doctor","The Seven Deadly Sins"]
    list_images=["/static/GoT.jpg","/static/ragnarok.jpg","/static/lucifer.jpg","/static/sevendeadlysins.jpg","/static/thegooddoctor.jpg"]
    return flask.render_template("index.html",name="Hoan",len1=len(list_TVshows),list1=list_TVshows,len2=len(list_images),list2=list_images)

app.run(debug=True)
