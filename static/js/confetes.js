function criarConfetes() {
    const numeroConfetes = 100; // Quantidade de confetes

    for (let i = 0; i < numeroConfetes; i++) {
        const confete = document.createElement('div');
        confete.setAttribute("id",'caindo')
        confete.classList.add('confete');
        confete.style.left = Math.random() * 100 + 'vw'; // Posição horizontal aleatória
        confete.style.animationDuration = (Math.random() * 2 + 1) + 's'; // Duração da animação aleatória
        document.getElementById('confetes').appendChild(confete);
        document.getElementById('confetes').style.display = 'none'
    
        
    }
}

criarConfetes();