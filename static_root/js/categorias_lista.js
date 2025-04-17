function loaded(){

    $('#tb_categoria_lista').DataTable({
        responsive: true,
        searching: false,
        // "bSort": false,
        "aaSorting": [],
        "pageLength": 10,
        "language": {
            "decimal": "",
            "emptyTable": "Sem dados disponíveis",
            "info": "Mostrando de _START_ até _END_ de _TOTAL_ registos",
            "infoEmpty": "Mostrando de 0 até 0 de 0 registos",
            "infoFiltered": "(filtrado de MAX registos no total)",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "Mostrar _MENU_ registos",
            "loadingRecords": "A carregar dados...",
            "processing": "A processar...",
            "search": "Procurar:",
            "zeroRecords": "Não foram encontrados resultados",
            "paginate": {
                "first": "Primeiro",
                "last": "Último",
                "next": "Seguinte",
                "previous": "Anterior"
            },
            "aria": {
                "sortAscending": ": ordem crescente",
                "sortDescending": ": ordem decrescente"
            }
        }
    });

}

function categorias_apaga(){

    id = document.getElementById('ed_apaga_categoria').value;
    $('#categorias_apaga_modal').modal('hide');
    window.location.href='del?id='+id;

}

function categorias_reinicia(){

    $('#categorias_reinicia_modal').modal('hide');

    let url =  window.location.origin + '/gastos/reinicia';
    $.get(url,0,function(response){

        if (response.success){

            location.reload();
            //liveToast('bg-primary',response.message);

        } else {
            //liveToast('bg-danger',response.message);
        }
      }, 'json');

}

function categorias_modal_apaga(id){

    document.getElementById('ed_apaga_categoria').value=id;
}

function categorias_altera(id){

    window.location.href='edit?id='+id;

}

function gasto_novo(id){

    window.location.href = window.location.origin + '/gastos/form?id='+id;

}

function gasto_lista(id){

    window.location.href = window.location.origin + '/gastos/list?id='+id;

}