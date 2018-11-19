// Nav shrink
$(document).ready(function(){
  $(window).scroll(function(){
    if($(document).scrollTop() > 100){
      $('.navbar').addClass('shrink');
    }
    else{
      $('.navbar').removeClass('shrink');
    }
  });
});
