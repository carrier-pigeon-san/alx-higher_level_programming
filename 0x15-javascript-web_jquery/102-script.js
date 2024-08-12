$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    const language = $('INPUT#language_code').val();
    const address = `https://hellosalut.stefanbohacek.dev/?lang=${language}`;

    $.get(address, function (content) {
      $('DIV#hello').text(content.hello);
    });
  });
});
