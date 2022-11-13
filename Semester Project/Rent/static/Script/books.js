
//slider function
function slideSlider(offset = 1){
    // const slides = btn.closest('[data-carousel]').querySelector('[data-slides]')
    const slides = document.querySelector('[data-slides]');
    // const activeSlide = slides.querySelector('[data-active]')
    const activeSlide = document.querySelector('[data-active]')
    let newIndex = [...slides.children].indexOf(activeSlide) + offset
    if(newIndex < 0 ) newIndex = slides.children.length - 1;
    if(newIndex >= slides.children.length) newIndex = 0;
    slides.children[newIndex].dataset.active = true
    delete activeSlide.dataset.active;
}

//sliding on clicking the buttons
const buttons = document.querySelectorAll("[data-carousel-btn]")
buttons.forEach(btn=>{
    btn.addEventListener('click',(e)=>{
        const offset = btn.dataset.carouselBtn === 'next'? 1: -1;
        slideSlider(offset);
    })
})

//sliding automatically after 7 seconds
setInterval(slideSlider, 7000)


//card hover 

const cardBtn = document.querySelectorAll('[data-card-btn]');
cardBtn.forEach(btn=>{
    const cartBtn = btn.querySelector('[data-cart-btn]');
    btn.addEventListener("mouseover", ()=>{
        cartBtn.style.height = '50px';
    })
    btn.addEventListener("mouseout", ()=>{
        cartBtn.style.height = null;
    })
})