const checkSkillTree = (skill, skillTree) => {
    const skillObject = {};

    for (let i = 0; i < skill.length; i++) {
        skillObject[skill[i]] = true;
    }

    const skillTreeList = [];

    for (let i = 0; i < skillTree.length; i++) {
        if (skillObject[skillTree[i]] !== undefined) skillTreeList.push(skillTree[i]);
    }

    const mySkill = skillTreeList.join("");

    for (let i = 0; i < mySkill.length; i++) {
        if (skill[i] !== mySkill[i]) return false;
    }

    return true;
}

function solution(skill, skill_trees) {
    let ans = 0;

    skill_trees.forEach(skillTree => {
        if (checkSkillTree(skill, skillTree)) ans++;
    })

    return ans;
}
