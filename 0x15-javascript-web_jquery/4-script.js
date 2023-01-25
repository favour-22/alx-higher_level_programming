$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    const myClass = $('HEADER').attr('class');
    if (myClass === 'green') {
      $('HEADER').removeClass('green');
      $('HEADER').addClass('red');
    } else {
      $('HEADER').removeClass('red');
      $('HEADER').addClass('green');
    }
  });
});
