function calc(){
var op1=document.getElementById("getno1").value;
var op2=document.getElementById("getno2").value;
var x=document.getElementById("getid");
var p=x.options[x.selectedIndex].value;
var res;

if(p=="add"){
    res=parseInt(op1)+parseInt(op2);
}
else if(p=="sub"){
    res=parseInt(op1)-parseInt(op2); 
}
else if(p=="div"){
    res=parseInt(op1)/parseInt(op2);
}
else{
    res=parseInt(op1)*parseInt(op2);
}

console.log(res);


}