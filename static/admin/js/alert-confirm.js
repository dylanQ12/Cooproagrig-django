document.addEventListener('DOMContentLoaded', function() {
  const buttons = document.querySelectorAll('.btn-eliminar');

  buttons.forEach(button => {
    button.addEventListener('click', function(event) {
      event.preventDefault();
      const form = button.closest('form');
      const url = form.action;
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

      swal({
        title: "¿Estás seguro?",
        text: "¡Una vez eliminado, no podrás recuperar este registro!",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
          fetch(url, {
            method: 'POST',
            headers: {
              'X-CSRFToken': csrftoken,
              'X-Requested-With': 'XMLHttpRequest'
            }
          })
          .then(response => response.json())
          .then(data => {
            if (data.success) {
              swal("¡Eliminado!", "Se elimimó con éxito.", "success")
              .then(() => {
                window.location.reload();
              });
            } else {
              swal("¡Error!", "Hubo un problema al eliminar el carrusel.", "error");
            }
          })
          .catch(error => {
            console.error('Error:', error);
            swal("¡Error!", "Hubo un problema al eliminar el carrusel.", "error");
          });
        }
      });
    });
  });
});