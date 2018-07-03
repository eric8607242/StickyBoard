$(document).ready(function(){ console.log("Hey")
    // get whether you have relation or not
    get_relation()
})

$('#addBoard').submit(function(e){
    console.log($('#titleInput'))
    e.preventDefault()
    if($('#titleInput').val().length < 3){
        alert("Title too short")
    }
    else
        identiFy($('#titleInput').val(),$('#closeBoard'))
})

$('#subBoard').submit(function(e){
    console.log($('#deleteInput'))
    e.preventDefault()
    board_name = $('#deleteInput').val()
    delete_board(board_name,$('#closeBoard2'))
})

$('#invite').submit(function(e){
    console.log("------------------")
    e.preventDefault()
    inviter = $('#my_name').val()
    invitee = $('#friend_name').val()
    panel_name = $('#panel_name').val()
    invite_friend(panel_name, inviter, invitee)
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

function sub_A_Tag(name){
    let new_name = " " + name + " "
    a_list = document.getElementsByTagName("a")
    if(a_list){
        for (let i = 0;i < a_list.length ;i++){
            if(a_list[i].textContent == new_name){
                a_list[i].remove()
            }
        }
    }
}

function a_tag_func(event){
    let link_name = event.target.textContent
    goPanel(link_name)
}

function identiFy(name,close){
    $.ajax({
        type:'POST',
        url: '/createboard/', //Check whether this board created yet
        data:{
            boardname: name,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
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

function delete_board(name,close){
    $.ajax({
        type:'POST',
        url: '/deleteboard/', //Check whether this panel created yet
        data:{
            board_name: name,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(response){
            if(response == "success"){
                sub_A_Tag(name)
                close.click()
            }
        },
        error: function(){
            alert("Send failed")
        }
    })
}

function invite_friend(board_name , inviter, invitee){
    $.ajax({
        type:'POST',
        url: '/invite/', //Check whether this panel created yet
        data:{
            board_name: board_name,
            invitee: invitee,
        },
        success: function(response){
            alert(response)
        },
        error: function(){
            alert("Send failed")
        }
    })
}

function get_relation(){
    $.ajax({
        type:'POST',
        url: '/invitestatus/',
        data:{
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            if(response == "No invitaion"){

            }
            else{
                let invitation = JSON.parse(response)
                console.log(invitation)
                add_tr_tag(invitation)
            }
        },
        error: function(){
            alert("Send failed")
        }
    })
}

function add_tr_tag(invitation){
    let invitation_account = invitation.length
    console.log("add_tr_tag")
    console.log(invitation_account)
    for (let index = 0; index < invitation_account ; index++){
        console.log("HH")
        let tr_tag = document.createElement("tr") 
        let td_tag_inviter = document.createElement("td")
        let td_tag_panel_name = document.createElement("td")
        let td_tag_accept = document.createElement("td")
        let td_tag_cancel = document.createElement("td")
        let a_tag_accept = document.createElement("a")
        let a_tag_cancel = document.createElement("a")
        a_tag_accept.setAttribute("href","#")
        a_tag_accept.addEventListener("click",accept_relation)
        a_tag_cancel.setAttribute("href","#")
        a_tag_cancel.addEventListener("click",delete_relation)
        accept_content = document.createTextNode("accept")
        cancel_content = document.createTextNode("cancel")
        a_tag_accept.appendChild(accept_content)
        a_tag_cancel.appendChild(cancel_content)
        td_tag_accept.appendChild(a_tag_accept)
        td_tag_cancel.appendChild(a_tag_cancel)


        inviter_content = document.createTextNode(invitation[index].inviter)
        panel_name_content = document.createTextNode(invitation[index].panel_name)
        td_tag_inviter.appendChild(inviter_content)
        td_tag_panel_name.appendChild(panel_name_content)

        tr_tag.appendChild(td_tag_inviter)
        tr_tag.appendChild(td_tag_panel_name)
        tr_tag.appendChild(td_tag_accept)
        tr_tag.appendChild(td_tag_cancel)

        $('#invitation_table').append(tr_tag)

    }
}

function delete_relation(event){
    let tr_tag = event.target.parentElement.parentElement
    let inviter_name = tr_tag.childNodes[0].textContent
    let panel_name = tr_tag.childNodes[1].textContent
    let invitee_name = localStorage["account"]
    $.ajax({
        type:'POST',
        url: '/refuserelation/',
        data:{
            inviter_name: inviter_name,
            panel_name: panel_name,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            if(response == "delete success"){
                tr_tag.remove()
            }
            else{
                
                alert(response)
            }
        },
        error: function(){
            alert("Send failed")
        }
    })

}

function accept_relation(event){
    let tr_tag = event.target.parentElement.parentElement
    let inviter_name = tr_tag.childNodes[0].textContent
    let panel_name = tr_tag.childNodes[1].textContent
    console.log(panel_name)
    $.ajax({
        type:'POST',
        url: '/acceptrelation/',
        data:{  
            inviter_name: inviter_name,
            panel_name: panel_name,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            if(response == "accept success"){
                tr_tag.remove()
            }
            else{
                alert(response)
            }
        },
        error: function(){
            alert("Send failed")
        }
    })

}

function goPanel(panel_name){
    if(panel_name[0] == ' ')
        panel_name = panel_name.substr(1,panel_name.length-2)
    localStorage["panel_name"] = panel_name
    window.location='localhost:8000/website/directPanel/' + "?" + "account=" +localStorage["account"] + "&" + "panel_name=" + panel_name
}


