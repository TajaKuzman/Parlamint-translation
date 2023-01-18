@app.route('/callback', methods=['POST'])
def callback():
    print('Callback received !')
    requestId = request.form.get('request-id')
    targetLanguage = request.form.get('target-language')
    translatedText = request.form.get('translated-text')
    print('Request ID: ' + requestId + ", Target language: " + targetLanguage + ", Translated text:" + translatedText)
    correlationMap[requestId] = translatedText
    return "OK"