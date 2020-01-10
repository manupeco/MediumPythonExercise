from callsupPDF import CallsUpPDF
from emailObj import EmailObj
from sendEmail import sendMailWithPdf
import base64
from requestUtil import getStringParameter

def sendCallsUp(req_data):
    pdf = CallsUpPDF(req_data)    
    pdf.composeDoc()        
    encodedStr = base64.b64encode(pdf.output(dest='S').encode("latin-1")).decode("latin-1")   
    print(encodedStr)
    emailData = {
         "to": getStringParameter(req_data, 'to'),
         "subject": getStringParameter(req_data, 'subject'),
         "html": getStringParameter(req_data, 'html'),
         "text": getStringParameter(req_data, 'text'),
         "from": "noreply-stats@myteammanager.club",
         "pdf": encodedStr,
         "filename": "callsup.pdf",
         "templateId": "e628ae81-c314-4c22-8626-ec5b362cebba"
    }    
    emailObject = EmailObj(emailData)
    try:
        sendMailWithPdf(emailObject)
        return "Ok"
    except Exception as e:
        print(str(e))
        return str(e), 500