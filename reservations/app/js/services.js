'use strict';

app.factory('reservation', function($http) {

  function getUrl(id) {
    id = typeof id !== 'undefined' ? id : '';
    return 'http://reservation-viewer.herokuapp.com/api/reservations/' + id + '?format=json';
  }

  return {
    get: function(id, callback) {
      return $http.get(getUrl(id)).success(callback);
    },
    query: function(page, page_size, callback) {
      return $http.get(getUrl() + '&page_size=' + page_size + '&page=' + page).success(callback);
    },
    save: function(reservation, callback) {
      return $http.post(getUrl(), reservation).success(callback);
    },
    remove: function(id, callback) {
      return $http.delete(getUrl(id)).success(callback);
    },
    put: function(reservation, callback) {
      return $http.put(getUrl(reservation.id), reservation).success(callback);
    }
  };
});
