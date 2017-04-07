$(document).ready(function(){

  /* Home Page Slider */
  var owl = $('.homepage-carousel');
  owl.owlCarousel({
    items: 1,
    margin: 0,
    loop: true,
    autoHeight:true,
    autoplay:false,
    autoplayTimeout:7000,
    autoplayHoverPause:false,
    nav:true,
    dots: true,
    navText: [
      "<i class='fa fa-arrow-left'></i>",
      "<i class='fa fa-arrow-right'></i>"
    ],
    navContainer: '.owl-nav',
    dotsContainer: '.owl-dots'
  });


  /* Home Page Slider */
  var owl = $('.testimonials-carousel');
  owl.owlCarousel({
    items: 1,
    margin: 0,
    loop: true,
    autoHeight:true,
    autoplay:false,
    autoplayTimeout:7000,
    autoplayHoverPause:false,
    nav:true,
    dots: true,
    navText: [
      "<i class='fa fa-arrow-left'></i>",
      "<i class='fa fa-arrow-right'></i>"
    ],
    navContainer: '.owl-nav',
    dotsContainer: '.owl-dots'
  });

  // Custom Language Switcher with Flags
  $('#language-options').flagStrap({
    countries: {
      "US": "English",
      "FR": "French",
      "DE": "Deutch"
    },
    placeholder: {
      value: "",
      text: "Please select your language"
    },
    buttonSize: "btn-md",
    buttonType: "btn-custom",
    labelMargin: "10px",
    scrollable: false,
    scrollableHeight: "350px"
  });

  $('#language-options-mobile').flagStrap({
    countries: {
      "US": "English",
      "FR": "French",
      "DE": "Deutch"
    },
    placeholder: {
      value: "",
      text: "Please select your language"
    },
    buttonSize: "btn-md",
    buttonType: "btn-custom",
    labelMargin: "10px",
    scrollable: false,
    scrollableHeight: "350px"
  });

  $('.language-options').flagStrap({
    countries: {
      "US": "English",
      "FR": "French",
      "DE": "Deutch"
    },
    placeholder: {
      value: "",
      text: "Country"
    },
    buttonSize: "btn-md",
    buttonType: "btn-custom-register",
    labelMargin: "10px",
    scrollable: false,
    scrollableHeight: "350px"
  });


  $('.country-options').flagStrap({
    countries: {
      "Ke": "Kenya",
      "US": "US",
      "Fr": "France"
    },
    placeholder: {
      value: "",
      text: "Country"
    },
    buttonSize: "btn-md",
    buttonType: "btn-custom-register",
    labelMargin: "10px",
    scrollable: false,
    scrollableHeight: "350px"
  });


  $('#country-selection').flagStrap({
    countries: {
      "Ke": "Kenya",
      "US": "US",
      "Fr": "France"
    },
    placeholder: {
      value: "",
      text: ""
    },
    buttonSize: "btn-md",
    buttonType: "btn-custom",
    labelMargin: "10px",
    scrollable: false,
    scrollableHeight: "350px"
  });

  // Change Layout based on width size
  $(window).on("load resize",function(e){
    if ($(window).width() <= 991) {
      // if window is small than 991px, update footer layout
      $(".moveMe").insertAfter('.mobile-target');

    } else {
      // otherwise leave it default
      $(".moveMe").appendTo('.download-app');
    }
  }).resize();


});
