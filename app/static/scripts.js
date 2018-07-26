$(document).ready(function(){

    $('#admin-login').on('submit', function(event){

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
              alert(data.error)
        }
        else{
              window.location.href = '/admin';
              alert(data.status)
        }

        });

        event.preventDefault();

    });

});