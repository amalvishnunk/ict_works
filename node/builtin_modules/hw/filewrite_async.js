const fs=require('fs');
fs.writeFile('txtfile.txt','asynchronous write',function(err,data){
    if(err)console.log(err);
    else console.log(data);
});