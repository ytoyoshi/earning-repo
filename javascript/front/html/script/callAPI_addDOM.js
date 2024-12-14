// DOM
const addButton = document.getElementById("addButton");
const lists = document.getElementById("lists");

async function  getUserName(){
    const res = await fetch("https://jsonplaceholder.typicode.com/users");
    const userName = await res.json();
    return userName;
}

async function listUsers(){
    const userName = await getUserName();
    userName.forEach(addList);
}

function addList(userName){
    const list = document.createElement("li");
    list.innerText = userName.name;
    lists.appendChild(list);
}

// イベント
window.addEventListener("load",listUsers);
addButton.addEventListener("click",listUsers);
