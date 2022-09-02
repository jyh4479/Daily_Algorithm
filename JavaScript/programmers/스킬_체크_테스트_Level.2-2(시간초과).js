function check(i, j, board, size) {
    const move = size - 1;

    // 범위에 벗어나는 경우
    if (i + move >= board.length || j + move >= board[0].length) return 0;

    // 범위에 사각형이 들어오는 경우
    else {
        for (let a = i; a <= i + move; a++) {
            for (let b = j; b <= j + move; b++) {
                if (board[a][b] === 0) return 0;
            }
        }
    }

    return size * size;
}

function solution(board) {
    let answer = 0;

    const checkSize = Math.max(board.length, board[0].length);

    for (let size = 1; size <= checkSize; size++) {
        for (let i = 0; i < board.length; i++) {
            for (let j = 0; j < board[0].length; j++) {
                answer = Math.max(answer, check(i, j, board, size));
            }
        }
    }

    return answer;
}