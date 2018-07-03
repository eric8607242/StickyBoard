$(document).on('submit','#postData',function(e){
    console.log("-----------------")
    e.preventDefault()
    console.log(localStorage["boardName"])
    $.ajax({
        type:'POST',
        url: '/board/saveboard/',
        data:{
            board_info: localStorage["POSTData"],
            board_name: localStorage["boardName"],
            board_id: localStorage["board_id"],
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(response){
            if(response == "success"){
                alert("Hello")
            }
            else{
                alert(response)
            }
        },
        error: function(){
            alert("failed")
        },
    })
})
