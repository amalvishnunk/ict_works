// async read eg
const fs=require('fs');
fs.readdir('./',function(e,files){
    if(e) console.log(e);
    else console.log(files);
});