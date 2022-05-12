function solution(nums) {
    let canCatch = nums.length/2
    let checkList = [];

    nums.forEach(monster=>{
        if(!checkList.includes(monster) && canCatch>=1){
            checkList.push(monster)
            canCatch-=1
        }
    })

    return checkList.length;
}

// 오늘 코딩 테스트.. 시험 보고.. 충격 받아서 다시 시작합니다.. ㅠㅜㅠㅜ