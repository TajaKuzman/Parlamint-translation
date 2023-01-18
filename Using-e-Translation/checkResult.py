@app.route('/checkResult', methods=['POST'])
def checkResult(idRequest):
    return correlationMap[idRequest]