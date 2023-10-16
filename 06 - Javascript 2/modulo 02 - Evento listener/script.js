/* let numero = document.querySelector("h1")
let botao = document.querySelector("button")
let contagem = 0

function adicionarUm() {
    contagem = contagem + 1
    numero.innerText = contagem
}

botao.addEventListener("click", adicionarUm)


botao.addEventListener("click", function(){
    contagem = contagem + 1;  
    numero.innerText = contagem;  
});
*/


/* -----evento mouse ----*/

let button = document.querySelector("button");
let span = document.querySelector("span");
let section = document.querySelector("section");

function mostrarSpan(){
    span.style.opacity = "100"
}

button.addEventListener("mouseover", mostrarSpan);

function ocultarSpan(){
    span.style.opacity = "0"
}

button.addEventListener("mouseout", ocultarSpan);

function fazerUmClick(){
    section.innerText = "Fez um click simples!"
}

button.addEventListener("click", fazerUmClick);