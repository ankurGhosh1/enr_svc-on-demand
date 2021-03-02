from .emails import send_html_mail
host = 'https://localhost:8000'

def new_job_template(TopicName, content):
    return f'<div> <h3>{TopicName}</h3><div>{content}</div></div>'

def new_jobApplied_template(TopicName, host):
    return f'''<div><h3>Job Name: {TopicName}</h3><br><p>Someone Have applied to a job of your's with the above title<p><br><div><a href="{host}/client/reviewapplications/">Click To view</a></div></div>'''

def new_jobHired_template(TopicName, host, job_id):
    return f'''<div><h3>Job Name: {TopicName}</h3><br><p>Congratulations, You have been hired for a job with the above title<p><br><div><a href="{host}/job/{job_id}/">Click To view</a></div></div>'''


class Notification:
    @staticmethod
    def createjobNoti(email, content, TopicName, **kwargs):
        print(email)
        send_html_mail('New Job Posted Successfully', new_job_template(TopicName, content), email)

    @staticmethod
    def appliedOnJob(email, job, **kwargs):
        print(email)
        send_html_mail('A new job application', new_jobApplied_template(job, host), email)

    @staticmethod
    def hiredNoti(email, job, job_id, **kwargs):
        print(email)
        send_html_mail('Hired', new_jobHired_template(job, host, job_id), email)
