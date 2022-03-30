// function suma(a) {
//     return function (b) {
//         if (b) {
//             return suma(a + b)
//         }
//         return a
//     }
// }

// sums = (a) => (b) => b ? sums(a + b) : a

// // console.log(suma(5)(4)(3)(2)(1)())
// // console.log(sums(5)(4)(3)(2)(1)())
// // console.log("test", sums(5)(4)(3)(2)(1))

// // for (let i = 1; i < 6; i++) {
// //     setTimeout(() => {
// //         console.log(i)
// //     }, i * 1000)
// // }

// const arr = [
//     {
//         'title': "HEY",
//         "val": 45
//     },
//     {
//         'title': "A",
//         "val": 46
//     },
//     {
//         'title': "V",
//         "val": 47
//     },
//     {
//         'title': "D",
//         "val": 48
//     },
//     {
//         'title': "E",
//         "val": 43
//     }
// ]

// Array.prototype.customMap = function (callback) {
//     var tmp = []
//     for (var i = 0; i < this.length; i++) {
//         tmp.push(callback(this[i], i, this))
//     }
//     return tmp
// }

// // console.log("HEY", arr.map((v) => v.val - 40))
// // console.log("HEY", arr.customMap((v) => v.val - 40))

// let printTitle = function (...args) {
//     console.log('a', args)
//     this.forEach(element => {
//         console.log(element.title, args[0], args[1])
//     });
// }

// let test = printTitle.bind(arr, ["s", "b"])
// test("c")

let getData = () => {
    console.log("Getting data")
}

let debounce = (fn, delay) => {
    let timer;
    return function () {
        var obj = this;
        args = arguments
        clearTimeout(timer)
        timer = setTimeout(() => {
            fn.apply(obj, args)
        }, delay)
    }
}

let throttle = (fn, delay) => {
    let flag = true;
    return function () {
        if (flag) {
            var obj = this;
            args = arguments
            flag = false;
            fn.apply(obj, args)
            setTimeout(() => {
                flag = true;
            }, delay)
        }
    }
}

const test = {
    a: 10,
    b: 5
}

function print(a, b) {
    console.log(`${this.a}+${this.b} | ${a}-${b}`)
}

Function.prototype.myBind = function (scope, ...args) {
    scope._this = this
    return function () {
        return scope._this(...args)
    }
}

Function.prototype.myCall = function (scope, ...args) {
    scope._this = this;
    return scope._this(...args)
}

Function.prototype.myApply = function (scope, args) {
    scope._this = this;
    return scope._this(...args)
}

const betterFunction = debounce(getData, 300)

const betterClick = throttle(getData, 500)

