function variavel1() {
    const val =10;
    if (val == 10) {
        alert("variável é igual a 10");
    }
}

function variavel2() {
    const val = "Pedro Henrique";
    if (val == "Pedro Henrique") {
        alert("variável é igual a Pedro Henrique");
    }
}

function variavel3() {
    const val = document.getElementById("ok").value;
    if (val == "ok") {
        alert("você digitou ok");
    }
}

function variavel4() {
    const val = document.getElementById("5").value;
    if (val == "5") {
        alert ("o valor é igual a 5");
    }
}

function variavel5() {
    const val = document.getElementById("admin").value;
    const correto = document.getElementById("Correto");
    if (val == "admin") {
        correto.textContent = "Correto";
    }
}

function variavel6() {
    const val = document.getElementById("teste").value;
    const textoTeste = document.getElementById("TextoTeste");
    if (val == "teste") {
        textoTeste.textContent = "você digitou teste";
    }
}

function variavel7() {
    const val = document.getElementById("cor").value;
    const div1 = document.getElementById("div1");
    if (val == "azul"){
        div1.style.color = "blue";
    }
}

function variavel8() {
    const val = document.getElementById("verificar").value;
    if (val > 10) {
        alert("o valor é maior que 10");
    }
}

function variavel9() {
    const val = document.getElementById("verificar2").value;
    if (val < 50) {
        alert("o valor é menor que 50");
    }
}

function variavel10() {
    const val = document.getElementById("senha").value;
    const textosenha = document.getElementById("textosenha");
    if (val == "senha") {
        textosenha.textContent = "você digitou senha";
    }
}

function variavel11() {
    const val = document.getElementById("corpagina").value;
    const body = document.getElementById("body");
    if (val == "escuro") {
        body.style.backgroundColor = "black";
    }
}

function variavel12() {
    const val = document.getElementById("textocor").value;
    const textocor = document.getElementById("txt");
    if (val == "mudar") {
        textocor.textContent = "você mudou o texto e a cor";
        textocor.style.color = "red";
    }
}

function variavel13() {
    const val = document.getElementById("elementos").value;
    const elementos = document.getElementById("elemetos");
    const body = document.getElementById("p");
    if (val == "mudar") {
        elementos.textContent = "você mudou o texto e a cor";
        elementos.style.color = "blue";
        p.style.color = "red";
    }
}

function variavel14() {
    const val = document.getElementById("tamanhotexto").value;
    const tamanho = document.getElementById("tamanho");
    if (val >20) {
        tamanho.style.fontSize = "50px"; 
    }
}

function variavel15() {
    const val = document.getElementById("bemvindo").value;
    const mensagem = document.getElementById("mensagem");
    if (val == "admin") {
        mensagem.textContent = "Bem-vindo, Pedro Henrique!";
    }
}

function variavel16() {
    const val = document.getElementById("mudarcort").value;
    const txtmudarcort = document.getElementById("txtmudarcort");
    if (val == "19") {
        txtmudarcort.textContent = "você mudou o texto, a cor e o tamanho";
        txtmudarcort.style.color = "red";
        txtmudarcort.style.fontSize = "40px";
     }
 }


function variavel17() {
    const val = document.getElementById("condição2").value;
    const condição1 = document.getElementById("condição1");
    if (val == "22") {
        condição1.textContent = "você digitou 22";
        condição1.style.color = "blue";
        condição1.style.fontSize = "30px";
    }
}

function variavel18() {
    const val = document.getElementById("nmr100").value;
    const condição3 = document.getElementById("100");
    if (val > 100) {
        body.style.backgroundColor = "cyan";
    }
}

function variavel19() {
    const val = document.getElementById("copiar").value;
    const copia = document.getElementById("copia");
    if (val == "copiar") {
        copia.textContent = "O melhor gestor é o raphael";
    }
}

function variavel20() {
    const val = document.getElementById("divis").value;
    const div2 = document.getElementById("div2");
    const div3 = document.getElementById("div3");
    if (val == "mudar") {
        div2.textContent = "você mudou as duas divis";
        div3.textContent = "você mudou as duas divis";
        div2.style.color = "red";
        div3.style.color = "cyan";
        div2.style.fontSize = "40px";
        div3.style.fontSize = "40px";
    }
}

function variavel21() {
    const val = document.getElementById("multiplo2").value;
    const multiplo1 = document.getElementById("multiplo1");
    if (val == "7") {
        multiplo1.textContent = "você digitou 7";
        body.style.backgroundColor = "cyan";
        multiplo1.style.fontSize = "50px";
    }
}