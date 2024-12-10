import { initializeDataTable } from './utils.js';
const token = sessionStorage.getItem("access_token");

initializeDataTable(
    "#productosTable",
    "/api/movimiento-data/",
    [
        { data: "id" },
        { data: "fecha_formateada" },
        { data: "nombre_producto" },
        { data: "tipo" },
        { data: "cantidad" },
    ],["copy", "csv", "excel", "pdf", "print"],
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
            $("#productosTable").DataTable().ajax.reload();
            $("#modal-catalogos").removeClass("is-active");
        },
        error: function (error) {
        }
    });
});