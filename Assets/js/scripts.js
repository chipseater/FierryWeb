var slides = document.querySelectorAll('#slides .slide');
var currentSlide = 0;
var slideInterval = setInterval(nextSlide,2000);

function nextSlide(){
  slides[currentSlide].className = 'slide';
  currentSlide = (currentSlide+1)%slides.length;
  slides[currentSlide].className = 'slide showing';
}

function resize(id1,id2){
  var yourImg = document.getElementById(id1);
  if(yourImg && yourImg.style) {
    yourImg.style.height = '100px';
    yourImg.style.width = '200px';
}
}