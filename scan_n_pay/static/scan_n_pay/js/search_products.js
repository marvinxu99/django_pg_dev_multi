$(document).ready(function(){
    $('[data-toggle="popover"]').popover();   


    // Handle the modal window when 'Search Products" btton is pressed
    $('#searchProductsModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget) // Button that triggered the modal
        var data = button.data('whatever') // Extract info from data-* attributes
        // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
        // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
        //var modal = $(this)
        //modal.find('.modal-title').text('TEST:' + recipient)
        //$("#detail_img").attr("src", data)
        $.get('products/', function(data, status){
            console.log(data)
            console.log(data.itemsCount);
            let html = "";
            if (data.itemsCount > 0) {
                for (var i=0; i<data.itemsCount; i++) {
                    element_id = `prod-${i}`
                    html += `<tr>
                            <td>${ data.items[i].description }</td>
                            <td class="text-right">${ data.items[i].price }</td>
                            <td class="text-center">
                                <input type="number" class="js-spinner" size='2' id=element_id value=0>
                            </td>             
                        </tr>`
                
                    console.log('test');
                    html += "test,"
                }
            } else {
                html = `
                    <tr>
                        <td colspan="7" class="text-center bg-warning">Products not found. </td>
                    </tr>`
            }
            
            $('#search_item_list').html(html);

        });

    });

    // Handling search in the Modal Window
    $("#products-table").on("click", ".js-update-book", loadForm);
    
    
    
    //$("#search_item_list").on("submit", ".js-book-update-form", saveForm);
    
  
    $('#confirmDeleteModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget) // Button that triggered the modal
        var data = button.data('whatever') // Extract info from data-* attributes
        $("#confirm_delete_post").attr("href", data)
    });
  
});