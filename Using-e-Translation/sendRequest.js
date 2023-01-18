$("submitbutton").click(function(event) {
    $.ajax({
        url : "[Your server address]/receiveRequest",
        data : {
                    textToTranslate : $('#textAreaOriginal').val(),
                    sourceLanguage : $('#sourceLanguageCombo').val(),
                    targetLanguage : $('#targetLanguageCombo').val()
                },
        type : 'POST',
        success : function(data) {
            if(data > 0){
                refresh(data, 5);
            }
        }
    });
});