// Execute the function after the DOM is fully loaded
$(function(){

	$('DIV#red_header').on('click', function(){
		$('header').addClass('red');
	});
});
