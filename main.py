from flask import Flask,render_template,flash, redirect,url_for,session,logging,request, render_template
from flask_sqlalchemy import SQLAlchemy
from selenium import webdriver
from bs4 import BeautifulSoup
from input import get_input
from show import showres
import concurrent.futures


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Nihat Eliyev/Desktop/uno/database.db'
db = SQLAlchemy(app)



PATH="chromedriver.exe"


options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values': { 'images': 2, 'javascript': 2,
							'plugins': 2, 'popups': 2, 'geolocation': 2, 
							'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 
							'mouselock': 2, 'mixed_script': 2, 'media_stream': 2, 
							'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 
							'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 
							'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 
							'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 
							'durable_storage': 2,"profile.managed_default_content_settings.images": 2}}

options.add_experimental_option("prefs", prefs)
options_aliexpress = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values': { 'images': 2,
							'plugins': 2, 'popups': 2, 'geolocation': 2, 
							'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 
							'mouselock': 2, 'mixed_script': 2, 'media_stream': 2, 
							'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 
							'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 
							'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 
							'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 
							'durable_storage': 2,"profile.managed_default_content_settings.images": 2}}
options_aliexpress.add_experimental_option("prefs", prefs)


def fff():
	return webdriver.Chrome(PATH,chrome_options=options_aliexpress)
def sss():
	return webdriver.Chrome(PATH,chrome_options=options)
def ttt():
	return webdriver.Chrome(PATH,chrome_options=options)

with concurrent.futures.ThreadPoolExecutor() as executor:
		start1 = executor.submit(fff)
		start2 = executor.submit(sss)
		start3 = executor.submit(ttt)
		ress = [
			f.result()
			for f in (start1,start2,start3)
		]
		driver=ress[0]
		driver1=ress[1]
		driver2=ress[2]

def ff():
	urls_1='https://aliexpress.ru/wholesale?catId=0&SearchText=computer'
	driver.get(urls_1)
def ss():
	urls_2='https://www.amazon.com/s?k=computer'
	driver1.get(urls_2)
def tt():
	urls_3='https://tap.az/elanlar?keywords=computer'
	driver2.get(urls_3)

#Decreasing startup time with threading
with concurrent.futures.ThreadPoolExecutor() as executor:
		start1 = executor.submit(ff)
		start2 = executor.submit(ss)
		start3 = executor.submit(tt)
		ress = [
			f.result()
			for f in (start1,start2,start3)
		]

class user(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80))
	email = db.Column(db.String(120))
	password = db.Column(db.String(80))
 

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/search")
def search():
	return render_template("input.html")

@app.route('/search', methods=['POST'])
def search_post():
	inputt.get_input()
	return results(item,aliexpress,tapaz,amazon,sortt,price_min,price_max)

@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method == "POST":

		uname = request.form['uname']
		mail = request.form['mail']
		passw = request.form['passw']

		register = user(username = uname, email = mail, password = passw)
		db.session.add(register)
		db.session.commit()

		return redirect(url_for("login"))

	return render_template("register.html")

if __name__ == "__main__":
	db.create_all()
	app.run(debug=True)

@app.route("/login",methods=["GET", "POST"])
def login():
	if request.method == "POST":

		uname = request.form["uname"]
		passw = request.form["passw"]
		
		login = user.query.filter_by(username=uname, password=passw).first()

		if login is not None:
			return redirect(url_for("search"))

	return render_template("login.html")

