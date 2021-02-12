// Setup Stripe payments
function setupStripePayments() {
    // Get Stripe publishable key
    fetch("/scan_n_pay/stripe/config")
    .then((result) => { return result.json(); })
    .then((data) => {
        // Initialize Stripe.js
        stripe = Stripe(data.publicKey);

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

// Set up event listener for "Ready to Pay" button
document.getElementById('post-n-pay').addEventListener('click', postAndPay);

// Send the transData to Server
async function postAndPay() {

    // Check data - doing nothing if no transaction data.
    if (transData.allItems.length === 0) {
        return { status: 'F' };
    }

    // 1. Send transaction data to server
    const res_post = await postTransData();
    if(res_post.status === 'S') {

        // 2. Handl stripe payment...
        // Stripe only accepts acmount in cents.
        const amount = Math.round(transData.totals.price * 100);
        const res_pay = await processPayment(amount);

        if (res_pay.status === 'S')
            return stripe.redirectToCheckout({sessionId: res_pay.sessionId})
    }

    // The post and/or pay didn't succeed
    // TO DO: to add some warnings

}

// Post transactionn data to server after payment is done
// data: should be an object of (k,v)'s
async function postTransData() {
    const URL_POST = 'transdata/';
    let csrftoken = getCookie('csrftoken');

    const response = await fetch(URL_POST, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
        },
        body: JSON.stringify(transData),
        headers: { "X-CSRFToken": csrftoken },
    });

    // Status data from server
    const res_post = await response.json();
    console.log(res_post);

    return res_post;
};

async function processPayment(amount) {
    // URL
    URL_PAY = `/scan_n_pay/stripe/checkout/?amount=${ amount }`;

    // Get Checkout Session ID
    const result = await fetch(URL_PAY);
    const data = await result.json();
    //console.log(data);

    return data;
}
