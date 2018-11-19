const fs=require('fs');
fs.readFile('txtfile.txt','utf8',function(err,data){
    if(err) console.log(err);
    else console.log(data);
});

// async file read