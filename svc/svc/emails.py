import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import threading
from threading import Thread

class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run (self):
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        msg = Mail(subject=self.subject, html_content=self.html_content, from_email='info@engagenreap.com', to_emails=self.recipient_list)
        response = sg.send(msg)
        print("sending email")
        print(response.status_code, response.body)

def send_html_mail(subject, html_content, recipient_list):
    EmailThread(subject, html_content, recipient_list).start()


class SyncMail:
    @staticmethod
    def sendMail(data):
        message = Mail(
            from_email='info@engagenreap.com',
            to_emails=[data['to_email']],
            subject=data['email_subject'],
            html_content=data['email_body']
        )
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
