$(document).ready(function(){
    $('[data-toggle="popover"]').popover();   

    // Handle the modal window when 'Search Products" btton is pressed
    $('#searchProductsModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget) // Button that triggered the modal
        var data = button.data('whatever') // Extract info from data-* attributes

        $('#search_item_list').html(`<div class="spinner-border" role="status">
                 <span class="sr-only">Loading...</span> </div>`);

        $.get('products/', function(data) {
            console.log(data)
            console.log(data.itemsCount);
            let html = "";
            if (data.itemsCount > 0) {
                for (var i=0; i<data.itemsCount; i++) {
                    element_id = `prod-${i}`
                    html += `<tr>
                            <td style="width:50%">${ data.items[i].description }</td>
                            <td class="text-right">${ data.items[i].price }</td>
                            <td class="text-center" style="width:30%">
                                <input type="number" class="js-spinner" style="width:40px;" id=element_id value=0>
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

    // // Handling search in the Modal Window
    // $("#products-table").on("click", ".js-update-book", loadForm);
    
    
    
    //$("#search_item_list").on("submit", ".js-book-update-form", saveForm);
    
  
    $('#confirmDeleteModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget) // Button that triggered the modal
        var data = button.data('whatever') // Extract info from data-* attributes
        $("#confirm_delete_post").attr("href", data)
    });
  
});