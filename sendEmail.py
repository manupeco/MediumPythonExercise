import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Content, MimeType,
    Mail,Attachment,Attachment,FileName,FileContent,FileType,Disposition,ContentId,TemplateId,To,Subject,From )



mailApiKey = os.environ['MAIL_API_KEY']

def sendMailWithPdf(email):
    #mailMsg = '{
     #       "subject": "subject",
      #      "to": "emanuele.pecorari@gmail.com",
       #     "from": "noreply-stats@myteammanager.club",
        #    "text": "Text",
         #   "html": "",
          #  "filename": "stats.xlsx",
           # "contentId": "stats"
    #}'
    #mailMsgJson = json.loads(mailMsg)
    message = Mail()
    message.to = To(email.data['to'])
    message.subject = Subject(email.data['subject'], p=0)
    message.from_email = From(email.data['from'], 'My Team Manager')

    message.template_id = TemplateId(email.data['templateId'])
    message.attachment = Attachment(FileContent(email.data['pdf']),
                                FileName(email.data['filename']),
                                FileType('application/pdf'),
                                Disposition('attachment'),
                                ContentId('Content ID 1'))  
    message.content = Content(
    MimeType.text,
    email.data['text'])
    message.content = Content(
    MimeType.html,
    email.data['html'])
    sg = SendGridAPIClient(mailApiKey)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)    