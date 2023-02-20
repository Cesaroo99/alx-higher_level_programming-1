$.get('https://swapi.co/api/films/?format=json', function (data) {
	$('UL#list_movies').append(...ada.results.map(movie => '<li>${movie.title}</li>'));
});
