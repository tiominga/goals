function  liveToast(bg,message){

    $('#liveToast').removeClass('bg-primary bg-secondary bg-success bg-danger bg-warning bg-info bg-light bg-dark');
    $('#liveToast').addClass(bg);
    $('#toast-message').text(message);

    $('#liveToast').toast('show');

    var isSmallScreen = $(window).width() < 768; // Define 768 como limite para tela pequena

    if (isSmallScreen){
     let t = $('#bt_salvar').offset().top-30;
     $('#liveToast').offset({ top: t });
    }

  }

function refresh(){

  setTimeout(function() {
    location.reload();
  }, 1500);

}

function gastos_apaga(){

    id = document.getElementById('ed_apaga_gasto').value;
    $('#gastos_apaga_modal').modal('hide');

    var url = window.location.origin + '/gastos/list/del?id='+id;

    $.get(url, id, function(response) {
        if (response.success){

          refresh();
          liveToast('bg-primary',response.message);

        } else {
          liveToast('bg-danger',response.message);
        }
      }, 'json');

}

function gastos_modal_apaga(id){

    document.getElementById('ed_apaga_gasto').value=id;
}