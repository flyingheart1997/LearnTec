jQuery(document).ready(function(){
	"use strict"
	  $('.slider').ripples({
      dropRadius: 11,
      perturbance: .1,
     
	});
	  $(".text").typed({
	  	strings:["<strong class='primary1'>Hi I am</strong><strong class='primary'> koushik...!</strong>","<strong class='primary'>Welcome To...!</strong>","<strong class='primary1'> Learn Tech...!</strong>","<strong class='primary1'>Use Your</strong><strong class='primary2'> Own..!</strong>","<strong class='primary2'>Have a</strong><strong class='primary1'> Grate</strong> <strong>Day..</strong><strong class='primary1'>!</strong>"],
	  	typespeed:50,
	  	loop:true,
	});

      $('.').magnificPopup({
        delegate: 'enviournment-wrap', // child items selector, by clicking on it popup will open
        type: 'image',
        gallery: {
        enabled: true
       },
     });
    
});





