from flask import Flask, render_template, request, redirect, flash, session
import re
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
password_regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{4,8}$')
app = Flask(__name__)
app.secret_key='Top_Secret'
@app.route('/')
def index():
	return render_template("index.html")
@app.route('/reg', methods=['POST'])
def reg():
	session['email'] = request.form['email']
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['password'] = request.form['password']
	session['confirm'] = request.form['confirm_pw']
	
	if len(session['email']) < 1:
		flash("Sorry too short")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Sorry not an email")
	else:
		flash(session['email'])
	
	if session['first_name'].isalpha():
		print "yep it works"
	else:
		session['first_name'] = "Sorry dude you got numbers"
		print "Sorry got number"

	if session['last_name'].isalpha():
		print 'it works too'
	else:
		session['last_name'] = "Try again not valid last name"
		print "try again"
		
	
	if not password_regex.match(request.form['password']):
		session['match'] = "Whered youd learn how to type dude? PW dont match"
	
	else:
		print "Match!"
		session['match'] = "Good Job"

	if  len(session['password']) == len(session['confirm']):
		session['match'] = "its a MAtch!"
	else:
		session['match'] = "Sorry PW is too long"

	return redirect ('/results')
@app.route('/results')
def register():
	return render_template("results.html",email=session['email'],first=session['first_name'],last=session['last_name'], match=session['match'])
app.run(debug=True)