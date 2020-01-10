#def getStringParameterFromGet(requestData, parameterName):
#    return requestData.get(parameterName, default='')

def getStringParameter(requestData, parameterName):
    return requestData.get(parameterName, '')