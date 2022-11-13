const errorMessage = document.querySelector('[data-error-message]');
const closeBtn = document.querySelector('.error-close-btn');

closeBtn.addEventListener("click", ()=>{
    errorMessage.classList.add('hidden');
})