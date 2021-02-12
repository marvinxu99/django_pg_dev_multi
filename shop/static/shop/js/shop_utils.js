// Dependency js/winn_utils.js
function get_cart_count() {
    const csrftoken = getCookie('csrftoken');

    $.ajax({
      type: "GET",
      url: "/shop/cart/item_count",
      headers: {'X-CSRFToken': '{{ csrf_token }}'},
      success: function (data) {
        if (data.status === "S") {
          $('#cart-icon').html(data.item_count);
        }
      }
    });
};
