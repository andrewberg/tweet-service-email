# Zapier Twitter Email Service

Email service to be triggered with a POST request written in Flask with Python.

Uses Flask, Request, re, Tweepy and JSON to parse and send emails based on the tweet id posted to it in the form 'tweet-id'.

Triggered by Zapier Twitter and then calls send_request.py on the Python module on zapier and emails to the given email.
