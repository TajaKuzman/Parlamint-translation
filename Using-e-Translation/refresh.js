function refresh(idRequest, nbRetry) {
    $.ajax({
        url : "[Your server address]/checkresult",
        data : {
                    'idRequest': idRequest
               },
        type : 'POST',
        success : function(data) {
            if(data != ''){
                $("#textAreaTranslation").value = data;
            } else if (nbRetry = 0){
                $("#textAreaTranslation").value = "TIMEOUT!";
            } else {
                setTimeout(refresh(idRequest, --nbRetry), 1000);
            }
        }
    });
}