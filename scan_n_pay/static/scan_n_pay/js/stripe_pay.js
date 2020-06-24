// Setup Stripe payments
async function setupStripePayments() { 
    // Get Stripe publishable key
    fetch("/scan_n_pay/stripe/config")
    .then((result) => { return result.json(); })
    .then((data) => {
        // Initialize Stripe.js
        const stripe = Stripe(data.publicKey);

        // Event handler
        document.querySelector("#submitPayment").addEventListener("click", () => {
            if(transData.totals.price > 0) {
                URL = `/scan_n_pay/stripe/checkout/?amount=${ transData.totals.price * 100 }`;

                // Get Checkout Session ID
                fetch(URL)
                .then((result) => { return result.json(); })
                .then((data) => {
                    console.log(data);
                    
                    // Redirect to Stripe Checkout
                    return stripe.redirectToCheckout({sessionId: data.sessionId})
                })
                .then((res) => {
                    console.log(res);
                });
            }
        });
    });
}
setupStripePayments();
