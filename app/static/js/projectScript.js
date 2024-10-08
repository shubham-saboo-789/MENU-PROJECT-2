// Function to load AWS content from aws.html into the mainContainer
// function loadPythonContent() {
//     const mainContainer = document.getElementById("mainContainer");

//     // Fetch the AWS content from aws.html
//     fetch('/static/html/projectsHtml.html')
//         .then(response => response.text())
//         .then(data => {
//             // Insert the fetched content into #mainContainer
//             mainContainer.innerHTML = data;
//         })
//         .catch(error => {
//             console.error('Error loading AWS content:', error);
//             mainContainer.innerHTML = '<p>Sorry, something went wrong while loading the content.</p>';
//         });
// }


// this is for the toggleCard

function toggleCard(cardImg) {
    const card = cardImg.parentElement;
    card.classList.toggle('expanded');
}




document.getElementById('p1_form').addEventListener('submit',p1_mail)
function p1_mail(e){
    e.preventDefault();
    var p1_senderEmail=document.getElementById("p1_senderEmail").value;
    var p1_senderEmailPassword=document.getElementById("p1_senderEmailPassword").value;
    var p1_receiverEmail=document.getElementById("p1_receiverEmail").value;
    var p1_subject=document.getElementById("p1_subject").value;
    var p1_body=document.getElementById("p1_body").value;
    
    var param={
        'p1_senderEmail':p1_senderEmail,
        'p1_senderEmailPassword':p1_senderEmailPassword,
        'p1_receiverEmail':p1_receiverEmail,
        'p1_subject':p1_subject,
        'p1_body':p1_body
    }
    
    var xhr=new XMLHttpRequest();
    
    xhr.open('post','../p1_mail',true);
    
    xhr.setRequestHeader('Content-type', 'application/json');
    
    xhr.onload=function(){
        console.log("email reached till onload");
        document.getElementById('p1_result').innerHTML=this.responseText;
    }
    xhr.send(JSON.stringify(param));
}

document.getElementById('p2_form').addEventListener('submit',p2_sms)
function p2_sms(e){
    e.preventDefault();
    var p2_account_sid=document.getElementById("p2_account_sid").value;
    var p2_auth_token=document.getElementById("p2_auth_token").value;
    var p2_twilio_no=document.getElementById("p2_twilio_no").value;
    var p2_receivers_no=document.getElementById("p2_receivers_no").value;
    var p2_message=document.getElementById("p2_message").value;
    
    var param={
        'p2_account_sid':p2_account_sid,
        'p2_auth_token':p2_auth_token,
        'p2_twilio_no':p2_twilio_no,
        'p2_receivers_no':p2_receivers_no,
        'p2_message':p2_message
    }
    
    var xhr=new XMLHttpRequest();
    
    xhr.open('post','../p2_sms',true);
    
    xhr.setRequestHeader('Content-type', 'application/json');
    
    xhr.onload=function(){
        console.log("sms reached till onload");
        document.getElementById('p2_result').innerHTML=this.responseText;
    }
    xhr.send(JSON.stringify(param));
}

document.getElementById('p3_form').addEventListener('submit',p3_top5_google)
function p3_top5_google(e){
    e.preventDefault();
    var p3_query=document.getElementById("p3_query").value;
    
    var param={
        'p3_query':p3_query
    }
    
    var xhr=new XMLHttpRequest();
    
    xhr.open('post','../p3_top5_google',true);
    
    xhr.setRequestHeader('Content-type', 'application/json');
    
    xhr.onload=function(){
        console.log("query reached till onload");
        document.getElementById('p3_result').innerHTML=this.responseText;
    }
    xhr.send(JSON.stringify(param));
}

document.getElementById('p4_form').addEventListener('submit',p4_find_geoLocation)
function p4_find_geoLocation(e){
    e.preventDefault();
    
    var xhr=new XMLHttpRequest();
    
    xhr.open('post','../p4_find_geoLocation',true);
    
    xhr.setRequestHeader('Content-type', 'application/json');
    
    xhr.onload=function(){
        console.log("post request reached till onload");
        document.getElementById('p4_result').innerHTML=this.responseText;
    }
    xhr.send();
}


document.getElementById('p5_form').addEventListener('submit',p5_text_to_speech)
function p5_text_to_speech(e){
    e.preventDefault();
    var p5_text=document.getElementById("p5_text").value;
    
    var param={
        'p5_text':p5_text
    }
    
    var xhr=new XMLHttpRequest();
    
    xhr.open('post','../p5_text_to_speech',true);
    
    xhr.setRequestHeader('Content-type', 'application/json');
    
    xhr.onload=function(){
        console.log("query reached till onload");
        document.getElementById('p5_result').innerHTML=this.responseText;
    }
    xhr.send(JSON.stringify(param));
}

document.getElementById('p6_form').addEventListener('submit',p6_set_volume)
function p6_set_volume(e){
    e.preventDefault();
    var p6_per=document.getElementById("p6_per").value;
    
    var param={
        'p6_per':p6_per
    }
    
    var xhr=new XMLHttpRequest();
    
    xhr.open('post','../p6_set_volume',true);
    
    xhr.setRequestHeader('Content-type', 'application/json');
    
    xhr.onload=function(){
        console.log("query reached till onload");
        document.getElementById('p6_result').innerHTML=this.responseText;
    }
    xhr.send(JSON.stringify(param));
}

document.getElementById('p7_form').addEventListener('submit',p7_sms_phone)
function p7_sms_phone(e){
    e.preventDefault();
    var p7_sendX=document.getElementById("p7_sendX").value;
    var p7_sendY=document.getElementById("p7_sendY").value;
    var p7_phone=document.getElementById("p7_phone").value;
    var p7_body=document.getElementById("p7_body").value;
    
    var param={
        'p7_sendX':p7_sendX,
        'p7_sendY':p7_sendY,
        'p7_phone':p7_phone,
        'p7_body':p7_body
    }
    
    var xhr=new XMLHttpRequest();
    
    xhr.open('post','../p7_sms_phone',true);
    
    xhr.setRequestHeader('Content-type', 'application/json');
    
    xhr.onload=function(){
        console.log("email reached till onload");
        document.getElementById('p7_result').innerHTML=this.responseText;
    }
    xhr.send(JSON.stringify(param));
}