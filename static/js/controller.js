function testesAutomaticos(testes){
    testes.forEach(element => {
        if(element['acao'] == "itemExiste"){
            console.log(window.getComputedStyle(document.getElementById(element['id'])).display)
        }
    });
}