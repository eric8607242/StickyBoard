$('#addBoard').submit(function(e){
    console.log($('#titleInput'))
    e.preventDefault()
    if($('#titleInput').val().length < 3){
        alert("Title too short")
    }
    else
        identiFy($('#titleInput').val(),$('#closeBoard'))
})

function append_A_Tag(){
    alert("create")
    li_tag = document.createElement("li")
    li_tag.setAttribute("class","nav-item") 
    a_tag = document.createElement("a")
    a_tag.setAttribute("href","#")
    plain_text = $('#titleInput').val()
    a_tag.addEventListener("click",a_tag_func)
    a_tag.setAttribute("class","nav-link")
    a_tag.setAttribute("href","#")
    text_content = document.createTextNode($('#titleInput').val())
    a_tag.appendChild(text_content)
    li_tag.appendChild(a_tag)
    console.log($('#panel-container'))

    $('#panel-container').append(li_tag)
}

function a_tag_func(event){
    let link_name = event.target.textContent
    goPanel(link_name)
}
function identiFy(name,close){
    $.ajax({
        type:'POST',
        url: '/mainsite/createboard/', //Check whether this board created yet
        data:{
            boardname: name,
        },
        success: function(response){
            if(response == "success"){
                append_A_Tag()
                close.click()
            }
            else
                alert("This panelname has been used")
        },
        error: function(){
            alert("Send failed")
        }
    })
}

function goPanel(board_name){
    localStorage["board_name"] = board_name
    $.ajax({
       type:'GET',
       url: '/mainsite/directboard/', //Check whether this panel created yet
       data:{
           board_name: board_name,
       },
       success: function(response){
           $('body').html(response);
           if(response == "success"){

           }
           else
               alert("This panelname has been used")
       },
       error: function(){
           alert("Send failed")
       }
    })
    // panel_name = panel_name.substr(1,panel_name.length-2)
    
    // window.location='localhost:8000/website/directPanel/' + "?" + "account=" +localStorage["account"] + "&" + "panel_name=" + panel_name
}
