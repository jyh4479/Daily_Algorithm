/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
    const pathList = path.split('/').filter(p=>p!=='');

    const ansList = [];

    pathList.forEach(path=>{
        if(path==="..") ansList.pop();
        else if(path==='.') return;
        else ansList.push(path);
    })

    let ans="";

    ansList.forEach(path=>{
        ans+=`/${path}`;
    })

    return ansList.length===0 ? '/' : ans;
};
