const graph = {
    A: ["B", "C"],
    B: ["A", "D"],
    C: ["A", "G", "H", "I"],
    D: ["B", "E", "F"],
    E: ["D"],
    F: ["D"],
    G: ["C"],
    H: ["C"],
    I: ["C", "J"],
    J: ["I"]
};

// stack을 이용한 dfs
const dfs = (start) => {
    const visited = [];
    let needVisit = [];

    needVisit.push(start);

    while (needVisit.length > 0) {
        const node = needVisit.shift();

        if (!visited.includes(node)) {
            visited.push(node);
            needVisit = [...graph[node], ...needVisit];
        }
    }

    return visited;
}

console.log(dfs("A"));