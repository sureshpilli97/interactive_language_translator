function speek(){
    var s=confirm("Allow microphone");
    if(s){
        document.getElementById("acess-phone").value="True";
        document.getElementById("listen").style.display="block";
        document.getElementById("disp-text").style.display="none";
        document.getElementsById("voice").style.display="none";
    }
    else{
        alert("allow microphone to continue.....")
    }
}
function convert() {
    document.getElementById("disp-text").style.display="none";
    document.getElementsById("voice").style.display="none";
}
function valLan(){
    var r1 = document.getElementById("from_languages").value;
    var r2 = document.getElementById("languages").value;

    document.getElementById("l").value = r1;
    document.getElementById("f").value = r2;
    
}
function inpText() {
    document.getElementById('inp-text').style.display='block'; 
    document.getElementById('inp-file').style.display='none'; 
    document.getElementById('micro').style.display='none'; 
    document.getElementById('disp-text').style.display='none';
    document.getElementsById('voice').style.display='none';    
}
function inpFile() {
    document.getElementById('inp-text').style.display='none'
    document.getElementById('inp-file').style.display='block'; 
    document.getElementById('micro').style.display='none'; 
    document.getElementById('disp-text').style.display='none';
    document.getElementsById('voice').style.display='none';    
}
function disp(){
    var v = document.getElementById("disp-text");
    var val = v.innerHTML.trim();
    console.log(val);
    if(val !== "Empty"){
        if(val.includes("Empty")){
            val=val.replace("Empty","");
            v.innerHTML=val;
            v.style.display="block";
            document.getElementById("acess-phone").value="False";
        }
    }
    else{
        alert("click the mic to speek otherwise stop listening...");
    }
}
function downDoc(){
    content=document.getElementById("msg").innerHTML;
    var blob = new Blob([content], { type: 'text/html' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'document.txt';
    a.click();
    URL.revokeObjectURL(url);
}
let glow = 0; 
function aboutUs(){
    const glowingElement = document.getElementById("about");
    if (glow == 0) {
        glowingElement.style.boxShadow = `0 0 30px rgba(0, 0, 255, 0.7)`;
        glow++;
    } else {
        glowingElement.style.boxShadow = "none";
        glow--;
    }

}
let r=0,c=0;
function nav(){
    if(c!=0){
        r-=90;
        c-=1;
        document.querySelector(".nav-but").style.transform=`rotate(${r}deg)`;
        document.getElementById("nav-bar").style.display="none";
    }
    else{
        r+=90;
        c+=1;
        document.querySelector(".nav-but").style.transform=`rotate(${r}deg)`;
        document.getElementById("nav-bar").style.display="block";
    }
}