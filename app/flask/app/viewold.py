from app import app  

#app = Flask(__name__)



from flask import render_template
import requests
import json
#from flask import FLASK , jsonify
#app = Flask(__name__)

@app.route('/')
def homepage():


  url = 'https://api.chucknorris.io/jokes/random'
  #proxies = {
   #   "http": "http://jx954:Jan*3189@webproxy.deutsche-boerse.de:8080"
  #}
  r = requests.get(
      url)

  return render_template('view.html', jokes=json.loads(r.text)['value'])
  
