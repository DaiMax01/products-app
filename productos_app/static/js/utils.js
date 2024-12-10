
export function initializeDataTable(selector, ajaxUrl, columns,buttons,dom,token,extraConfig = {}) {
    
    const defaultConfig = {
        processing: true,
        serverSide: true,
        language: {
            url: "https://cdn.datatables.net/plug-ins/1.10.15/i18n/Spanish.json",
        },
        scrollY: "400px",
        scrollX: false,
        autoWidth: false,
        ajax: {
            url: ajaxUrl, 
            type: "POST",
            headers: {
                "X-CSRFToken": csrfToken,
                Authorization: `Bearer ${token}`,
            },
            data: function (d) {
               
            },
        },
        dom:dom,
        columns: columns,
        buttons: buttons
    };
    const config = Object.assign({}, defaultConfig, extraConfig);
    $(selector).DataTable(config);
    setTimeout(function () {
        $(selector).DataTable().columns.adjust();
      }, 500);
}
