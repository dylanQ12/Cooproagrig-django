document.addEventListener('DOMContentLoaded', function () {
  const elements = document.querySelectorAll('.animated-element, .animated-title, .animated-image');
  elements.forEach(element => {
    element.style.animationPlayState = 'paused';
    element.style.opacity = 0; // Ensure the elements are initially hidden
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
        entry.target.style.opacity = 1; // Ensure the elements become visible when animated
      } else {
        entry.target.style.animationPlayState = 'paused';
      }
    });
  }, options);

  elements.forEach(element => {
    observer.observe(element);
  });
});


