from app import app
from flask import Flask, request, render_template,jsonify

import sys
import os
# sys.path.append(os.path.abspath('/pythonTasks'))
# import p1_mail
from pythonTasks.p1_mail import mail_api
from pythonTasks.p2_sms import sms_api
from pythonTasks.p3_top5_google import search_query_api



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
    
@app.route('/p2_sms', methods=["POST"])
def p2_sms():
    account_sid=request.json['p2_account_sid']
    auth_token=request.json['p2_auth_token']
    twilio_phone_no=request.json['p2_twilio_no']
    number=request.json['p2_receivers_no']
    message=request.json['p2_message']
    
    try:
        sms_api(account_sid,auth_token,twilio_phone_no,number, message)
        return jsonify({'status': 'success', 'message': 'Sms sent successfully!'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/p3_top5_google', methods=["POST"])
def p3_top5_google():
    query=request.json['p3_query']
    
    try:
        res=search_query_api(query)
        return jsonify({'status': 'success', 'message': res}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.errorhandler(404)
def page_not_found(e):
    return "File not found", 404