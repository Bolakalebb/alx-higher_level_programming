$(document).ready(function() {
  function translateHello() {
    let languageCode = $('#language_code').val();
    let url = `https://fourtonfish.com/hellosalut/?lang=${languageCode}`;
    $.get(url, function(data) {
      $('#hello').text(data.hello);
    });
  }
  $('#btn_translate').click(translateHello);
  $('#language_code').keypress(function(event) {
    if (event.keyCode === 13) {
      translateHello();
    }
  });
});
