var fs = require("fs")
try{fs.readFile("app1.js", "utf-8", function (err, data) {
    if (err) {
        throw err
    }
    console.log(data);
    
})}catch{
    
}
