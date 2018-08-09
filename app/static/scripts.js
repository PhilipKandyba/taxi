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

        if (data.error) {
            $("#error-notification").show();
            $("#error-notification").text('Error');
        }
        else{
            window.location.href = data.url;
        }

        });

        event.preventDefault();

    });

});

$(document).ready(function(){

    $('#new-admin').on('submit', function(event){

        $.ajax({
            data : {
                adm_phone: $('#adm_phone').val(),
                adm_password: $('#adm_password').val(),
                adm_password_confirmation: $('#adm_password_confirmation').val()
            },
            type: 'POST',
            url: '/create_admin',
        })
        .done(function(data) {

        if (data.error) {
            $("#success-notification").hide();
            $("#error-notification").show();
            $("#error-notification").text(data.error);
        }
        else{
            $("#error-notification").hide();
            $("#success-notification").show();
            $("#success-notification").text(data.status);
            $('#new-admin')[0].reset();
        }

        });

        event.preventDefault();

    });

});