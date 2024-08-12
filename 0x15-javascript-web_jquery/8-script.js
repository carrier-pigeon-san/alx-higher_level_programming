const address = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(address, function (content) {
  for (const film of content.results) {
    $('UL#list_movies').append(`<li>${film.title}</li>`);
  }
});
