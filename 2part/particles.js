const particlesContainer = document.querySelector('.particles','footer');
const particleCount = 50;

for (let i = 0; i < particleCount; i++) {
  const particle = document.createElement('div');
  particle.className = 'particle';
  particlesContainer.appendChild(particle);
}

document.querySelectorAll('.particle').forEach((particle) => {
  const size = Math.random() * 5 + 2 + 'px';
  particle.style.width = size;
  particle.style.height = size;
  particle.style.backgroundColor = 'white';
  particle.style.position = 'absolute';
  particle.style.top = Math.random() * 100 + '%';
  particle.style.left = Math.random() * 100 + '%';
  particle.style.animation = `moveParticles ${Math.random() * 5 + 2}s linear infinite`;
});

const style = document.createElement('style');
style.textContent = `
  @keyframes moveParticles {
    0% {
      transform: translateY(0);
      opacity: 1;
    }
    100% {
      transform: translateY(-200px);
      opacity: 0;
    }
  }
`;
document.head.appendChild(style);
