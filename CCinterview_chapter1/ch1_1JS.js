// Chapter 1 problem 1 ,  JavaScript

/**
 * Strings are immutable.  You can not change a string 'in-place', or 'reverse', or modify it without returning a new string.
 */

function logit(arg, logdata) {
    document.getElementById("app").innerHTML = `
<h1>log</h1>
<div>
  <h2 id="results"> arg= ${arg}, logdata= ${logdata} </h2>
</div>
`;
}

// Solution A

function unique(str) {
    let size = str.length;
    let checker = ''

    for (let i = 0; i < size; i++) {
        let letter = str.charAt(i)
        if (checker.includes(letter)) {
            return false
        }
        else {
            checker += letter
        }
    } // end for i
    return true


}

// Solution B

function Unique2(str) {
    let size = str.length
    let end = str.length - 1
    for (let i = 0; i < size; i++) {
        let letter1 = str.charAt(i)
        for (let j = end; j >= 0; j--) {
            let letter2 = str.charAt(j)
            if (i != j && letter1 === letter2) {
                return false
            }
        } //end for j
    } //end for i
    return true

}


let notUnique = "asdfjkl;uu57462819"
let isUnique = "87654ertyu$%^&AaBbCc"
//logit(notUnique, unique(notUnique))
//let result = Unique2(notUnique)
let result2 = Unique2(isUnique)
console.log(result2)