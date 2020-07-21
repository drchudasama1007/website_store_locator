odoo.define('website_store_locater.google_map', function(require) {
    'use strict';
    var rpc = require('web.rpc');
    var core = require('web.core');
    var markers = [0];
    var currentInfoWindow = null;
    var map_key = null;
    var _t = core._t;
    var _lt = core._lt;
    var QWeb = core.qweb;

    $(document).ready(function() {
        rpc.query({
            route: '/map/key',
            async:false,
        }).then(function(key) {
            if(key){
                $.getScript('//maps.googleapis.com/maps/api/js?key='+key+'&libraries=places').then(function() {
                    myMap();
                });
            }
            else{
                  alert("Please add gmap_api_key parameter with Google Map API Key value in system parameters.");
            }

        })
    });

    function myMap() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition);
        } else {
            x.innerHTML = "Geolocation is not supported by this browser.";
        }
    }

    function showPosition(position) {
        var myLatLng = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        };
        var map = new google.maps.Map(document.getElementById('googleMap'), {
            zoom: 5,
            center: myLatLng
        });
        const card = document.createElement('div');
        const titleBar = document.createElement('div');
        const title = document.createElement('div');
        const container = document.createElement('div');
        const defaultBounds = new google.maps.LatLngBounds();
        const options = {
            types: ['(cities)'],
        };
        card.appendChild(titleBar);
        card.appendChild(container);
        map.controls[google.maps.ControlPosition.TOP_RIGHT].push(card);
         var store_country_id = parseInt($('#store_country_id').val())
        rpc.query({
            route: '/store/location',
            params: {'store_country_id':store_country_id}
        }).then(function(locations) {
            var locators = $('.map_locator');
            var infowindow = new google.maps.InfoWindow();
            for (var i = 0; i < locations.length; i++) {
                rpc.query({
                    route: '/store/locator/marker',
                    params: {
                        'id': locations[i][5],
                        'i': i+1
                    }
                }).then(function(markersid) {});
                var uluru = {
                    lat: parseFloat(locations[i][0]),
                    lng: parseFloat(locations[i][1])
                };
                $(locators[i]).attr('data-markerid', i+1);

                var marker = new google.maps.Marker({
                    position: uluru,
                    map: map,
//                    icon: icon,
                });
                var contentString =
                    '<div id="content">' +
                    '<div id="siteNotice">' +
                    '<div class="container" style="width:200px !important;padding-bottom: 10px;">' +
                    '<span style="font-weight: 600;">' + locations[i][2] + '</span>' +
                    '</div>' +
                    '<div class="container" style="width:200px!important;padding-bottom: 10px;  ">' +
                    '<span style="font-weight: 600;">' + locations[i][3] + '</span>' +
                    '</div>' +
                    '<div class="container" style="width:200px !important;">' +
                    '<span style="font-weight: 600;">Phone: ' + locations[i][4] + '</span>' +
                    '</div>' +
                    '</div>' +
                    '</div>';

                var infowindow = new google.maps.InfoWindow({
                    content: contentString
                });
                google.maps.event.addListener(marker, 'click', (function(marker, infowindow) {
                    return function() {
                        if (currentInfoWindow != null) {
                            currentInfoWindow.close();
                        }
                        infowindow.open(map, marker);
                        currentInfoWindow = infowindow
                    };
                })(marker, infowindow));
                markers.push(marker);
            }
        });

        $(document).on('click', '.map_locator', function() {
            map.setZoom(12);
            google.maps.event.trigger(markers[$(this).data('markerid')], 'click');
            $('#search_place').val('')
            $('.product_main_div').hide()
            $( ".map_locator" ).each(function( index ) {
              $(this).css('background', 'white');
            });
            $(this).css('background', '#f5b5b5');
        });

        $(document).on('click', '.main_address', function() {
            $( ".main_address" ).each(function( index ) {
              $(this).css('color', '#ae8e59');
            });
            $(this).css('color', 'black');
        });


//        $(document).on('click', function() {
//            $('html, body').animate({
//                scrollTop: $(".map_location").offset().top
//            }, 100);
//        });

        $("#search_place").keyup(function(){
        var product_search = $('#search_place').val()
        var store_country_id = parseInt($('#store_country_id').val())
        rpc.query({route: '/advance_search_place',
            params:{
                product_search:product_search,
                store_country_id:store_country_id,
            },
        }).then(function(products) {
            var search = $('.search-query')
            if(products){
                $('#product_search_results').html(products);
            }
        });
    });

    }

});