 $(document).ready(function(){
    $(".button-collapse").sideNav();
    $('.modal').modal();
  });

  $('#showPassword').click(function(){
      if ($('#password').prop('type') == 'password') {
        $('#password').prop('type', 'text')
    } else {
        $('#password').prop('type', 'password')
    }
  });
  
