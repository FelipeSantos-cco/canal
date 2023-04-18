function calcular() {
    var metaEco = Number(ipt_metaEco.value);
    var guardado = Number(ipt_qntd.value);

    console.log(guardado, metaEco)

    if (metaEco > guardado) {
        div_resp.innerHTML = `Força! <br>Ainda em busca da meta! Falta R$ ${metaEco - guardado}`
    }
    else {
        div_resp.innerHTML = `Parabéns, meta alcançada!`
        if (guardado > metaEco) {
            div_resp.innerHTML += `<br>Meta ultrapassada em R$ ${guardado - metaEco}`
        }
    }

}
