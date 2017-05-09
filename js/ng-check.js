(function() {
'use strict'

angular.module('check', []).controller('ctrl', ctrl)
.config(['$sceDelegateProvider', function($sceDelegateProvider) {
  $sceDelegateProvider.resourceUrlWhitelist([
    'self',
    'https://www.ulmart.ru/**'
  ]);
}]);

ctrl.$inject = ['$http'];
function ctrl($http) {
  angular.element('noindex a').each(function() {
    var href = angular.element(this).attr('href');
    if (href.indexOf('ulmart') !== -1) {
      var href = href.slice(16);
      $http.jsonp(href, {jsonpCallbackParam: 'dataLayer'}).then(function(response) {
        console.log(response);
      }, function(response) {
        console.log(response);
      })
    }
  })
}

})();
