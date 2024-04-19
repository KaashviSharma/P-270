# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define route and Verify_otp() function below
@app.route("/login",methods = ['POST'])
def verify_otp():
	username = request.form['username']
	password = request.form['password']
	mobile_number = request.form['number']
	if usename =='verify' and password=='12345':
		account_sid = "AC89d648110c0fb9cb084d25dca9bfbd74"
		auth_token = "1eefeb97ee624f82440277c0ee68ea42"
		client = Client(account_sid,auth_token)



        verification = client.verify \
            .services('Enter service sid from twilio') \
            .verifications \
            .create(to=enter mobile number variable here, channel='Enter mode of sending otp here')

    	print(verification.status)
    	return render_template("otp_verify.html")
    else:
    	return "entered user id or password is wrong"

if __name__ == "__main__":
    app.run()

#message id:MG14a3e00c554b5d7cf233081d3e538520