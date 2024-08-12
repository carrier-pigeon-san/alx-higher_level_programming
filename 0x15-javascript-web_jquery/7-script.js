const address = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.get(address, function (content) {
  $('#character').text(content.name);
});
