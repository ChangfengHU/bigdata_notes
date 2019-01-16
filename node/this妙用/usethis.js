// var laosiji={
//     name:"王晓静",
//     drive:function () {
//         setTimeout(function () {
//             console.log("我是"+this.name+",哈哈");
//
//         },2000)
//     }
// }
// laosiji.drive()
//
// var laosiji1={
//     name:"王晓静",
//     drive:function () {
//         setTimeout(function () {
//             console.log("1我是"+this.name+",哈哈");
//
//         }.bind(laosiji1),2000)
//     }
// }
// laosiji1.drive()
// var laosiji3={
//     name:"王晓静",
//     drive:function () {
//         setTimeout(function () {
//             console.log("3我是"+this.name+",哈哈");
//
//         }.bind(this),2000)
//     }
// }
// laosiji3.drive()
//
// var laosiji2={
//     name:"王晓静",
//     drive:function () {
//         var that =this
//         setTimeout(function () {
//             console.log("2我是"+that.name+",哈哈");
//
//         },2000)
//     }
// }
// laosiji2.drive()

var obj={
    name:"changfeng"
}
function test() {
    console.log(this)
}
test1=test.bind(obj)
test1()