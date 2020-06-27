//console.log("Sanity check!");

// Class to hold basic item data (front-end)
class Item {
    constructor(id, itemId, description, price, discount=0, discountType=1, quantity=1){
        this.id = id;
        this.itemId = itemId;
        this.description = description;
        this.quantity = quantity;
        this.price = price;               // regular price 
        this.discount = discount;         // this can be a percentage, or amount (UOM: dollar)
        this.discountType = discountType;            // 1: percentage off regular price (10 is 10%); 2: ammount off. (0.5 = 50 cents)
        this.discountSpecial = 0;         // this can manager's account, item damaged discount. etc
        this.discountAmount = 0;          // this is the amount ($).
        this.priceFinal = 0 ;             // Price customer paying for the item, is equal to (price - discountCalculated)
        this.comment ='';
    }
    
    // For now - 
    calcFinalPrice() {
        if(this.discountType === 1) {         // amount off 
            this.discountAmount = this.discount;
        } 
        else if (this.discountType === 2) {     /* percentage off */
            this.discountAmount = this.price * (1 - this.discount/100);
        }

        this.priceFinal = this.price - this.discountAmount;
    }
}
 
// Class to hold all transaction data
class TransactionData {
    constructor() {
        this.allItems = [];      // Array of Items
        this.totals = {
            quantity: 0,
            originalPrice: 0,
            discount: 0, 
            price: 0,            // addition of all priceFinal
        }
        this.coupon = {
            amount: 0,
            couponId: 0,          // it means no coupon if coupon_id <= 0

        }
        this.payment_amt = -1;    // this the final amount to pay (total price - coupon amount)
 
        this.terminal_id = 123456;
        this.operator_id = 123456;
 
        this.comment = '';
    }

    // add a new item
    addItem(itemId, description, price, discount=0, discountType=1, quantity=1) {
        let id, newItem; 

        // Create new ID
        if (this.allItems.length > 0) {
            id = this.allItems[this.allItems.length - 1].id + 1;
        } else {
            id = 0;
        }

        newItem = new Item(id, itemId, description, price, discount=0, discountType=1, quantity=1); 
        newItem.calcFinalPrice();

        this.allItems.push(newItem);  

        this.addItemToTotals(newItem);
        
        return newItem;
    }

    deleteItem(id) {
        // id = 6
        //data.allItems[id];
        // ids = [1 2 4 6 8]
        //index = 3
        
        let ids = this.allItems.map(item => item.id)
        let index = ids.indexOf(id);

        if (index !== -1) {
            this.allItems.splice(index, 1);
        }
    }

    // Reset transactionData to empty (ready for next transaction)
    resetData() {
        this.allItems.splice(0, this.allItems.length);
        this.totals.price = 0;
        this.totals.quantity = 0;
        this.totals.originalPrice = 0;
        this.discountAmount = 0;
        this.comment = '';
    } 
    
    // Calculate totals: price, quantity
    calculateTotals() {
        this.totals.price = this.allItems.reduce( (total, item) => 
            { return total + item.priceFinal; }, 0);

        this.totals.quantity = this.allItems.reduce( (total, item) => 
            { return total + item.quantity; }, 0);
        
        this.totals.discount = this.allItems.reduce( (total, item) =>
            { return total + item.discountAmount; }, 0);

        this.totals.originalPrice = this.allItems.reduce( (total, item) =>
            { return total + item.price; }, 0);
    }

    // Add item price, quantity to totals
    addItemToTotals(item) {
        this.totals.price += item.priceFinal;
        this.totals.price.toFixed(2);
        
        this.totals.originalPrice += item.price;
        this.totals.originalPrice.toFixed(2);
        
        this.totals.quantity += item.quantity;

        this.totals.discount += item.discountAmount;
        this.totals.discount.toFixed(2);
    }
} 

// Class to hold UI data and methods
class UIController {

