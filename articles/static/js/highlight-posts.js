$(document).ready(function(){
		$('.onepost').hover(function(event){
			$(event.currentTarget).find('.one-post-shadow').animate({opacity:'0.9'},300);
		}, function(event){
			$(event.currentTarget).find('.one-post-shadow').animate({opacity:'0'},300);
});
});