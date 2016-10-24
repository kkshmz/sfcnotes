// 1. Populate an array with the numbers 1 through 100.
// 2. Shuffle it.
// 3. Take the first 8 elements of the resulting array.
var arr = []
while(arr.length < 8){
  var randomnumber=Math.ceil(Math.random()*100)
//The indexOf() method returns the position of the first occurrence of a specified value in a string.
// returns -1 when, if the search for the value never occurs
  if(arr.indexOf(randomnumber) === -1){
// The push() method adds new items to the end of an array, and returns the new length.
    arr.push(randomnumber)
  }
}
console.log(arr);
arr.sort();
console.log(arr);
