// JavaScript source code





//   BRUTE FORCE
/*
 * codesandbox
import "./styles.css";

function logit(arg, results) {
    document.querySelector('#app').innerHTML = `
  <h2>args = ${arguments[0]} </h2>
  <h2>results= ${results}
  `
}

*/

// O(n)
// Space - makes two objects to compare the strings
function isPermutation(str1, str2) {
    const str1OBJ = {}
    const strOBJ2 = {}
    let size1 = str1.length
    let size2 = str2.length
    if (size1 !== size2) {
        return false
    }
    else {
        let i = 0
        let j = 0
        for (i, j; i < size1, j < size2; i++, j++) {
            const letter = str1.charAt(i)
            const letter2 = str2.charAt(j)
            if (str1OBJ.hasOwnProperty(letter)) {
                str1OBJ[letter] += 1
            }
            else {
                str1OBJ[letter] = 1
            }
            if (strOBJ2.hasOwnProperty(letter2)) {
                strOBJ2[letter2] += 1
            }
            else {
                strOBJ2[letter2] = 1
            }
        } // end for (i, j)

        for (const [key, value] of Object.entries(str1OBJ)) {
            if (strOBJ2.hasOwnProperty(key)) {
                if (strOBJ2[key] == value) {
                    //pass
                }
                else {
                    return false
                }
            }
            else {
                return false
            }
        };
        return true;
    }



}

let first = 'upperpenninsula'
let second = 'penninsulaupper'
/* codesandbox 
logit([first, second], isPermutation(first, second))
*/
function test1() {
    // change the first/second to see the true change to false when it's not a permutation
    let x = isPermutation(first, second)
    console.log(x)
}

//test1()

// Sort and Compare

function isPermutation2(str1, str2) {
    if (str1.length != str1.length) {
        return false
    }
    let str1list = str1.split('')
    let str2list = str2.split('')
    str1list.sort() 
    str2list.sort() 
    // can not use operator to compare two arrays, they are different objects
    str1A = str1list.join()
    str2A = str2list.join()
    console.log(str1A, str2A)
    return str1A === str2A
}

function test2() {
    let result = isPermutation2(first, second)
    console.log('test 2:  result=')
    console.log(result)
}
//test2()

// creat modify ONE object O(n)

function isPermutation3(str1, str2) {
    if (str1.length != str2.length) {
        return false
    }
    let charOBJ = {}
    let size = str1.length
    for (let i = 0; i < size; i++) {
        let letter = str1.charAt(i)
        if (charOBJ.hasOwnProperty(letter)) {
            charOBJ[letter] += 1
        }
        else {
            charOBJ[letter] = 1 
        }
    }
    for (let j = 0; j < size; j++) {
        let letter2 = str2.charAt(j)
        if (charOBJ.hasOwnProperty(letter2)) {
            charOBJ[letter2] -= 1
        }
        else {
            return false
        }
    }

    //check if all key values are 0
    for (item in charOBJ) {
        let value = charOBJ[item]
        if (value != 0) {
            return false
        }
    };
    return true
}


function test3() {
    let result = isPermutation3(first, second)
    console.log('test 3 (true):  result=')
    console.log(result)
    falsefirst = "upperpe8ninsula"
    let result2 = isPermutation3(falsefirst, second)
    console.log('test 3 (false): ', result2)
}

test3()
