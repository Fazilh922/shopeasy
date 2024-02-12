function validateform(){
    var email=document.getElementById("email").value
    var password=document.getElementById("password").value



    if (email===""||password===""){
        document.getElementById("error").innerHTML="Invalid email or password"


        return false
    }


    else{
        return true
    }
}