 $(document).ready(function(){
    $(".button-collapse").sideNav();
    $('.modal').modal();

    var xhr = new XMLHttpRequest();

    xhr.setRequestHeader('token', token);

    xhr.send();



    xhr.open( "GET", 'http://127.0.0.1:8888/log', false ); // false for synchronous request
    xhr.send( null );

  });

  $('#showPassword').click(function(){
      if ($('#password').prop('type') == 'password') {
        $('#password').prop('type', 'text')
    } else {
        $('#password').prop('type', 'password')
    }
  });
  
