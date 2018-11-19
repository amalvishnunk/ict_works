const http=require('http');
const server=http.createServer(function(req,res){
    res.write("hello world");
    res.end();
    // console.log(res);
});
server.listen(3000);
console.log('listening to port 3000');