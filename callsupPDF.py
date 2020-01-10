
from fpdf import FPDF
import urllib.request
import time
from requestUtil import getStringParameter

class CallsUpPDF(FPDF):

    def __init__(self, req_data):
        self.req_data = req_data
        super(CallsUpPDF, self).__init__()

    def header(self):
        # Logo                     
        logoUrl = getStringParameter(self.req_data,'logoUrl') 
        if logoUrl:
            millis = int(round(time.time() * 1000))
            filePath = "/tmp/%s.png" % str(millis)
            f = open(filePath,'wb')
            f.write(urllib.request.urlopen(logoUrl).read())
            f.close()
            self.image(filePath, 10, 8, 33)

        # Match
        self.set_font('Arial', 'B', 15)                
        match = getStringParameter(self.req_data,'match')   
        print("match: " + match) 
        if match:
            self.cell(0, 5, match, ln=1, align='C')
        
        # Match Date        
        date = getStringParameter(self.req_data,'date')   
        if date:   
            self.set_font('Arial', '', 12)
            self.cell(0, 5, date, ln=1, align='C')

        # Line break
        self.ln(8)

    def __addAppointmentAndPlace(self):
        appointmentAndPlace = getStringParameter(self.req_data, 'appointmentAndDate')
        if appointmentAndPlace:
            self.set_font('Arial', '', 12)
            self.cell(0, 10, appointmentAndPlace, ln=1, align='C')
            self.ln(2)

    def __addStadeAddress(self):
        stadeAddress = getStringParameter(self.req_data, 'stadeAddress')        
        if stadeAddress:
            self.set_font('Arial', '', 12)
            self.cell(0, 10, stadeAddress, ln=1, align='C')

    def __callsUpBlock(self):
        self.ln(8)        
        callsup = getStringParameter(self.req_data, 'callsup')               
        callsupTitle = getStringParameter(self.req_data, 'callsupTitle')        
        self.set_font('Arial', 'B', 12)
        self.cell(0, 5, callsupTitle, ln=1)
        self.ln(3)
        callsup = callsup.replace(', ', ",")
        players = callsup.split(',')
        self.set_font('Arial', '', 12)
        for player in players:
            self.cell(0, 5, player, ln=1)
        

    def composeDoc(self):
        self.add_page()
        self.set_font('Arial', 'B', 16)          
        self.__addAppointmentAndPlace()      
        self.__addStadeAddress()        
        self.ln(6)
        self.__callsUpBlock()

        