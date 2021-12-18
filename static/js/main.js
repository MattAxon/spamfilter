
$(document).ready(function(){
    textarea = $('#text-area')
    submitBtn = $('#submitBtn');
    submitBtn.click(function(){
        handleSubmit()
    });
});


function handleSubmit(){
    console.log("handled");
    email = textarea.val();
    var dataToSend = {
        'email' : email
    }
    let URL = 'test';
    $.ajax({
        type: 'POST',
        url: URL,
        type: 'json',
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(dataToSend),
        success: function(result){
            console.log(result);
        },
        error: function(error){
            console.log(error);
        }
    })
}