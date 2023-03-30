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

p_par = document.querySelector("p");

console.log({ p_table });
///////////////////VARIABILI//////////////////
const tris = ["", "", "", "", "", "", "", "", ""];
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
  if (event.target.textContent === "") {
    event.target.textContent = charPlayer;
    event.target.style.color = "blue";
    id = event.target.id;
    tris[id] = charPlayer;
    botRandom();
    checkWin();
  }
};
///////////////////MAIN//////////////////////

///////////////////eventlistener/////////////
document.addEventListener("click", gameTris);
