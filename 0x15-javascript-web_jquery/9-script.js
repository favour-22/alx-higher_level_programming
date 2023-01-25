$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, status) {
  $('DIV#hello').html(data.hello);
});
