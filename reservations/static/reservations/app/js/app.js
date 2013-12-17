'use strict';

var app = angular.module('pgApp', []);

app.config(function ($routeProvider) {
  $routeProvider
    .when('/home',
      {
        templateUrl: 'static/reservations/app/partials/home.html'
      })
    .when('/reservations',
      {
        controller: 'ReservationListController',
        templateUrl: 'static/reservations/app/partials/reservations.html'
      })
    .when('/reservations/:reservationId',
      {
        controller: 'ReservationDetailController',
        templateUrl: 'static/reservations/app/partials/reservation.html'
      })
    .when('/about',
      {
        templateUrl: 'static/reservations/app/partials/about.html'
      })
    .otherwise({ redirectTo: '/home' });
});
