    function initMap() {
        var uluru = {lat: 63.418110, lng: 10.405579};
        var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 17,
        center: uluru
        });
        var marker = new google.maps.Marker({
        position: uluru,
        map: map
        });
    }
