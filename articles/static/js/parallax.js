$(document).ready(function(){
	var scrolled = 0;
	var $parallaxElements=$('.icons-for-parallax img');
	var $parallaxImg=$('#logo');
	$(window).scroll(function(){
		scrolled = $(window).scrollTop();
		for (var i=0; i<$parallaxElements.length;i++){
			yPosition = (scrolled * 0.15*(i+1));
			$parallaxElements.eq(i).css({top:yPosition});
		};
		for (var i=0; i<$parallaxImg.length;i++){
			yPositionImg = (scrolled * 0.5*(i+1));
			$parallaxImg.eq(i).css({top:yPositionImg});
		};
	});
});