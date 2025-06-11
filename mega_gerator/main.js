function gerarSenha(tamanho = 12) {
    const maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const minusculas = "abcdefghijklmnopqrstuvwxyz";
    const numeros = "0123456789";
    const simbolos = "!@#$%^&*()_+";

    const todos = maiusculas + minusculas + numeros + simbolos;

    if (tamanho < 8) {
        alert("Tamanho mínimo da senha é 8.");
        return "";
    }

    let senha = [
        maiusculas[Math.floor(Math.random() * maiusculas.length)],
        minusculas[Math.floor(Math.random() * minusculas.length)],
        numeros[Math.floor(Math.random() * numeros.length)],
        simbolos[Math.floor(Math.random() * simbolos.length)],
    ];

    for (let i = 0; i < tamanho - 4; i++) {
        senha.push(todos[Math.floor(Math.random() * todos.length)]);
    }

    return senha.sort(() => Math.random() - 0.5).join("");
}

function salvarSenha(rede, senha) {
    let senhas = JSON.parse(localStorage.getItem("senhas")) || [];
    senhas.push({ rede, senha });
    localStorage.setItem("senhas", JSON.stringify(senhas));
}

function mostrarSenhasSalvas() {
    const lista = document.getElementById("lista-senhas");
    lista.innerHTML = "";

    const senhas = JSON.parse(localStorage.getItem("senhas")) || [];

    senhas.forEach(item => {
        const li = document.createElement("li");
        li.innerHTML = `<strong>${item.rede}:</strong> ${item.senha}`;
        lista.appendChild(li);
    });
}

document.addEventListener("DOMContentLoaded", () => {
    mostrarSenhasSalvas();

    document.getElementById("form-rede").addEventListener("submit", function (e) {
        e.preventDefault();

        const rede = document.getElementById("rede").value.trim();
        if (rede === "") {
            alert("Informe o nome da rede social.");
            return;
        }

        const senha = gerarSenha();
        salvarSenha(rede, senha);
        mostrarSenhasSalvas();

        document.getElementById("rede").value = "";
    });
});
