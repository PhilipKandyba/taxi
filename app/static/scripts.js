$(document).ready(function(){

    $('form').on('submit', function(event){

        $.ajax({
            data : {
                phone: $('#phone').val(),
                password: $('#password').val()
            },
            type: 'POST',
            url: '/login_in',
        })
        .done(function(data) {

        if (data.error){
//            $('#error').text(data.error).show();
              alert(data.error)
        }
        else{
//            $('#success').text(data.success).show();
              alert(data.status)
        }

        });

        event.preventDefault();

    });

});