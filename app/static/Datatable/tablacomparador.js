$(document).ready( function () {
    $('#table_id_comparador').DataTable(
      {"scrollX": true,
      "aaSorting": [],
      "scrollY": false,
      "paging": false,
      "searching": false,
      "info": false,
      "language": {
                  "lengthMenu": "Mostrar _MENU_ productos por página",
                  "zeroRecords": "Sólo se acepta entre 2 y 10 productos",
                  "infoEmpty": "No hay datos disponibles",
                  "infoFiltered": "(filtrado de _MAX_ patologías disponibles)",
                  "search": "Buscar:",
                  "paginate": {
                        "previous": "anterior",
                        "next": "siguiente"
                      }
              }}

                             );
} );

