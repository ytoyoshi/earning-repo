// DOM
const seisanClone = document.getElementById("seisanClone");
const seisanRemove = document.getElementById("seisanRemove");

// 精算金追加ボタン押下時の処理
function addSeisanKin() {
    const divId = document.getElementById("seisanKin");
    addInput(divId);

    // 削除ボタンの表示制御
    // inputとbrタグが初期表示で存在するので・・・・
    if (divId.childElementCount >= 3) {
        seisanRemove.style.display = "";
    } else {
        seisanRemove.style.display = "none";
    }
}

// 入力欄の追加処理
function addInput(divId) {
    const newSeisankin = document.createElement("input");

    const id = divId.id;
    let seisanKinId = divId.childElementCount;

    if (seisanKinId = 0) {
        console.log(seisanKinId);
        seisanKinId = 1;
    } 

    newSeisankin.setAttribute("id", id + seisanKinId);
    newSeisankin.setAttribute("type", "text");
    newSeisankin.setAttribute("size", "10");
    divId.appendChild(newSeisankin);
    divId.appendChild(document.createElement("br"));
}


// イベント
window.addEventListener("load", addSeisanKin);
seisanClone.addEventListener("click", addSeisanKin);


