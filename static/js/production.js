document.addEventListener('DOMContentLoaded', function () {
    const elements = document.querySelectorAll('.animated-element, .animated-title, .animated-line, .animated-arrow, .animated-icon, .animated-button, .animated-image');
    elements.forEach(element => {
      element.style.animationPlayState = 'paused';
    });
  
    const options = {
      root: null,
      rootMargin: '0px',
      threshold: 0.1
    };
  
    const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.animationPlayState = 'running';
        } else {
          entry.target.style.animationPlayState = 'paused';
        }
      });
    }, options);
  
    elements.forEach(element => {
      observer.observe(element);
    });
  });
  