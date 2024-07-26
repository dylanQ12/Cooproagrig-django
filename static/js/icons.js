document.addEventListener('DOMContentLoaded', function () {
    const icons = document.querySelectorAll('.icon');
    icons.forEach(icon => {
      icon.style.animationPlayState = 'paused';
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
  
    icons.forEach(icon => {
      observer.observe(icon);
    });
  });
  