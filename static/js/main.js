function handleReply(response_id){
    //const reply_form_container = document.querySelector('#reply-form-container-${response_id}')
    const reply_form_container = document.getElementById('reply-form-container')
    if(reply_form_container){
        reply_form_container.style.display = 'block';
    }
}

function handleCancel(response_id){
    //const reply_form_container = document.querySelector('#reply-form-container-${response_id}')
    const reply_form_container = document.getElementById('reply-form-container')
    if(reply_form_container){
        reply_form_container.style.display = 'none';
    }
}

//js slider function
let slideIndex = 0;
showSlides()
//next-prev control
function nextSlide(){
    slideIndex++;
    showSlides();
    timer = _timer;//reset timer
}
function prevSlide(){
    slideIndex--;
    showSlides();
    timer = _timer;
}
//thumbnail controls
function currentSlide(n){
    slideIndex = n-1;
    showSlides();
    timer = _timer;
}
function showSlides(){
    let slides = document.querySelectorAll('.mySlides');
    let dots = document.querySelectorAll('.dots');

    if(slideIndex > slides.length - 1)slideIndex = 0;
    if(slideIndex < 0)slideIndex = slides.length - 1;
    //hide all slides
    slides.forEach((slide)=>{
        slide.style.display = "none";
    });
    //show one slide based on index number
    slides[slideIndex].style.display = "block";
    dots.forEach((dot)=>{
        dot.classList.remove("active");
    });
    dots[slideIndex].classList.add("active");
}
//autoplay slides...
let timer = 7; //secs
const _timer = timer;
//this function runs every 1 second
setInterval(()=>{
    timer--;
    if(timer < 1){
        nextSlide();
        timer =_timer; //reset timer
    }
}, 1000);//1sec