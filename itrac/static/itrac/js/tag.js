$(function () {

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
          url: btn.attr("data-url"),
          type: 'get',
          dataType: 'json',
          beforeSend: function () {
            $("#modal-tag").modal("show");
          },
          success: function (data) {
            $("#modal-tag .modal-content").html(data.html_form);
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
                    $("#tag-table tbody").html(data.html_tag_list);  // <-- Replace the table body
                    $("#modal-tag").modal("hide");  // <-- Close the modal dialogue
                }
                else {
                    $("#modal-tag .modal-content").html(data.html_form);
                }
            }
        });

        //A very important detail here: in the end of the function we are returning false. That’s because
        // we are capturing the form submission event. So to avoid the browser to perform a full HTTP POST
        // to the server, we cancel the default behavior returning false in the function
        return false;
    };

    // Create tag
    $(".js-create-tag").click(loadForm);
    $("#modal-tag").on("submit", ".js-tag-create-form", saveForm);

    // Update tage
    $("#tag-table").on("click", ".js-edit-tag", loadForm);
    $("#modal-tag").on("submit", ".js-tag-edit-form", saveForm);

    // Delete tag
    $("#tag-table").on("click", ".js-delete-tag", loadForm);
    $("#modal-tag").on("submit", ".js-tag-delete-form", saveForm);

    // Set up the filter for tag list
    $("#tagInput").on("keyup", () => {
        const input = document.getElementById("tagInput");
        const filter = input.value.toUpperCase();

        const tags = document.getElementsByClassName("tags-item-tag");
        for (let i = 0; i < tags.length; i++) {
          let tag_item = tags.item(i);
          let tag_title = tags.item(i).firstElementChild;
          const txtValue = tag_title.textContent || tag_title.innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tag_item.style.display = "";
          } else {
            tag_item.style.display = "none";
          }
        }
    })

});
