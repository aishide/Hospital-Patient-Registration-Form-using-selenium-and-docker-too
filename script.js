function validateForm(){

let name = document.getElementById("name").value.trim();
let email = document.getElementById("email").value.trim();
let phone = document.getElementById("phone").value.trim();
let dob = document.getElementById("dob").value;
let genderSelected = document.querySelector('input[name="gender"]:checked');
let bloodType = document.getElementById("bloodType").value;


// NAME VALIDATION
let namePattern = /^[A-Za-z\s]+$/;

if(name === ""){
alert("Name cannot be empty");
return false;
}

if(!name.match(namePattern)){
alert("Name should contain only letters (no numbers allowed)");
return false;
}


// EMAIL VALIDATION
let emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

if(!email.match(emailPattern)){
alert("Please enter a valid Email ID");
return false;
}


// PHONE VALIDATION
let phonePattern = /^[0-9]{10}$/;

if(!phone.match(phonePattern)){
alert("Phone number must be 10 digits");
return false;
}


// DATE OF BIRTH VALIDATION
if(dob === ""){
alert("Please select your date of birth");
return false;
}


// GENDER VALIDATION
if(!genderSelected){
alert("Please select your gender");
return false;
}


// BLOOD TYPE VALIDATION
if(bloodType === ""){
alert("Please select your blood type");
return false;
}


alert("Patient Registration Successful!");

return true;

}