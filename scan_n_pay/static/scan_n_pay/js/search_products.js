$(document).ready(function(){
    $('[data-toggle="popover"]').popover();   

    $('#searchProductsModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget) // Button that triggered the modal
        var data = button.data('whatever') // Extract info from data-* attributes
        // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
        // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
        //var modal = $(this)
        //modal.find('.modal-title').text('TEST:' + recipient)
        //$("#detail_img").attr("src", data)
        $.get('products/', function(data, status){
            console.log(data);
            
        });

    });
  
    $('#confirmDeleteModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget) // Button that triggered the modal
        var data = button.data('whatever') // Extract info from data-* attributes
        $("#confirm_delete_post").attr("href", data)
    });
  
  });