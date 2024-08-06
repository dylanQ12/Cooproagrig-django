$(document).ready(function () {
  function initializeDataTable(selector) {
      $(selector).DataTable({
          language: {
              "decimal": "",
              "emptyTable": "No hay datos disponibles en la tabla",
              "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
              "infoEmpty": "Mostrando 0 a 0 de 0 registros",
              "infoFiltered": "(filtrado de _MAX_ registros en total)",
              "infoPostFix": "",
              "thousands": ",",
              "lengthMenu": "Mostrar _MENU_ registros",
              "loadingRecords": "Cargando...",
              "processing": "Procesando...",
              "search": "Buscar:",
              "zeroRecords": "No se encontraron registros coincidentes",
              "paginate": {
                  "first": "Primero",
                  "last": "Último",
                  "next": "Siguiente",
                  "previous": "Anterior"
              },
              "aria": {
                  "sortAscending": ": activar para ordenar la columna de manera ascendente",
                  "sortDescending": ": activar para ordenar la columna de manera descendente"
              }
          }
      });
  }

  // Inicializar DataTables en tablas con el selector proporcionado
  initializeDataTable("#basic-datatables");
});
  