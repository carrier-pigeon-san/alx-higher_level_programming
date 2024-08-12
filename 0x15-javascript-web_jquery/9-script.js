$(document).ready(function () {
  const address = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  $.get(address, function (content) {
    $('DIV#hello').text(content.hello);
  });
});
