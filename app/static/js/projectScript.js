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
