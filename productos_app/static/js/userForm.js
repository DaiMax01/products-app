
$("#user_form").submit(function (e) {
    const formData = $(this).serialize();
    e.preventDefault();
    Swal.fire({
        title: 'Procesando Solicitud',
        text: 'Por favor, espera un momento.',
        allowOutsideClick: false,
        allowEscapeKey: false,
        allowEnterKey: false,
        showConfirmButton: false,
        didOpen: () => {
            Swal.showLoading();
        }
    });
    $.ajax({
        type: "POST",
        url: $(this).data("url"),
        data: formData,
        dataType: "json",
        success: function (response) {
            Swal.close();
            Swal.fire({
                title: 'Bienvenido!',
                text: 'Se le redireccionará en un momento',
                icon:'success',
                timer:'1000',
                showConfirmButton: true,
            }).then(() => {
                sessionStorage.setItem("access_token", response.access);
                window.location.href = "/";
            });
        },
        error: function (error) {
            console.log(error);

            Swal.close();
            Swal.fire({
                title: 'Error!',
                text: 'Credenciales incorrectas',
                icon: 'error',
                timer:'1000',
                showConfirmButton: true,
            }).then(() => {
                Swal.close();
            })
        },
        complete: function () {

            console.log(response)
        },
    });
});
