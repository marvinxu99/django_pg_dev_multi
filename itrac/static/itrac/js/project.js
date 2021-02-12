$(function () {

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
          url: btn.attr("data-url"),
          type: 'get',
          dataType: 'json',
          beforeSend: function () {
            $("#modal-project").modal("show");
          },
          success: function (data) {
            $("#modal-project .modal-content").html(data.html_form);
          }
        });
    };

    var saveForm = function () {
        // In this context, this refers to the element with class .js-book-create-form.
        // Which is the element that fired the submit event. So when we select $(this) we are selecting the actual form.
        var form = $(this);

        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#project-table tbody").html(data.html_project_list);  // <-- Replace the table body
                    $("#modal-project").modal("hide");  // <-- Close the modal dialogue
                }
                else {
                    $("#modal-project .modal-content").html(data.html_form);
                }
            }
        });

        //A very important detail here: in the end of the function we are returning false. That’s because
        // we are capturing the form submission event. So to avoid the browser to perform a full HTTP POST
        // to the server, we cancel the default behavior returning false in the function
        return false;
    };

    // Create book
    $(".js-create-project").click(loadForm);
    $("#modal-project").on("submit", ".js-project-create-form", saveForm);

    // Update book
    $("#project-table").on("click", ".js-edit-project", loadForm);
    $("#modal-project").on("submit", ".js-project-edit-form", saveForm);

    // Delete book
    $("#project-table").on("click", ".js-delete-project", loadForm);
    $("#modal-project").on("submit", ".js-project-delete-form", saveForm);

});
