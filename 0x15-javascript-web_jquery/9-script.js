$(document).ready(function() {
  $.ajax({
    url: "https://fourtonfish.com/hellosalut/?lang=fr",
    type: "GET",
    dataType: "jsonp",
    success: function(data) {
      $("DIV#hello").text(data.hello);
    },
    error: function(jqXHR, textStatus, errorThrown) {
      console.log(textStatus, errorThrown);
    }
  });
});
