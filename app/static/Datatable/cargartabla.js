(function(){

function removeAccents ( data ) {
    if ( data.normalize ) {
        // Use I18n API if avaiable to split characters and accents, then remove
        // the accents wholesale. Note that we use the original data as well as
        // the new to allow for searching of either form.
        return data +' '+ data
            .normalize('NFD')
            .replace(/[\u0300-\u036f]/g, '');
    }

    return data;
}

var searchType = jQuery.fn.DataTable.ext.type.search;

searchType.string = function ( data ) {
    return ! data ?
        '' :
        typeof data === 'string' ?
            removeAccents( data ) :
            data;
};

searchType.html = function ( data ) {
    return ! data ?
        '' :
        typeof data === 'string' ?
            removeAccents( data.replace( /<.*?>/g, '' ) ) :
            data;
};

}());




$(document).ready( function () {
    $('#table_id').DataTable(
      {"scrollX": true,
      "scrollY": false,
      "language": {
                  "lengthMenu": "Mostrar _MENU_ patologías por página",
                  "zeroRecords": "No se ha encontrado nada - disculpe",
                  "info": "Mostrando página _PAGE_ de _PAGES_",
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


$(document).ready( function () {
    $('#table_plantas').DataTable(
      {"scrollX": true,
      "pageLength": 10,
      "scrollY": false,
      "language": {
                        "lengthMenu": "Mostrar _MENU_ plantas por página",
                        "zeroRecords": "No se ha encontrado nada - disculpe",
                        "info": "Mostrando página _PAGE_ de _PAGES_",
                        "infoEmpty": "No hay datos disponibles",
                        "infoFiltered": "(filtrado de _MAX_ plantas disponibles)",
                        "search": "Buscar:",
                                          "paginate": {
                                                "previous": "anterior",
                                                "next": "siguiente"
                                              }
                    }}
                             );
} );

$(document).ready( function () {
    $('#table_id_productos').DataTable({
      "aaSorting": [],
      "scrollX": true,
      "pageLength": 10,
      "scrollY": false,
      "language": {
                  "lengthMenu": "Mostrar _MENU_ productos por página",
                  "zeroRecords": "No se ha encontrado nada - disculpe",
                  "info": "Mostrando página _PAGE_ de _PAGES_",
                  "infoEmpty": "No hay datos disponibles",
                  "infoFiltered": "(filtrado de _MAX_ productos disponibles)",
                  "search": "Buscar:",
                  "paginate": {
                        "previous": "anterior",
                        "next": "siguiente"
                      }
              }}

                             );
} );

