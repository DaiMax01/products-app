import { initializeDataTable } from './utils.js';
const token = sessionStorage.getItem("access_token");

initializeDataTable(
    "#productosTable",
    "/api/producto-data/", // URL del endpoint para esta tabla
    [
        { data: "id" },
        { data: "nombre_producto" },
        { data: "precio_unitario" },
        { data: "cantidad_disponible" },
        { data: "valor_total" },
    ],["copy", "csv", "excel", "pdf", "print", {
        text: '<i class="fa fa-plus"></i> Agregar stock de producto',
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
    token
);

$(document).on("click", ".modal-close, .modal-background", function() {
    $("#modal-catalogos").removeClass("is-active"); 
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
            console.log("Solicitud exitosa:", response);
            $("#productosTable").DataTable().ajax.reload();
            $("#modal-catalogos").removeClass("is-active");
        },
        error: function (error) {
            console.log("Error en la solicitud:", error);
        }
    });
});