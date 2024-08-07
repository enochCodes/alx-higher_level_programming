$(function() {
	const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
	
	$.get(url, function(data) {
		const helloMessage = data.hello;
		$('#hello').text(helloMessage);
	});
});
