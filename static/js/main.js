
$(document).ready(function(){
    textarea = $('#text-area');
    submitBtn = $('#submitBtn');
    submitBtn.click(function(){
        handleSubmit()
    });
});


function handleSubmit(){
    email = textarea.val();
    if(email == ""){
        document.getElementById('result-header').innerText = "";
    }else{
        var dataToSend = {
            'email' : email
        }
        let URL = 'test';
        $.ajax({
            method: 'POST',
            url: URL,
            type: 'json',
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(dataToSend),
            success: function(result){
                document.getElementById('result-header').innerText = result;
            },
            error: function(error){
                console.log(error);
            }
        })
    }
}