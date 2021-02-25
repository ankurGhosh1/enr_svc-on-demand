from .emails import send_html_mail
host = 'https://localhost:8000'

def new_job_template(TopicName, content):
    return f'<div> <h3>{TopicName}</h3><div>{content}</div></div>'

def new_jobApplied_template(TopicName, host):
    return f'<div><h3>Job Name: {TopicName}</h3><br><br><div><a href="{host}/client/reviewapplications/">Click To view</a></div></div>'


class Notification:
    @staticmethod
    def createjobNoti(email, content, TopicName, **kwargs):
        send_html_mail('New Job Posted Successfully', new_job_template(TopicName, content), email)

    @staticmethod
    def appliedOnJob(email, job, **kwargs):
        print(email)
        send_html_mail('A new job application', new_jobApplied_template(job, host), email)
