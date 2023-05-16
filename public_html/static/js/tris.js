//Fare un bot che giochi a tris
///////////////////SELETTORI/////////////////
p_table = [];
table = document.querySelector(".tristable");
p_table[0] = document.querySelector(".NO");
p_table[1] = document.querySelector(".N");
p_table[2] = document.querySelector(".NE");
p_table[3] = document.querySelector(".O");
p_table[4] = document.querySelector(".C");
p_table[5] = document.querySelector(".E");
p_table[6] = document.querySelector(".SO");
p_table[7] = document.querySelector(".S");
p_table[8] = document.querySelector(".SE");

room_code = document.getElementById("codiceStanza").textContent;
username = document.getElementById("username").textContent;
avatar = document.getElementById("avatar").textContent;
p_par = document.querySelector(".p_message");

console.log({ p_table });
console.log({ room_code });
///////////////////VARIABILI//////////////////
const tris = ["", "", "", "", "", "", "", "", ""];
let turn = ""; // può essere host=X o guest=O

async function buildTable() {
  table = await getMove(room_code);
  tris[0] = table["NO"];
  tris[1] = table["N"];
  tris[2] = table["NE"];
  tris[3] = table["O"];
  tris[4] = table["C"];
  tris[5] = table["E"];
  tris[6] = table["SO"];
  tris[7] = table["S"];
  tris[8] = table["SE"];

  turn = table["turn"];
  printTable();
}
function printTable() {
  p_table[0].textContent = tris[0];
  p_table[1].textContent = tris[1];
  p_table[2].textContent = tris[2];
  p_table[3].textContent = tris[3];
  p_table[4].textContent = tris[4];
  p_table[5].textContent = tris[5];
  p_table[6].textContent = tris[6];
  p_table[7].textContent = tris[7];
  p_table[8].textContent = tris[8];

  for (let i = 0; i < p_table.length; i++) {
    if (p_table[i].textContent != avatar) {
      p_table[i].style.color = "red";
    }
  }
}
function changeTurn() {
  console.log("turno:", turn);
  if (turn == "X") {
    turn = "O";
  } else if (turn == "O") {
    turn = "X";
  }
}

const gameTris = (event) => {
  //TODO:
  //DA MODIFICARE: in modo che una vola che l'utente immette un input controlla che sia il suo turno
  //e poi invii l'oggetto tris all' api
  console.log(avatar);
  if (event.target.textContent === "" && turn == avatar) {
    event.target.textContent = avatar;
    event.target.style.color = "blue";
    id = event.target.id;
    tris[id] = avatar;
    //TODO: ricontrollare parametri postMOve
    //ricontrollare gameTris
    postMove(tris, room_code, username);
    changeTurn();
    buildTable();
  }
};

///////////////////API//////////////////////

async function postMove(mossa, codiceStanza, username) {
  const url = `/mossa/${codiceStanza}/${username}`;
  const response = await fetch(url, {
    method: "POST",
    body: JSON.stringify(mossa),
    headers: { "Content-Type": "application/json" },
  });
  return response;
}

async function getMove(codiceStanza) {
  const url = `/tris/${codiceStanza}`;
  try {
    const response = await fetch(url);
    const data = await response.json();
    return data;
  } catch (error) {
    console.log(data);
  }
}

///////////////////MAIN//////////////////////
buildTable();

///////////////////eventlistener/////////////
document.addEventListener("click", gameTris);

// codice vecchio
/*
const charPlayer = "O";
const charBot = "X";
///////////////////FUNZIONI//////////////////
function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min); // The maximum is exclusive and the minimum is inclusive
}
//bot random
function botRandom() {
  marked = true;

  if (tris.find((el) => el === "") === "") marked = false; //controllo se la tabella ha uno spazio vuoto, se si find restituisce "", e lo confronta nel if
  console.log(marked);
  while (!marked) {
    choise = getRandomInt(0, 9);
    console.log(choise);
    if (tris[choise] === "") {
      p_table[choise].textContent = charBot;
      p_table[choise].style.color = "red";
      tris[choise] = charBot;
      marked = true;
    }
  }
}
function checkWin() {
  let char = charPlayer;
  let message = "Vittoria";
  for (let idx = 0; idx <= 6; idx += 3) {
    //casi vittoria orizontali
    if (tris[idx] == char && tris[idx + 1] == char && tris[idx + 2] == char) {
      p_par.textContent = message;
    }
  }
  for (let idx = 0; idx <= 2; idx += 1) {
    //casi vittoria verticali
    if (tris[idx] == char && tris[idx + 3] == char && tris[idx + 6] == char) {
      p_par.textContent = message;
    }
  }
  //casi vittoria in obliquo
  if (tris[0] == char && tris[4] == char && tris[8] == char) {
    p_par.textContent = message;
  } else if (tris[2] == char && tris[4] == char && tris[6] == char) {
    p_par.textContent = message;
  }

  char = charBot;
  message = "Sconfitta";
  for (let idx = 0; idx <= 6; idx += 3) {
    //casi vittoria orizontali
    if (tris[idx] == char && tris[idx + 1] == char && tris[idx + 2] == char) {
      p_par.textContent = message;
    }
  }
  for (let idx = 0; idx <= 2; idx += 1) {
    //casi vittoria verticali
    if (tris[idx] == char && tris[idx + 3] == char && tris[idx + 6] == char) {
      p_par.textContent = message;
    }
  }
  //casi vittoria in obliquo
  if (tris[0] == char && tris[4] == char && tris[8] == char) {
    p_par.textContent = message;
  } else if (tris[2] == char && tris[4] == char && tris[6] == char) {
    p_par.textContent = message;
  }
}



const gameTris = (event) => {
  //TODO:
  //DA MODIFICARE: in modo che una vola che l'utente immette un input controlla che sia il suo turno
  //e poi invii l'oggetto tris all' api

  if (event.target.textContent === "") {
    event.target.textContent = charPlayer;
    event.target.style.color = "blue";
    id = event.target.id;
    tris[id] = charPlayer;
    buildTable();
    //botRandom();
    checkWin();
  }
};
*/
