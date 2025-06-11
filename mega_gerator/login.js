document.querySelector("form").addEventListener("submit", function (e) {
    e.preventDefault();

    const usuario = document.getElementById("usuario").value;
    const senha = document.getElementById("senha").value;
    const erro = document.querySelector(".erro");

    const usuarioSalvo = localStorage.getItem("usuario");
    const senhaSalva = localStorage.getItem("senha");

    if (usuario === "" || senha === "") {
        erro.textContent = "Preencha todos os campos!";
        return;
    }

    if (usuario === usuarioSalvo && senha === senhaSalva) {
        window.location.href = "main_screem.html";
    } else {
        erro.textContent = "Usuário ou senha incorretos!";
    }
});
