from flask import Flask, request
app = Flask(__name__)

from functions import *

@app.route("/tweet-send-nort", methods = ['POST', 'GET'])
def callNoRt():
	retval = False

	if request.method == 'POST':
		tid = request.form['tweet-id']
		retval = send_tweet_mail(tid, False) # No retweets, "FALSE"

	if retval:
		return "SUCCESS"
	else:
		return "FAILURE - Possible retweet"

@app.route("/tweet-send-rt", methods = ['POST', 'GET'])
def callRt():
	retval = False

	if request.method == 'POST':
		tid = request.form['tweet-id']
		retval = send_tweet_mail(tid, True) # Retweets, "TRUE"

	if retval:
		return "SUCCESS"
	else:
		return "FAILURE - Possible retweet"

if __name__ == '__main__':
    app.run(host= '0.0.0.0')