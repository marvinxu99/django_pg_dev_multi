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


// Send the transData to Server
function postTransData2() {
        
    const URL_POST = 'transdata/';
    
    // Check data - doing nothing if no transaction data.
    if (transData.allItems.length === 0) { 
        return; 
    }
    console.log("sending transData...")

    const resp_json = postData2(URL_POST, transData);

    console.log('after post data.');
}

// Post transactionn data to server after payment is done 
// data: should be an object of (k,v)'s 
async function postData2(url, data) {

    const rawResponse = await fetch(url, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    const resp = await rawResponse.json();

    if(resp.status === "S") {
        console.log('Server received data sucessfully.')

        const amount = Math.round(transData.totals.price * 100);

        URL_PAY = `/scan_n_pay/stripe/checkout/?amount=${ amount }`;

        // Get Checkout Session ID
        const result = await fetch(URL_PAY);

        const data_id = await result.json();
        
        console.log(data_id);
             
        // Redirect to Stripe Checkout
        return stripe.redirectToCheckout({sessionId: data_id.sessionId})

    }

    return resp;
};
