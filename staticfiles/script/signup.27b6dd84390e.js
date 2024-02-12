function validateform(){
    alert('password must be ateast 8 character')
    var username=document.getElementById("user name").value
    var email=document.getElementById("email").value
    var phonenumber=document.getElementById("phonenumber").value
    var password=document.getElementById("password").value
    var confirmpassword=document.getElementById("confirmpassword").value



    if (username===""||email===""||phonenumber===""||password===""||confirmpassword===""){
        document.getElementById("error").innerHTML="Invalid email or password"


        return false
    }else if(password.length<6){
        return false
    }


    else{
        return true
    }
}