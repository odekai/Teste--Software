document.querySelector("form").addEventListener("submit", function (e) {
    e.preventDefault();

    const usuario = document.getElementById("usuario").value;
    const senha = document.getElementById("senha").value;
    const erro = document.querySelector(".erro");

    if (usuario === "" || senha === "") {
        erro.textContent = "Preencha todos os campos!";
        return;
    }

    localStorage.setItem("usuario", usuario);
    localStorage.setItem("senha", senha);

    alert("Cadastro realizado com sucesso!");
    window.location.href = "login.html";
});
