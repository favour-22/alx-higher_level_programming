$.get('https://swapi.co/api/films/?format=json', function (data, status) {
  let i = 0;
  while (i < data.count) {
    $('UL#list_movies').append('<li>' + data.results[i].title + '</li>');
    i++;
  }
});
