//$(document).ready(function(){
$('[data-toggle="popover"]').popover();

// Set the focus to barcode input once loaded.
document.getElementById("barcode_input").focus();

// To hold all the selecte items form Product Search window
class ProductItems {
    constructor() {
        this.data = [];
        /* data format:
            {
                itemId: 1
                itemIdentId: 1,
                description: 'xxxx',
                itemPriceId: 1,
                price: '10.24',
                quantity: 2
            }
        */
    }

    updateQuantity(id, qty) {
        this.data[id].quantity = qty;
    }

    updatePrice(id, price) {
        this.data[id].price = price;
    }

    resetData() {
        this.data = [];
    }

}

const selectedItems = new ProductItems();

// Handle the modal window when 'Search Products" btton is pressed
$('#searchProductsModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    //var data = button.data('whatever') // Extract info from data-* attributes

    // Loading spinner...
    $('#list-search-products').html(`<div class="spinner-border" role="status">
                <span class="sr-only">Loading...</span> </div>`);

    // Request all product info from server (json data)
    $.get('products/', function(data) {

        // Store data into the global variable
        selectedItems.data = data.items
        console.log(selectedItems.data)

        let html = "";
        if (data.itemsCount > 0) {
            for (var i=0; i<data.itemsCount; i++) {

                element_id = `prod-${i}`
                html += `
                    <tr class="prod-list-item">
                        <td style="width:50%">${ data.items[i].description }</td>
                        <td class="text-right">${ data.items[i].price }</td>
                        <td class="text-center" style="width:30%">
                            <input type="number" class="js-spinner prod-quantity_input" style="width:50px;" id=${ element_id } value=0 min="0", max="20" >
                        </td>
                    </tr>`
            }
        } else {
            html = `<tr><td colspan="7" class="text-center bg-warning">Products not found. </td></tr>`
        }
        $('#search_item_list').html(html);

    });
});

// Set up Search Product filter
function filterFunction() {
    const input = document.getElementById("productInputFilter");
    const filter = input.value.toUpperCase();
    console.log("typing..");

    const prods = document.getElementsByClassName("prod-list-item");
    for (let i = 0; i < prods.length; i++) {
        let prod_item = prods.item(i)
        const txtValue = prod_item.textContent || prod_item.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
        prod_item.style.display = "";
        } else {
        prod_item.style.display = "none";
        }
    }
    }
    document.getElementById("productInputFilter").onkeyup = filterFunction;

// Handling "Select Items" in the Modal Window
//const select_btn = document.getElementById("select-items-btn");
//select_btn.onclick = function() { console.log("clicked"); };
$('#select-items-btn').click(function(){

    $("#searchProductsModal").modal("hide");  // <-- Close the modal dialogue

    quantity_list = document.getElementsByClassName("prod-quantity_input");
    console.log(quantity_list.length)

    for (let i=0; i<quantity_list.length; i++) {
        qty_input = quantity_list[i];
        splitId = qty_input.getAttribute('id').split('-');
        id = parseInt(splitId[1]);

        selectedItems.updateQuantity(id, parseInt(qty_input.value));

        // To ensure the correct data type for price
        selectedItems.updatePrice(id, parseFloat(selectedItems.data[id].price));
    }
    console.log(selectedItems.data);

    for (let i=0; i<selectedItems.data.length; i++) {
        item = selectedItems.data[i];

        if(item.quantity > 0) {
            // 1. Add the item data to TransData
            const newItem = transData.addItem(item, item.quantity);
            console.log(newItem);

            // 2. add the item to UI display
            UIController.addListItem(newItem, transData.totals);

            // 3. Reset the barcode input box
            UIController.clearBarcodeField();
        }
    }
    console.log(transData);
})

// $('#confirmDeleteModal').on('show.bs.modal', function (event) {
//     var button = $(event.relatedTarget) // Button that triggered the modal
//     var data = button.data('whatever') // Extract info from data-* attributes
//     $("#confirm_delete_post").attr("href", data)
// });

//});
