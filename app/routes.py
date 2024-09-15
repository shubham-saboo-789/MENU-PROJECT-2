from app import app
from flask import Flask, request, render_template,jsonify

import sys
import os
# sys.path.append(os.path.abspath('/pythonTasks'))
# import p1_mail
from pythonTasks.p1_mail import mail_api
from pythonTasks.p2_sms import sms_api
from pythonTasks.p3_top5_google import search_query_api
from pythonTasks.p4_find_geoLocation import get_current_location
from pythonTasks.p5_text_to_speech import text_speech_api
from pythonTasks.p6_set_volume import volume_api
from pythonTasks.p7_sms_phone import send_sms_api



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

@app.route('/p4_find_geoLocation', methods=["POST"])
def p4_find_geoLocation():    
    try:
        lat, lng, add=get_current_location()
        return jsonify({'status': 'success', 'message': {'latitude':lat,'longitude':lng,'address':add}}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/p5_text_to_speech', methods=["POST"])
def p5_text_to_speech():
    text=request.json['p5_text']
    print(f'{text}: reached till route')
    try:
        text_speech_api(text)
        return jsonify({'status': 'success', 'message': 'text to speech successfully!'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/p6_set_volume', methods=["POST"])
def p6_set_volume():
    per=request.json['p6_per']
    
    try:
        volume_api(per)
        return jsonify({'status': 'success', 'message': 'volume change successfully!'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/p7_sms_phone', methods=["POST"])
def p7_sms_phone():
    sendX=request.json['p7_sendX']
    sendY=request.json['p7_sendY']
    phone_number=request.json['p7_phone']
    message=request.json['p7_body']
    try:
        send_sms_api(sendX,sendY, phone_number, message)
        return jsonify({'status': 'success', 'message': 'Sms sent successfully!'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.errorhandler(404)
def page_not_found(e):
    return "File not found", 404