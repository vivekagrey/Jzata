console.log("hello world ")
console.log("this is my funtions end up for this ")
function ReSendOTP(username ,mess_id)
{
    mess =document.getElementById(mess_id);
    console.log(mess)
    mess.innerText="sending" ;
    console.log(username)
 
    $.ajax({
        type:'GET',
        url:'/signup/resend',
        data:{usr:username},
        success:function(data)
        {
            mess.innerText = data ;
        }
    })

}

