from callsupUseCase import sendCallsUp

def pdfmedium(request):    
    #req_data = request.args
    req_data = request.get_json()
    return sendCallsUp(req_data)        