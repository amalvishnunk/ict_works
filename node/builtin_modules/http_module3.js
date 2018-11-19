const http=require('http')
const server=http.createServer(function(req,res){
    if(req.url=='/'){
        res.write("homepage");
        res.end();
    }
    if(req.url=='/users'){
        res.write(JSON.stringify([1,2,3,4]));
        res.end();
    }
});
server.listen(3000);
console.log("listening to port 3000")



// JSON.stringify([1,2,3,4])