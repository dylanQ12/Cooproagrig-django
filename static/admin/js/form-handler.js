document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('FormHandler');
    
    form.addEventListener('submit', function(event) {
      event.preventDefault(); 
  
      const formData = new FormData(form);
      fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        },
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        if (data.success) {
          Swal.fire({
            icon: 'success',
            title: 'Éxito',
            text: '¡Se guardó satisfactoriamente!',
          }).then(() => {
            if (data.redirect_url) {
              window.location.href = data.redirect_url;
            }
          });
        } else {
          Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Hubo un problema al enviar el formulario.',
          });
        }
      })
      .catch(error => console.error('Error:', error));
    });
  });
  