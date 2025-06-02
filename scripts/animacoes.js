const elementosAnimados = document.querySelectorAll('.fade-in');

const animarScroll = () => {
  elementosAnimados.forEach(elemento => {
    const topoElemento = elemento.getBoundingClientRect().top;
    const alturaTela = window.innerHeight * 0.85;

    if (topoElemento < alturaTela) {
      elemento.classList.add('ativo');
    }
  });
}

window.addEventListener('scroll', animarScroll);
animarScroll();
