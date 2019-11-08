
// var vCenter = [40, 53]; 				// Mediterranean center
var vCenter = [40.78, -73.9602]; 	// ISAW center

// Initialize Leaflet map object
var map = L.map( 'mapid', {
	center: vCenter,
	zoom: 3,
	minZoom: 3,
	maxZoom: 22,
	zoomControl: false
});

// Adds the actual visual components of the map
// This one uses satellite imagery
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
	maxZoom: 22,
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
		'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
		'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
	id: 'mapbox.satellite'
}).addTo(map);
// This one uses terrain imagery
// L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiaXNhd255dSIsImEiOiJBWEh1dUZZIn0.SiiexWxHHESIegSmW8wedQ', {
//  attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
//  maxZoom: 28,
//  id: 'isawnyu.map-knmctlkh',
//  accessToken: 'pk.eyJ1IjoiZGl5Y2xhc3NpY3MiLCJhIjoiY2ozdW1uenYzMDFjejJxbzR2enBha3p6byJ9.0llqVkuLQVBkHA-T2G3c2Q'
//  }).addTo(map);

// Adds the button to zoom out and center or "show all"
//map.addControl( new L.Control.ZoomMin() );