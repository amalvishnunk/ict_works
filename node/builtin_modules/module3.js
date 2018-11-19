// template string
const os =require('os');
var totalMem=os.totalmem();
// var freeMem=os.freemem();

console.log(`Total memory= ${totalMem}`);
console.log(`Free Memory= ${os.freemem()}`)