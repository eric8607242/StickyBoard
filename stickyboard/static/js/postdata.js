$(document).on('submit','#postData',function(e){
    e.preventDefault()
    $.ajax({
        type:'POST',
        url: '/website/stickyBoard/saveBoard/',
        data:{
            stickyBoard: localStorage["POSTData"],
            panel_name: localStorage["panel_name"],
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
