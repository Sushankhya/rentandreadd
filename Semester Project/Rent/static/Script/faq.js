const questionBtn = document.querySelectorAll(".question");
const answers = document.querySelectorAll(".answer");


questionBtn.forEach(question=>{
    question.addEventListener("click", (e)=>{
        e.preventDefault();
        const pannel = question.nextElementSibling
        question.childNodes[1].classList.toggle("up")
        question.childNodes[1].classList.toggle("down")
        question.classList.toggle("active")
        if(pannel.style.maxHeight){
            pannel.style.maxHeight = null;
        }
        else {
            pannel.style.maxHeight = pannel.scrollHeight + "px";
        }
    })
})
