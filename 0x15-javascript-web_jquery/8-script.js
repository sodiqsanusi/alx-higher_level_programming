$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  for (let p = 0; p < data.count; p++) {
    $('UL#list_movies').append('<li>' + data.results[p].title + '</li>');
  }
});
