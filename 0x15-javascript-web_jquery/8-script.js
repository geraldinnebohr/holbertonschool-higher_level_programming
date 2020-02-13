$(() => {
  $.get('https://swapi.co/api/films/?format=json', (data) => {
    const results = data.results;
    results.forEach((result) => {
      if (result.title) {
        $('#list_movies').append('<li>' + result.title + '</li>');
      }
    });
  });
});
