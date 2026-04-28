function mostrarNome() {
    alert("Olá, mundo!");
    let Nome = "Pedro Henrique";
    alert(Nome);
}

function mostrarIdade() {
    let Idade = 17;
    let numero = 5;
    Idade = 15 + numero;
    alert(Idade);
}

function mudarTexto() {
    let textinho = document.getElementById("textinho");
    textinho.textContent= "clique em mudar cor";
}

function div1() {
    let div1 = document.getElementById("div1");
    div1.style.backgroundColor = "red";
}

function clicou() {
    let mensagem = document.getElementById("mensagem");
    mensagem.textContent= "Você clicou!";
}

function funcao() {
    let paragrafo = document.getElementById("paragrafo");
    let caixaa = document.getElementById("caixaa");
    let escrita = paragrafo.textContent;
    caixaa.value = escrita;
}

function soma() {
    let num1 = Number(document.getElementById("num1").value);
    let num2 = Number(document.getElementById("num2").value);
    let resultado = num1 + num2;
    let local = document.getElementById("resultado");
    local.textContent = resultado;
}

function mudarCor() {
    let body = document.getElementById("body");
    body.style.backgroundColor = "aqua";
}

function mudarTamanho() {
    let textoo = document.getElementById("textoo");
    textoo.style.fontSize = "30px";
}

function mudarCorTexto() {
    let textoo = document.getElementById("textoo");
    textoo.style.color = "red";
}

function mudar2() {
    let textoo = document.getElementById("textoo");
    textoo.style.fontSize = "50px";
    textoo.style.color = "blue";
}

function mudar3() {
    let textoo = document.getElementById("textoo");
    textoo.style.fontSize = "70px";
    textoo.style.color = "white";
    let body = document.getElementById("body");
    body.style.backgroundColor = "blue";
}

function mudar4() {
    let textoo = document.getElementById("texto difícil");
    textoo.style.fontSize = "30px";
    textoo.style.color = "red";
    textoo.textContent = "Este Texto ficou fácil";
}

function valor1() {
    let valor1 = Number(document.getElementById("valor1").value);
    let valor2 = Number(document.getElementById("valor2").value);
    let resultado1 = valor1 + valor2;
    let local = document.getElementById("resultado1");
    let resultado2 = valor1 + valor2;
    let local2 = document.getElementById("resultado 2");
    local2.textContent = resultado2;
    local.textContent = resultado1;
}

function mudarTamanho2() {
    let textop3 = document.getElementById("textop3");
    textop3.style.fontSize = "30px";
}

function mudarCorTexto2() {
    let textop3 = document.getElementById("textop3");
    textop3.style.color = "red";
}

function mudar3() {
    let textop3 = document.getElementById("textop3");
    textop3.style.fontSize = "15px";
    textop3.style.color = "blue";
}

function raphael() {
    let div1 = document.getElementById("div1");
    div1.style.backgroundColor = "red";
    let div2 = document.getElementById("div2");
    div2.style.fontSize = "30px";
}

function copiar() {
    let copiar = document.getElementById("valor3");
    const sixseven = document.getElementById("sixseven");
    sixseven.value = copiar.value;
    sixseven.textContent = copiar.value;
    textop3.value = copiar.value;
    textop3.textContent = copiar.value;
}

function valor2() {
    let valor4 = Number(document.getElementById("valor4").value);
    let valor5 = Number(document.getElementById("valor5").value);
    let resultado3 = valor4 + valor5;
    let local = document.getElementById("resultado3");
    local.textContent = resultado3;
}

function limpar() {
    let valor4 = document.getElementById("valor4");
    let valor5 = document.getElementById("valor5");
    let resultado3 = document.getElementById("resultado3");
    valor4.value = "";
    valor5.value = "";
    resultado3.textContent = "";
}

function mudargeral() {
    let textop3 = document.getElementById("textop3");
    textop3.style.fontSize = "20px";
    textop3.style.color = "red";
    let body = document.getElementById("body");
    body.style.backgroundColor = "aqua";
    let Idade = 17;
    let numero = 5;
    Idade = 15 + numero;
    alert(Idade);
    textoo.style.fontSize = "70px";
}