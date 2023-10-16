let quantidadeSubtotal = document.getElementById("quantidade-subtotal");
let valorSubtotal = document.getElementById("valor-subtotal");

let subtotalInfo = {
  quantidade: 1,
  valor: 11.66,
};

// Atualizar DOM
function atualizarDOM(){
  quantidadeSubtotal.innerText = subtotalInfo.quantidade + " itens";
  valorSubtotal.innerText = subtotalInfo.valor.toFixed(2);  
}

atualizarDOM()

// Capturar elementos para aumentar a quantidade + 1
let btnAdicionarUm = document.getElementById ('btn-adicionar-produto-01');
let quantidadeProduto01 = document.getElementById ('quantidade-produto-01');

let valorProduto01 = 11.66

//Função
function adicionarUm(){
  // Incrementa o valor do produto
  quantidadeProduto01.value = Number(quantidadeProduto01.value) + 1;

  // Incrementa a qtde do subtotal
  subtotalInfo.quantidade = subtotalInfo.quantidade + 1;

  // Atualizar o valor do subtotal
  subtotalInfo.valor = subtotalInfo.valor + valorProduto01

  // Atualizar o DOM
  atualizarDOM()
}

// Eventos
btnAdicionarUm.addEventListener("click", adicionarUm)




