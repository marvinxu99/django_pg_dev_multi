/* 
https://stackoverflow.com/questions/2901102/how-to-print-a-number-with-commas-as-thousands-separators-in-javascript
*/

// 1.  - does not work if decimal points > 2
function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

// 2. 
function numberWithCommas(x) {
    var parts = x.toString().split(".");
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    return parts.join(".");
}

// 3.
//JavaScript has lookbehind (support info), it can be solved in the regular expression itself:
function numberWithCommas(x) {
    return x.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",");
}

// 4. Using to local string - may be better.
var n = 34523453.345
n.toLocaleString()   // ==> "34,523,453.345"


