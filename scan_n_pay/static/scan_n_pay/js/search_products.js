//$(document).ready(function(){
    $('[data-toggle="popover"]').popover();   

    document.getElementById("barcode_input").focus();   
    
    // Handle the modal window when 'Search Products" btton is pressed
    $('#searchProductsModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget) // Button that triggered the modal
        var data = button.data('whatever') // Extract info from data-* attributes

        // Loading spinner
        $('#search_item_list').html(`<div class="spinner-border" role="status">
                 <span class="sr-only">Loading...</span> </div>`);

        // Request all product info from server
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

    // Handling "Select Items" in the Modal Window
    //const select_btn = document.getElementById("select-items-btn");
    //select_btn.onclick = function() { console.log("clicked"); };
    $('#select-items-btn').click(function(){
        console.log('clicked');

        $("#searchProductsModal").modal("hide");  // <-- Close the modal dialogue

        data= {
            description: "vancomycin 1 g inj",
            itemId: 1,
            itemIdentId: 1,
            itemPriceId: 1,
            price: 10.24,
            validInd: 1,
        };
        // 1. Add the item data to TransData
        const newItem = transData.addItem(data);
        console.log(newItem);
        console.log(transData);       

        // 2. add the item to UI display
        UIController.addListItem(newItem, transData.totals);

        // 3. Reset the barcode input box
        UIController.clearBarcodeField();
        
        return false;
    })
          
    // $('#confirmDeleteModal').on('show.bs.modal', function (event) {
    //     var button = $(event.relatedTarget) // Button that triggered the modal
    //     var data = button.data('whatever') // Extract info from data-* attributes
    //     $("#confirm_delete_post").attr("href", data)
    // });
  
//});