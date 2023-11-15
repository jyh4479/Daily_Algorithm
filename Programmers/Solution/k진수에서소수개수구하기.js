const isPrime = (num) => {
	if(num === 1 || num === 0) return false; 

 	for(let i = 2; i <= parseInt(Math.sqrt(num)); i++) {
  		if(num % i === 0) return false;
	} 
    return true; 
}


const getKNumber = (n, k) => {
    const result = [];
    
    while(n>0){
        result.push(n%k);
        n=parseInt(n/k);
    }

    result.reverse();
    
    return result.join("");
}

function solution(n, k) {
    
    const kNumber = getKNumber(n, k);
    
    const numberList = kNumber.split('0');
    
    const ansList = numberList.filter(number=>isPrime(Number(number)));
    
    return ansList.length;
}
