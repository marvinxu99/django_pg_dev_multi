// Setup Stripe payments
function setupStripePayments() {
    // Get Stripe publishable key
    fetch("/shop/stripe/config")
    .then((result) => { return result.json(); })
    .then((data) => {
        // Initialize Stripe.js
        stripe = Stripe(data.publicKey);
    });
}
setupStripePayments();

// Set up event listener for "Ready to Pay" button
document.getElementById('btn-pay-now').addEventListener('click', shop_pay_now);

// Send the transData to Server
async function shop_pay_now() {

    const cart_total = parseFloat($('#cart_total').text()).toFixed(2);

    if (cart_total <= 0) return true;

    // Stripe only accepts acmount in cents.
    const amount = Math.round(cart_total * 100);
    const res_pay = await processPayment(amount);

    if (res_pay.status === 'S')
        return stripe.redirectToCheckout({sessionId: res_pay.sessionId})

    // The post and/or pay didn't succeed
    // TO DO: to add some warnings

}

async function processPayment(amount) {
    // URL
    URL_PAY = `/shop/stripe/checkout/?amount=${ amount }`;

    // Get Checkout Session ID
    const result = await fetch(URL_PAY);
    const data = await result.json();
    //console.log(data);

    return data;
}
