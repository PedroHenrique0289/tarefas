let produtos = [
    "Mouse",
    "Teclado",
    "Monitor",
    "Cabo HDMI",
    "Pen Drive",
    "Webcam"
];
let preços = [];
let posição = 0;

function mostrarestoque() {
    let local = document.getElementById("estoqueResult");
    local.textContent = "";


    for (posicao = 0; posicao < produtos.length; posicao++) {
        let textoadicionar = document.createElement("li");
        
        textoadicionar.textContent = produtos[posicao];
        local.appendChild(textoadicionar);
    }
}

function calcularTotal() {
    const mouse = document.getElementById("cmouse").checked;
    const teclado = document.getElementById("cteclado").checked;
    const monitor = document.getElementById("cmonitor").checked;
    const cabo = document.getElementById("ccabo").checked;
    const pendrive = document.getElementById("cpendrive").checked;
    const webcam = document.getElementById("cwebcam").checked;
    let total = 0;
    if (mouse) {
        total += 50;
    }
    if (teclado) {
        total += 100;
    } 
    if (monitor) {
        total += 300;
    }
    if (cabo) {
        total += 20;
    }
    if (pendrive) {
        total += 50;
    }
    if (webcam) {
        total += 150;
    }
    caixaresult.textContent = `O total da compra é R$ ${total},00`;
}

function tentaracessar() {
    let tentativa = 1;  
    let senhaa = prompt("Senha: ");
    while (senhaa != 1234 && tentativa < 3) {
        tentativa++;
        alert("Senha incorreta. Tente novamente.");
        senhaa = prompt("Senha: ");
    }
    if (tentativa == 3)
    {
        document.getElementById("senharesult").textContent = "Acesso bloqueado. Você excedeu o número máximo de tentativas.";
        return;
    }

    document.getElementById("senharesult").textContent = `Senha correta! Você tentou ${tentativa} vezes.`;
}

let alunos = [];
let notas = [];
let situacao = [];
function gerarRelatorio() {
    let nomeAlunos = document.getElementById("nomeAlunos").value;
    let notaAlunos = parseFloat(document.getElementById("notaAlunos").value);
    let st = document.getElementById("relatorioList");
    limparCampos();

    if (isNaN(notaAlunos) || notaAlunos <= 0) {
        document.getElementById("relatorioo").textContent = "Digite um nome e uma nota válida.";
        document.getElementById("relatorioo").style.color = "red";
    } else if (notaAlunos > 100) {
        document.getElementById("relatorioo").textContent = "A nota deve ser entre 0 e 100.";
        document.getElementById("relatorioo").style.color = "red";
    }

    else{
        alunos.push(nomeAlunos + " - Nota:" + notaAlunos + " - " + (notaAlunos >= 60 ? "Aprovado" : "Reprovado"));
        notas.push(notaAlunos);
        situacao.push(notaAlunos >= 60 ? "Aprovado" : "Reprovado");
    }
    mostrarRelatorio();

}


function mostrarRelatorio() {
    let relatorioLista = document.getElementById("relatorioList");
    let me = document.getElementById("media");
    let soma = 0;
    while (relatorioLista.firstChild) {
        relatorioLista.removeChild(relatorioLista.firstChild);
    }
    for (let i = 0; i < alunos.length; i++) {
        let item = document.createElement("li");
        item.textContent = alunos[i];
        relatorioLista.appendChild(item);
        soma += notas[i];
    }

    if(alunos.length > 0) {
        let media = soma / alunos.length;
        me.textContent = `Média da Turma: ${media.toFixed(2)}`;
    } else {
        me.textContent = "Média da Turma: ";
    }
}

function limparCampos() {
    document.getElementById("nomeAlunos").value = "";
    document.getElementById("notaAlunos").value = "";
    document.getElementById("relatorioo").textContent = "";
    document.getElementById("relatorioo").style.color = "black";
}

function iniciarconf() {
    // 1. soma começa em zero
    let soma = 0;

    // 2. Pede um valor para o usuário
    let valor = Number(prompt("Digite um número (ou 0 para finalizar): "));

    // 3. Enquanto o valor for diferente de zero
    while (valor !== 0) {
    
    // 4. Soma o valor digitado 
    soma += valor;

    // 5. Pede outro valor
    valor = Number(prompt("Digite outro número (ou 0 para finalizar): "));
    
    }

    // 6. Mostar a Soma final
    textContent = `Soma final: ${soma}`;
    document.getElementById("resultadoConf").textContent = textContent;
}