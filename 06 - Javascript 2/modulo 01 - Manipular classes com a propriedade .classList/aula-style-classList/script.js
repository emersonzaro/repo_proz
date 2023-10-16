let titulo = document.querySelector("h2")
console.log(titulo)

titulo.style.color = "blue"
titulo.style.fontSize = "12rem"

// Primeira interação com o usuário

let loginUsuario = document.getElementById("login-usuario")
let errorTextUsuario = document.querySelector(".error-text")

loginUsuario.classList.add("error")
errorTextUsuario.classList.add("visible")

