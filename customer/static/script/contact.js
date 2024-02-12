function validateform(){
    var username=document.getElementById("user name").value
    var email=document.getElementById("email").value
    var phonenumber=document.getElementById("phonenumber").value
    var text=document.getElementById("text")
    



    if (username===""||email===""||phonenumber===""){
        document.getElementById("error").innerHTML="Invalid email or password"


        return false
    }else if(){
        please fill all the feilds
        return false
    }


    else{
        return true
    }
}