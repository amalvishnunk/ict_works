 function read(){
    var name=document.getElementById("getname").value;
    var rollno=document.getElementById("getno").value;
    var admno=document.getElementById("getadmno").value;
    var age=document.getElementById("getage").value;
    var p=document.getElementById("getdistrict");
    var dist=p.options[p.selectedIndex].value;
console.log(dist);
    if(age<=18){//console.log("Not eligible");
    alert("Not eligible")}
    else{//console.log("Eligible");
    alert("Eligible..")}

    // console.log(name); 
    // console.log(rollno);
    // console.log(admno);
    // console.log(age);
}

