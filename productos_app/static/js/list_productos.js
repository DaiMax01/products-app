import { initializeDataTable } from './utils.js';
const token = sessionStorage.getItem("access_token");

initializeDataTable(
    "#productosTable",
    "/api/catalogo-data/",
    [
        { data: "id" },
        { data: "descripcion" },
        { data: "costo_unitario" },
        { data: "precio_venta" },
    ],
    ["copy", "csv", "excel", "pdf", "print", {
        text: '<i class="fa fa-plus"></i> Agregar Producto',
        className: 'button is-success',
        action: function(e, dt, node, config) {
            const modal = document.getElementById('modal-catalogos');
            modal.classList.add('is-active');
        },
        init: function(api, node, config) {
            $(node).removeClass('dt-button')
        }
    }],
    "Bfrtlip",
    token,
    {
        
        "columnDefs": [
            {
                "targets": 4, 
                "data": null,
                "defaultContent": '<button class="button is-danger is-outlined is-small is-rounded delete-producto"><i class="fa fa-times"></i></button>',
                "render": function(data, type, row, meta) {
                    return '<button class="button is-danger is-outlined is-small is-rounded delete-producto" data-url=api/producto/'+ row.id +'/><i class="fa fa-times"></i></button>' +
                    '<button class="button is-warning is-outlined is-small is-rounded edit-producto" data-url=api/producto/'+ row.id +'/><i class="fa fa-pencil"></i></button>';
                }
            }

        ]
    }
);

$(document).on("click", ".modal-close, .modal-background", function() {
    $("#modal-catalogos").removeClass("is-active"); 
});

$(document).on("click", ".delete-producto", function() {
    $.ajax({
        type: "DELETE",
        headers: {
            Authorization: `Bearer ${token}`,
        },
        url: $(this).data("url"),
        success: function (response) {
            $("#productosTable").DataTable().ajax.reload();
        }
    });
});

$("#productoForm").submit(function (e) { 
    e.preventDefault();

    const formData = $(this).serialize(); 

    $.ajax({
        type: "POST",
        url: $(this).data("url"),
        headers: {
            "X-CSRFToken": csrfToken,
            Authorization: `Bearer ${token}`,
        }, 
        data: formData,
        success: function (response) {
            $("#productosTable").DataTable().ajax.reload();
            $("#modal-catalogos").removeClass("is-active");
        },
        error: function (xhr) {
            if (xhr.responseJSON) {
                $.each(xhr.responseJSON, function(field, messages) {
                    const inputField = $("#id_" + field);
        
                    if (inputField.length > 0) {
                        inputField.addClass("is-danger");
                        const errorMessage = messages.join(", ");
                        inputField.siblings(".help").remove();
                        inputField.parent().append('<p class="help is-danger">' + errorMessage + '</p>');
                    }
                });
            } else {
                alert("Ocurrió un error en el servidor. Inténtalo nuevamente.");
            }
        }
    });
});


$('#productosTable').on('click', '.edit-producto', function() {
    const url = $(this).data('url');  


    $.ajax({
        type: "GET",
        headers: {
            Authorization: `Bearer ${token}`,
        }, 
        url: url,
        success: function(response) {
           
            $('#edit-producto-form input[name="descripcion"]').val(response.descripcion);
            $('#edit-producto-form input[name="costo_unitario"]').val(response.costo_unitario);
            $('#edit-producto-form input[name="precio_venta"]').val(response.precio_venta);

            
            $('#edit-producto-form').data('url', url);

           
            const modal = document.getElementById('modal-edit-producto');
            modal.classList.add('is-active');
        },
        error: function(error) {
        }
    });
});


$('#close-modal').click(function() {
    const modal = document.getElementById('modal-edit-producto');
    modal.classList.remove('is-active');
});


$('#edit-producto-form').submit(function(e) {
    e.preventDefault();

    const url = $(this).data('url');  
    const formData = $(this).serialize();  

    $.ajax({
        type: "PATCH",  
        url: url, 
        headers: {
            "X-CSRFToken": csrfToken,
            Authorization: `Bearer ${token}`  
        },
        data: formData,
        success: function(response) {
            const modal = document.getElementById('modal-edit-producto');
            modal.classList.remove('is-active');
            $('#productosTable').DataTable().ajax.reload();
        },
        error: function (xhr) {
            if (xhr.responseJSON) {
                $.each(xhr.responseJSON, function(field, messages) {
                    const inputField = $("#id_" + field);
        
                    if (inputField.length > 0) {
                        inputField.addClass("is-danger");
                        const errorMessage = messages.join(", ");
                        inputField.siblings(".help").remove();
                        inputField.parent().append('<p class="help is-danger">' + errorMessage + '</p>');
                    }
                });
            } else {
                alert("Ocurrió un error en el servidor. Inténtalo nuevamente.");
            }
        }
    });
});
