$(function() {
	const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
	
	$.get(url, function(data) {
		data.results.forEach(function(movie) {
			$('#list_movies').append('<li>' + movie.title +'<li>';)
		});
	});
});
