from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from docx2pdf import convert


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_mail_task():
    send_mail("Celery Worked", "Celery is awosome",
            "cardscientists@gmail.com", 
            ["charan1631@gmail.com"],
            fail_silently= False
            )
    print("mail from celery")
    return None

@shared_task
def convert_doc_to_pdf(myfile):
    # sleep(10)
    convert('hotels/static/' + myfile)
    return None


