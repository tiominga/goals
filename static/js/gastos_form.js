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

function save(){

    var formData = $('#form_gastos').serialize();

    var url = window.location.origin + '/gastos/form/salvar/'; //v sempre usa esta linha ou acaba dando erro em n situações

    $.post(url, formData, function(response) {
      if (response.success){
        liveToast('bg-primary',response.message);
      } else {
        liveToast('bg-danger',response.message);
      }
    }, 'json');

}