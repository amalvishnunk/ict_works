const http=require('http');
const server=http.createServer();
server.listen(3000);
console.log('listening to port 3000');
//simple server without callback