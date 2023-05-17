//Fare un bot che giochi a tris
///////////////////SELETTORI/////////////////
const p_table = [];
const divTable = document.querySelector(".tristable");
p_table[0] = document.querySelector(".NO");
p_table[1] = document.querySelector(".N");
p_table[2] = document.querySelector(".NE");
p_table[3] = document.querySelector(".O");
p_table[4] = document.querySelector(".C");
p_table[5] = document.querySelector(".E");
p_table[6] = document.querySelector(".SO");
p_table[7] = document.querySelector(".S");
p_table[8] = document.querySelector(".SE");

const room_code = document.getElementById("codiceStanza").textContent;
const username = document.getElementById("username").textContent;
const avatar = document.getElementById("avatar").textContent;
const p_par = document.querySelector(".p_message");
const p_span = document.getElementById("turn");

///////////////////VARIABILI//////////////////
const tris = ["", "", "", "", "", "", "", "", ""];
let turn = ""; // può essere host=X o guest=O
let opponent = "";
let end = false;

//assegnazione del simbolo all'opponent
if (avatar == "X") {
  opponent = "O";
} else if (avatar == "O") {
  opponent = "X";
} //terzo caso avatar="" per gli spettatori

async function buildTable() {
  let table = await getMove(room_code);
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
  checkWin();
}
function printTable() {
  for (let i = 0; i < p_table.length; i++) {
    p_table[i].textContent = tris[i];
  }

  for (let i = 0; i < p_table.length; i++) {
    if (p_table[i].textContent == avatar) {
      p_table[i].style.color = "blue";
    }
  }

  for (let i = 0; i < p_table.length; i++) {
    if (p_table[i].textContent == opponent) {
      p_table[i].style.color = "red";
    }
  }

  p_span.textContent = turn;
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
  if (event.target.textContent === "" && turn == avatar && !end) {
    event.target.textContent = avatar;
    event.target.style.color = "blue";
    id = event.target.id;
    tris[id] = avatar;
    //ricontrollare gameTris
    console.log(tris);
    postMove(tris, room_code, username);
    changeTurn();
    buildTable();
  }
};

///////////////////API//////////////////////

async function postMove(mossa, codiceStanza, username) {
  const url = `/mossa/${codiceStanza}/${username}`;
  console.log(mossa);
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
var intervalId = window.setInterval(function () {
  buildTable();
}, 2000); //5000=5 sec 2000=2sec

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
*/
function checkWin() {
  let char = avatar;
  let message = "Vittoria";

  for (let idx = 0; idx <= 6; idx += 3) {
    //casi vittoria orizontali
    if (tris[idx] == char && tris[idx + 1] == char && tris[idx + 2] == char) {
      end = true;
      message = "Vittoria";
    }
  }
  for (let idx = 0; idx <= 2; idx += 1) {
    //casi vittoria verticali
    if (tris[idx] == char && tris[idx + 3] == char && tris[idx + 6] == char) {
      end = true;
      message = "Vittoria";
    }
  }
  //casi vittoria in obliquo
  if (tris[0] == char && tris[4] == char && tris[8] == char) {
    end = true;
  } else if (tris[2] == char && tris[4] == char && tris[6] == char) {
    end = true;
    message = "Vittoria";
  }

  char = opponent;
  for (let idx = 0; idx <= 6; idx += 3) {
    //casi vittoria orizontali
    if (tris[idx] == char && tris[idx + 1] == char && tris[idx + 2] == char) {
      end = true;
      message = "Sconfitta";
    }
  }
  for (let idx = 0; idx <= 2; idx += 1) {
    //casi vittoria verticali
    if (tris[idx] == char && tris[idx + 3] == char && tris[idx + 6] == char) {
      end = true;
      message = "Sconfitta";
    }
  }
  //casi vittoria in obliquo
  if (tris[0] == char && tris[4] == char && tris[8] == char) {
    end = true;
  } else if (tris[2] == char && tris[4] == char && tris[6] == char) {
    end = true;
    message = "Sconfitta";
  }
  if (end) {
    p_par.textContent = message;
    clearInterval(intervalId);
  }
}

/*
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
