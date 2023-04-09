const a = 'a'.charCodeAt(0)

const mergeColorCountLists = (arr1, arr2) => {
    // create new array taking the max value of each color from each input array
    const mergedList = []
    for (let i=0; i < arr1.length; i++)
        mergedList.push( Math.max(arr1[i], arr2[i]) )
    return mergedList
}

const getMaxColor = (colorCount) => {
    // obtain max color count from each node after BFS
    let max = 0
    for (let colorArray of colorCount)
        max = Math.max(max, Math.max(...colorArray))
    return max
}

const largestPathValue = (colors, edges) => {
    if (!edges.length) return 1
    
    const N = colors.length,
          graph = {},
          inCount = new Array(N).fill(0),
          stack = new Array()
    
    for (let [u, v] of edges) {
        graph[u] ? graph[u].push(v) : graph[u] = [v]
        inCount[v] ? inCount[v]++ : inCount[v] = 1
    }

    // begin BFS with nodes that do not have a parent
    for (let u of Object.keys(graph)) {
        if (!inCount[u]) stack.push(u)
    }
    
    // keep track of how many colors have been seen
    const colorCount = Array.from({ length: N }, () => Array(26).fill(0))
    
    while (stack.length) {
        let node = stack.pop()
        colorCount[node][colors[node].charCodeAt(0) - a]++
        if (!graph[node]) continue
        for (let nei of graph[node]) {
            // merge parent/child colorCount lists into one list of max colorCounts each node has seen
            colorCount[nei] = mergeColorCountLists(colorCount[node], colorCount[nei])
            inCount[nei]--
            if (!inCount[nei])
                stack.push(nei)
        }
    }
    
    return inCount.every(cnt => cnt === 0) ? getMaxColor(colorCount) : -1
}
