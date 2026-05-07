function verificaridade() {
    let idade = document.getElementById("idade").value
    if (idade >0 && idade <12) {
        alert("Criança")
    }
    else if (idade >= 12 && idade <= 17) {
        alert("Adolescente")
    }
    else if (idade >=18 && idade <60) {
        alert("Adulto")
    }
    else if (idade >=60) {
        alert("Idoso")
    }
    else {
        alert("Erro: Idade inválida")
    }
}

function login() {
    let usuario = document.getElementById("usuario").value;
    let senha = document.getElementById("senha").value;
    let incorreto = document.getElementById("incorreto");
    if (usuario == "admin" && senha == "1234"){
        alert("Login realizado com sucesso!")
    }
    else if (usuario == "professor" && senha == "senac") {
        alert("Bem-vindo, professor!")
    }
    else if ((!usuario && !senha) || (usuario == 0 && senha == 0)) {
        alert("Preencha todos os campos");
    }
    else {
        incorreto.textContent = ("Usuário ou senha incorretos!");
    }
}

function desconto() {
    let valor = document.getElementById("valor").value
    let vip = document.getElementById("vip").value
    let cupom = document.getElementById("cupom").value
    let incorreto = document.getElementById("incorreto").value
    if (valor >= 500 && vip == "sim" || vip == "Sim") {
        alert("Desconto de 20% aplicado!  Valor final:  R$" + (valor * 0.20))
    }
    else if (valor >= 300 || cupom == "sim" || cupom == "Sim") {
        alert("Desconto de 10% aplicado! Valor final:  R$" + (valor * 0.10))
    }
    else if (valor <300 && cupom == "não" || cupom == "Não") {
        alert("Nenhum cupom aplicado")
    }
    else {
        alert("ERRO")
    }
}

function nota() {
    let nota = document.getElementById("nota").value;
    let frec = document.getElementById("frec").value;
    if ((!nota || nota <= 0) || ((!frec || frec <=0) || (nota > 100 || frec > 100))) {
        alert("VALORES INVALIDOS!");
        return;
    }
     if (nota == 0 && frec == 0) { 

        alert("Preencha todos os campos")
    }

    else if (nota >=60 && frec >=75) {
        alert("Aprovado")
    }
    else if (nota >=40 && nota <60 && frec >=75) {
        alert("Recuperação")
    }
    else if (nota <40 || frec <75) {
        alert("Reprovado")
    }
    else if (nota == 0 && frec == 0) {
        alert("Preencha todos os campos")
    }
}