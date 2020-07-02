$(function () {
    $(".js-create-book").click(function () {
        $.ajax({
            url: '/books/create/',
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-book").modal("show");
                },
            success: function (data) {
                $("#modal-book .modal-content").html(data.html_form);
            }
        });
    });

    $("#modal-book").on("submit", ".js-book-create-form", function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    alert("Book created!");  // <-- This is just a placeholder for now for testing
                }
                else {
                    $("#modal-book .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });
  
});