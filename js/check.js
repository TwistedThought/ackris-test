(function() {

'use strict'

var data = {}
var $this = []

$('noindex a').each(function(index) {
  var href = $(this).attr('href');
  var href = href.slice(16);
  $this[index] = $(this);
  data[index] = href;
});

$.post('/check_goods/', data, function(response) {
  for (var variable in response) {
    if (response[variable] === false) {
      $this[variable].parent().css('display', 'none');
    }
  }
}, 'json');

})();
