function do_some_ajax(){
    jQuery.ajax({
        url     : 'ajax_view',
        type    : 'POST',
        dataType: 'json',
        success : function(data){
            alert("Gratulacje, udalo Ci sie wyswietlic wiadomosc:\n "+ data.message)
        }
    });
}