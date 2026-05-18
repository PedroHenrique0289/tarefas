let produtos = [];
let preços = [];
let posicao = 0;
let quantidade = 0;

function addproduto() {
    let produto = document.getElementById("produto").value;
    let preço = document.getElementById("preco").value;
    let isValid = validarcor();
    if (isValid === 0) {
        return;
    }
    else{
        produtos.push(produto);
        preços.push(preço);
        quantidade = quantidade + 1;
        document.getElementById("quantidade").textContent = quantidade;
    }
    limparCampos2();
}

function cadastrarProduto() {
    let textoriginal = document.getElementById("listaProdutos").textContent;
    document.getElementById("listaProdutos").textContent = textoriginal + " " + produtos[posicao] + " - R$" + preços[posicao] + " | ";
    posicao = posicao + 1;
    validarcor();
    calcularTotal();
    limparCampos2();
    caro();
    barato();
}



function validarcor()
{
    let produto = document.getElementById("produto").value;
    let preço = document.getElementById("preco").value;
    if (produto == "" || preço == "") { 
        document.getElementById("mensagem").style.color = "red";
        document.getElementById("mensagem").textContent = "Por favor, preencha todos os campos.";
        return 0;
    } else if (preço <= 0) {
        document.getElementById("mensagem").style.color = "red";
        document.getElementById("mensagem").textContent = "O preço deve ser um valor acima de zero.";
        return 0;
    } else if (produto.length < 3) {
        document.getElementById("mensagem").style.color = "red";
        document.getElementById("mensagem").textContent = "O nome do produto deve conter pelo menos 3 caracteres.";
        return 0;
    } else{
        document.getElementById("mensagem").style.color = "green";
        document.getElementById("mensagem").textContent = "Produto adicionado com sucesso!";
        return 1;
    }
}

function limparCampos() {
    if (produtos.length > 0) {
        let valor = preços[produtos.length - 1];
        let valororiginal = document.getElementById("total").textContent;
        document.getElementById("total").textContent = "R$" + (valororiginal.replace("R$", "") - valor).toFixed(2);
        produtos.pop();
        preços.pop();
        listaProdutos.textContent = "";
        posicao = --posicao;
         for (let i = 0; i < posicao; i++) {
            let textoriginal = document.getElementById("listaProdutos").textContent;
            document.getElementById("listaProdutos").textContent = textoriginal + " " + produtos[i] + " - R$" + preços[i] + " | ";
        }
        quantidade = quantidade - 1;

        document.getElementById("quantidade").textContent = quantidade;
        document.getElementById("mensagem").style.color = "green";
        document.getElementById("mensagem").textContent = "Último produto cadastrado removido com sucesso!";
    } else {
        document.getElementById("mensagem").style.color = "red";
        document.getElementById("mensagem").textContent = "Não há produtos para remover.";
    }
}

function calcularTotal() {
    let total = 0;
    for (let i = 0; i < preços.length; i++) {
        total += parseFloat(preços[i]);
    }
    document.getElementById("total").textContent = "R$" + total.toFixed(2);
}

function limparCampos2() {
    document.getElementById("produto").value = "";
    document.getElementById("preco").value = "";
}

function caro() {
    let maiscaro = 0;
    let maisCaroNome = "";
    for (i = 0; i < preços.length; i++) {
        if (maiscaro < preços[i]) {
            maiscaro = preços[i];
            maisCaroNome = produtos[i];
        }
    }
    document.getElementById("produtoMaisCaro").textContent = `${maisCaroNome} R$${maiscaro}`;
}

function barato() {
    let maisbarato = 0;
    let maisBaratoNome = "";
    for (i = 0; i < preços.length; i++) {
        if (maisbarato == 0 || maisbarato > preços[i]) {
            maisbarato = preços[i];
            maisBaratoNome = produtos[i];
        }
    }
    document.getElementById("produtoMaisBarato").textContent = `${maisBaratoNome} R$${maisbarato}`;
}