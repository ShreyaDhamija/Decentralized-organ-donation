function letters(evt) {
    var charCode = (evt.which) ? evt.which : event.keyCode
    if ((charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122) || charCode == 32 || charCode == 46)
        return true;
    else {
        //alert("Please Enter valid input");
        return false;
    }
}
function contact(evt) {
    var cno = document.getElementById("TextBox5").value;
    var charCode = (evt.which) ? evt.which : event.keyCode
    if ((charCode >= 47 && charCode <= 57)) {

        //alert("Please Enter valid input " + cno.length);
        if (cno.length <= 9) {
           // alert("Length " + cno.length);
            return true;
        
        }
        else
            return false;
    }
    else {

        return false;
    }
}
function aadharno(evt) {
    var cno = document.getElementById("TextBox5").value;
    var charCode = (evt.which) ? evt.which : event.keyCode
    if ((charCode >= 47 && charCode <= 57)) {

        //alert("Please Enter valid input " + cno.length);
        if (cno.length <= 11) {
            // alert("Length " + cno.length);
            return true;

        }
        else
            return false;
    }
    else {

        return false;
    }
}
function pincode(evt) {
    var cno = document.getElementById("TextBox4").value;
    var charCode = (evt.which) ? evt.which : event.keyCode
    
    if ((charCode >= 47 && charCode <= 57)) {

        //alert("Please Enter valid input " + cno.length);
        if (cno.length <= 5) {
            // alert("Length " + cno.length);
            return true;

        }
        else
            return false;
    }
    else {

        return false;
    }
}
function number(evt) {
    
    var charCode = (evt.which) ? evt.which : event.keyCode

    if ((charCode >= 47 && charCode <= 57)) {

            return true;

    }
    else {

        return false;
    }
}
function price(evt) {

    var charCode = (evt.which) ? evt.which : event.keyCode

    if ((charCode >= 47 && charCode <= 57) || charCode == 46) {

        return true;

    }
    else {

        return false;
    }
}
function card(evt) {
    var cno = document.getElementById("TextBox2").value;
    var charCode = (evt.which) ? evt.which : event.keyCode
    if ((charCode >= 47 && charCode <= 57)) {

        //alert("Please Enter valid input " + cno.length);
        if (cno.length <= 15) {
            // alert("Length " + cno.length);
            return true;

        }
        else
            return false;
    }
    else {

        return false;
    }
}