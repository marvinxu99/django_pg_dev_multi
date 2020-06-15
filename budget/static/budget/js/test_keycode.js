var test_keycode = (function() {

    document.addEventListener('keypress', function(e) {   
        console.log(e);
    })
    document.addEventListener('click', function(e) {   
        console.log(e);
        console.log(e.target, e.target.parentNode);
    })
    
})();


