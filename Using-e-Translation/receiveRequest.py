!pip install flask
import flask
from flask import request
import requests;
import json; 

correlationMap = {}

@app.route('/receiveRequest', methods=['POST'])
def receiveRequest():
    textToTranslate  = request.form.get('textToTranslate ')
    sourceLanguage  = request.form.get('sourceLanguage ')
    targetLanguage  = request.form.get('targetLanguage ') 

    eTranslationRestUrl = "https://webgate.ec.europa.eu/etranslation/si/translate"

    applicationName = "PARLAMINT_IJS_SI_20230117"
    password = "16djjGqaF5tLhSVW"

    translationRequest = {}
    translationRequest['sourceLanguage'] = sourceLanguage
    translationRequest['targetLanguages'] = [targetLanguage]
    translationRequest['callerInformation'] = {"application" : applicationName, "username":"John Smith"}
    translationRequest['textToTranslate'] = textToTranslate
    translationRequest['requesterCallback'] = 'http://[MY_SERVER]:[MY_PORT]/callback'

    jsonTranslationRequest = json.dumps(translationRequest)

    jsonHeader = {'Content-Type' : 'application/json'}

    response = requests.post(eTranslationRestUrl, auth=HTTPDigestAuth(applicationName, password), headers = jsonHeader, data=jsonTranslationRequest)  

    requestId = response.text

    print("Request ID:" + requestId )

    if(requestId > 0):
        correlationMap[response.text] = "" 

    return response.text