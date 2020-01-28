import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("hello.html")

    

@app.route("/more")
def more():
    return render_template("col-form.html")   

#@app.route('/')
#def index():
 #   now = datetime.datetime.now()
  #  new_year = now.month == 1 and now.day == 1
   # return render_template("new-year.html", new_year=new_year)
    


#@app.route('/')
#def index():
  #  headline = "hello"
   # return render_template("hello.html", headline=headline)


#@app.route('/bey')
#def bey():
   # headline = "bey"
    #return render_template("hello.html", headline=headline)   


#@app.route('/<string:name>')
#def hello_name(name):
 #   name = name.capitalize()
  #  return "<h1>Hello, {}!</h1>".format(name)

if __name__ == '__main__':
    app.run()