    static #DOMstrings = {
        barcodeInput: 'barcode',
        itemsContainer: 'ItemsContainer',
        itemsList: 'items__list',
        transactionItem: '.transaction-item',
        totalPrice: 'total_price',
        warningMessage: 'warning_msg',
    };

    // Add and display the item in the allItems list
    static addListItem(item, totals) {      
        // Create HTML string        
        let html = `<tr class="transaction-item" id="item-${item.id}">
                        <td class="item-name">${item.description}</td>
                        <td class="item-quantity">${item.quantity}</td>
                        <td class="item-original-price">${item.price}</td>
                        <td class="item-discount">${item.discountAmount}</td>
                        <td class="item-price">${item.priceFinal}</td>
                    </tr>`
        console.log(html);
        
        // Insert the HTML into the DOM
        const listRef = document.getElementById(this.#DOMstrings.itemsList);
        const newRow = listRef.insertRow();   // Insert a row at the end of the table
        newRow.innerHTML = html;
        
        // Make the last inserted item to be visible if needed.
        newRow.scrollIntoView(false);

        // Update the total price as well
        this.updateTotals(totals);
    }   
    
    static formatMoney(number, locale='en-CA', currency='CAD') {
        return number.toLocaleString(locale, 
                { style: 'currency', currency: currency }
            );
    }

    static getCurrencySymbol = (locale, currency) => {
        
        // getCurrencySymbol('en-US', 'CNY') // CN¥
        //getCurrencySymbol('zh-CN', 'CNY') // ￥      
        
        return (0).toLocaleString(locale, 
                    { style: 'currency', currency, minimumFractionDigits: 0, maximumFractionDigits: 0 }
            ).replace(/\d/g, '').trim();
    }
    
    static updateTotals({ quantity, originalPrice, discount, price }) {
        // Update the total price as well
        let html = `<td class="text-right item-name"><strong> Totals:</strong></td>
                <td class="item-quantity">
                    ${ quantity }
                </td>
                <td class="item-original-price">
                    ${ this.formatMoney(originalPrice) }
                </td>
                <td class="item-discount">
                    ${ this.formatMoney(discount) }
                </td>
                <td class="item-price total-price">
                    <strong>${ this.formatMoney(price) }</strong>
                </td>`

        document.getElementById(this.#DOMstrings.totalPrice).innerHTML = html;
    }

    // Delete the select item from UI display
    static deleteListItem(selectorID) {            
        const el = document.getElementById(selectorID);
        el.parentNode.removeChild(el);       
    }
    
    // Delelet all list items - empty the list for next transaction.
    static deleteAllListItems() {
        const listRef = document.getElementById(this.#DOMstrings.itemsList);
        while (listRef.firstChild) {
            listRef.removeChild(listRef.firstChild);
        }

        this.updateTotals({ price: 0, discount: 0 });
    }

    // Reset the barcode input field.    
    static clearBarcodeField() {
        let el_barcode = document.getElementById(this.#DOMstrings.barcodeInput);
        el_barcode.value = '';
        el_barcode.focus();

        this.hideWarningMsg();
    }

    // Reset UI display to ready for a new transaction
    static resetUI() {
        this.deleteAllListItems();
        this.clearBarcodeField();
    }

    // Display warning message in red  
    static displayWarningMsg(msg) {
        const msg_div = document.getElementById(this.#DOMstrings.warningMessage);
        msg_div.classList.remove('invisible');
        msg_div.innerText = `**${msg}**`
    }
    
    // Hide warning message
    static hideWarningMsg() {
        const msg_div = document.getElementById(this.#DOMstrings.warningMessage);
        msg_div.classList.add('invisible');
        msg_div.innerText = "ww";
    }
}


// Global variable to hold all transaction data
const transData = new TransactionData(); 

async function getItemInfo(barcode) {
    try {
        const result = await fetch(`get_item/?barcode=${barcode}`);
        const data = await result.json();
        console.log(data);
        if(data.validInd === 1) {
            
            // 1. Add the item data to TransData
            const newItem = transData.addItem(data.itemId, data.description, data.price);
            console.log(newItem);
            console.log(transData);       

            // 2. add the item to UI display
            UIController.addListItem(newItem, transData.totals);

            // 3. Reset the barcode input box
            UIController.clearBarcodeField();

        } else {
            //console.log("data not valid.")
            UIController.displayWarningMsg('Invalid barcode.');
        }

    } catch(error) {
        //console.log(error);
        UIController.displayWarningMsg('Not able to get item information.');
    }
}

function getItemInfoByCode() {
    const barcode =  document.getElementById('barcode').value;
    if (barcode.length > 0) {
      getItemInfo(barcode);
    }
}

const setupEventListeners = () => {
    // When the Enter button is pressed
    document.getElementById('btn_enter').addEventListener('click', getItemInfoByCode);

    // When a Enter key is pressed in Barcode input box
    document.getElementById('barcode').addEventListener('keypress', function(event) {   
        if((event.keyCode === 13) || (event.which === 13)) {
            event.preventDefault();
            getItemInfoByCode();
            // console.log(event.target);
            // console.log(event.target, event.target.parentNode);
            // console.log(event.keyCode);
        }
    })

    // When the Send Data! button is clicked
    document.getElementById('send_trans_data').addEventListener('click', postTransData);

    document.getElementById('new_transaction').addEventListener('click', startNewTransaction);

    document.getElementById('pay_submit').addEventListener('click', ()=> {
        document.querySelector("#submitPayment").click();
    });

    document.getElementById('post-n-pay').addEventListener('click', postAndPay);

}
setupEventListeners();


// Start a new transaction - discard previous data
function startNewTransaction() {
    // 1. Reset the transaction data to empty
    transData.resetData();

    // 2. remove previous items (if any) from UI
    UIController.resetUI(); 
}


// Send the transData to Server
function postTransData() {
        
    const URL_POST = 'transdata/';
    
    // Check data - doing nothing if no transaction data.
    if (transData.allItems.length === 0) { 
        return; 
    }
    console.log("sending transData...")

    const resp_json = postData(URL_POST, transData);
    console.log('after post data.');
}

// Post transactionn data to server after payment is done 
// data: should be an object of (k,v)'s 
async function postData(url, data) {

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
    }

    return resp;
};

