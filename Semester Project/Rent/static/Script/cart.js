const addToCartBtns = document.getElementsByClassName('update-cart')

const updateUserOrder = function(bookId, action){
    // console.log("ID: ", bookId, "Action: ",action)
    const url = '/upadate-cart/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            'bookId': bookId,
            'action': action
        })
    }).then((res)=>{
        return res.json()
    }).then((data)=>{
        // location.reload()
        // console.log('data', data)
    })
}

for(let i = 0; i<addToCartBtns.length; i++){
    if (addToCartBtns[i].classList.contains('not-available')){
        addToCartBtns[i].innerHTML = '<i class="fa-solid fa-cart-shopping"></i>OUT OF STOCK'
        continue
    }
    if(addToCartBtns[i].classList.contains('remove-from-cart')){
        addToCartBtns[i].innerHTML = '<i class="fa-solid fa-cart-shopping"></i>REMOVE FROM CART'
    }
    addToCartBtns[i].addEventListener('click',()=>{
        const bookId = addToCartBtns[i].dataset.book
        const action = addToCartBtns[i].dataset.action
        if(action == 'add'){
            addToCartBtns[i].dataset.action = 'remove'
            addToCartBtns[i].classList.add('remove-from-cart')
            addToCartBtns[i].innerHTML = '<i class="fa-solid fa-cart-shopping"></i>REMOVE FROM CART'
        }
        else{
            addToCartBtns[i].dataset.action = 'add'
            addToCartBtns[i].classList.remove('remove-from-cart')
            addToCartBtns[i].innerHTML = '<i class="fa-solid fa-cart-shopping"></i>ADD TO CART'

        }

        if(user === 'AnonymousUser'){
            console.log("Anonymous User");
        }
        else{
            // console.log('CSRF',csrftoken)
            updateUserOrder(bookId, action)
        }
    })
}


// removing item from cart
const removeBtns = document.getElementsByClassName('remove-btn')

for(let i = 0;i<removeBtns.length; i++){
    removeBtns[i].addEventListener('click', ()=>{
        console.log(removeBtns[i])
        const bookId = removeBtns[i].dataset.book;
        updateUserOrder(bookId, 'remove')
        removeBtns[i].parentNode.parentNode.classList.add('hidden')
        setTimeout(()=>{
            window.location.assign('/cart/');
        }, 300)
    })
}