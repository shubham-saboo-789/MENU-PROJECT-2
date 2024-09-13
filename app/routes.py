from app import app
from flask import Flask, request, render_template,jsonify

import sys
import os
# sys.path.append(os.path.abspath('/pythonTasks'))
# import p1_mail
from pythonTasks.p1_mail import mail_api


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/p1_mail', methods=["POST"])
def p1_mail():
    from_email=request.json['p1_senderEmail']
    from_email_password=request.json['p1_senderEmailPassword']
    to_email=request.json['p1_receiverEmail']
    subject=request.json['p1_subject']
    body=request.json['p1_body']
    
    try:
        mail_api(from_email, from_email_password, to_email, subject, body)
        return jsonify({'status': 'success', 'message': 'Email sent successfully!'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.errorhandler(404)
def page_not_found(e):
    return "File not found", 404