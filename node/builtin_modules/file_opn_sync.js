const fs=require('fs');
var data=fs.readFileSync('txtfile.txt','utf8');
console.log(data);
// sync file read