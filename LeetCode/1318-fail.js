// function makeConnected(n, connections) {
//     if (connections.length < n - 1) return -1;
//     const graph = makeGraph(connections);
//     const visited = new Set();
//     let components = 0;
//     for (let i = 0; i < n ; i++) {
//         components += dfs(graph, i, visited);
//     }
//     return components - 1
// }

// function dfs(graph, nodeIndex, visited) {
//     if(visited.has(nodeIndex)) return 0;
//     visited.add(nodeIndex);
//     const adj = graph[nodeIndex.toString()];
//     for (let i = 0; i < adj?.length; i++) {
//         dfs(graph, adj[i], visited);
//     }
//     return 1;
// }

// function makeGraph (connections) {
//     const graph = {}
//     for (let i = 0; i< connections.length; i++) {
//         const [key, value] = connections[i];
//         if(!(key in graph)) graph[key] = [];
//         if(!(value in graph)) graph[value] = []
//         graph[key].push(value);
//         graph[value].push(key);
//     }
//     return graph;
// }

var makeConnected = function(n, connections) {  // n nodes, 0 to n-1
  let parents = [...Array(n).keys()];           // initially all nodes point to self, ie [0, 1, 2, ...]
  let connected = n;                            // initially all nodes are unconnected
  let redundant = 0;

  function find(id) {
    if(parents[id] !== id) 
      parents[id] = find(parents[id]); // compress 
    return parents[id];
  }
  
  function union(a, b) {
    let [rootA, rootB] = [find(a), find(b)];
    if(rootA !== rootB) {
      parents[rootB] = rootA;
      connected--;
    } else { // already connected, ie redundant
      redundant++;
    }
  }
    
  connections.forEach(con => union(...con));
  return (redundant >= connected - 1) ? connected - 1 : -1;
}
