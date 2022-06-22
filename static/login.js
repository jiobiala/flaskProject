function sendMsg(data) {

        var u = $("#username").val();
        var p = $("#password").val();

        var form = new FormData();
        form.append('username', u );
        form.append('password', p);


        $.ajax({
            type: 'POST',
            url: '/login',
            data: form,
            cache: false,
            processData: false,
            contentType: false,

        }).done(function(data) {
                $(login_form).replaceWith(data)
        })
    }