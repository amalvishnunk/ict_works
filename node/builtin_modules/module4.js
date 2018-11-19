// fs module
const fs=require('fs');
const file=fs.readdirSync('./');//sync read
console.log(file);
