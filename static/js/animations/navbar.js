document.addEventListener('DOMContentLoaded', function () {
    var navLinks = document.querySelectorAll('.nav-link');
  
    navLinks.forEach(function (link) {
      link.style.position = 'relative';
      link.style.transition = 'all 0.3s ease';
  
      link.addEventListener('mouseover', function () {
        this.style.transform = 'scale(1.1)';
        this.style.color = '#007bff'; // Cambia a tu color deseado
        this.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)';
        this.style.backgroundColor = '#f8f9fa'; // Cambia a tu color deseado
  
        // Crear y animar pseudo-elemento
        var underline = document.createElement('span');
        underline.classList.add('underline');
        this.appendChild(underline);
        setTimeout(function() {
          underline.style.width = '100%';
        }, 0);
      });
  
      link.addEventListener('mouseout', function () {
        this.style.transform = 'scale(1)';
        this.style.color = ''; // Restablece el color original
        this.style.boxShadow = '';
        this.style.backgroundColor = '';
  
        // Remover pseudo-elemento
        var underline = this.querySelector('.underline');
        if (underline) {
          underline.style.width = '0';
          setTimeout(function() {
            if (underline.parentElement) {
              underline.parentElement.removeChild(underline);
            }
          }, 300);
        }
      });
    });
  });
  
  
  