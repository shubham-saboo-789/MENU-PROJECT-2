import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Function to send an email using SMTP
def mail_api(from_email, from_email_password, to_email, subject, body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Ensure subject and body are encoded in UTF-8
    subject = subject.encode('utf-8').decode('utf-8')
    body = body.encode('utf-8').decode('utf-8')

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject

    # Add body to email with utf-8 encoding
    message.attach(MIMEText(body, 'plain', 'utf-8'))

    try:
        # Connect to the server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(from_email, from_email_password)
        server.sendmail(from_email, to_email, message.as_string())
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Function to send email using credentials from environment variables
def mail_noinput(to_email, subject, body):
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")
    
    if not smtp_user or not smtp_password:
        print("SMTP_USER or SMTP_PASSWORD environment variable is not set.")
        return

    mail_api(smtp_user, smtp_password, to_email, subject, body)

# Function to take user input and send email
def mail_input():
    to_email = input("Enter recipient's Email: ")
    subject = input("Enter Subject of your Email: ")
    body = input("Enter Body of your Email: ")
    mail_noinput(to_email, subject, body)

# If running this script directly, call the mail_input function
# if __name__ == "__main__":
#     mail_input()
