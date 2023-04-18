function iniciar() {
    div_resp.innerHTML = "";

    var voltas = Number(ipt_voltas.value);

    for (var i = 1; i <= voltas; i++) {
        div_resp.innerHTML += `<b>Carro dando a ${i}° volta</b><br>`;
    }

    div_resp.innerHTML += `Corrida finalizada!`;

}
