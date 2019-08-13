// $(document).ready(function() {
	
var map;
var faisalabad = {lat:52.449970, lng:-1.930870};
var navDest = "1.01, 1.01";
var mulGate = true;

function addYourLocationButton(map, marker) 
{
    var controlDiv = document.createElement('div');

    var firstChild = document.createElement('button');
    firstChild.style.backgroundColor = '#fff';
    firstChild.style.border = 'none';
    firstChild.style.outline = 'none';
    firstChild.style.width = '0.56rem';
    firstChild.style.height = '0.56rem';
    firstChild.style.borderRadius = '0.04rem';
    firstChild.style.boxShadow = '0 0.02rem 0.08rem rgba(0,0,0,0.3)';
    firstChild.style.cursor = 'pointer';
    firstChild.style.marginRight = '0.2rem'; //button's margin
    firstChild.style.padding = '0rem';
    firstChild.title = 'Your Location';
    controlDiv.appendChild(firstChild);

    var secondChild = document.createElement('div');
    secondChild.style.margin = '0.1rem';
    secondChild.style.width = '0.36rem';
    secondChild.style.height = '0.36rem';
    secondChild.style.backgroundImage = 'url(https://maps.gstatic.com/tactile/mylocation/mylocation-sprite-1x.png)';
    secondChild.style.backgroundSize = '3.6rem 0.36rem';
    secondChild.style.backgroundPosition = '0px 0px';
    secondChild.style.backgroundRepeat = 'no-repeat';
    secondChild.id = 'you_location_img';
    firstChild.appendChild(secondChild);

    google.maps.event.addListener(map, 'dragend', function() {
        $('#you_location_img').css('background-position', '0px 0px');
    });

    firstChild.addEventListener('click', function() {
        var imgX = '0';
        var animationInterval = setInterval(function(){
            if(imgX == '-18') imgX = '0';
            else imgX = '-18';
            $('#you_location_img').css('background-position', imgX+'px 0px');
        }, 500);
        if(navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var latlng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude); //定位之后的坐标
                marker.setPosition(latlng);
                map.setCenter(latlng);
                clearInterval(animationInterval);
                $('#you_location_img').css('background-position', '-144px 0px');
            });
        }
        else{
            clearInterval(animationInterval);
            $('#you_location_img').css('background-position', '0px 0px');
        }
    });

    controlDiv.index = 1;
    map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(controlDiv);
}


//Map style
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 16,
        center: faisalabad,
        mapTypeControl: false,
        streetViewControl: false,
        fullscreenControl: false,
        styles: [
		    {
		        "stylers": [
		            {
		                "saturation": -100
		            },
		            {
		                "gamma": 1
		            }
		        ]
		    },
		    {
		        "elementType": "labels.text.stroke",
		        "stylers": [
		            {
		                "visibility": "off"
		            }
		        ]
		    },
		    {
		        "featureType": "poi.business",
		        "elementType": "labels.text",
		        "stylers": [
		            {
		                "visibility": "off"
		            }
		        ]
		    },
		    {
		        "featureType": "poi.business",
		        "elementType": "labels.icon",
		        "stylers": [
		            {
		                "visibility": "off"
		            }
		        ]
		    },
		    {
		        "featureType": "poi.place_of_worship",
		        "elementType": "labels.text",
		        "stylers": [
		            {
		                "visibility": "off"
		            }
		        ]
		    },
		    {
		        "featureType": "poi.place_of_worship",
		        "elementType": "labels.icon",
		        "stylers": [
		            {
		                "visibility": "off"
		            }
		        ]
		    },
		    {
		        "featureType": "road",
		        "elementType": "geometry",
		        "stylers": [
		            {
		                "visibility": "simplified"
		            }
		        ]
		    },
		    {
		        "featureType": "water",
		        "stylers": [
		            {
		                "visibility": "on"
		            },
		            {
		                "saturation": 50
		            },
		            {
		                "gamma": 0
		            },
		            {
		                "hue": "#50a5d1"
		            }
		        ]
		    },
		    {
		        "featureType": "administrative.neighborhood",
		        "elementType": "labels.text.fill",
		        "stylers": [
		            {
		                "color": "#333333"
		            }
		        ]
		    },
		    {
		        "featureType": "road.local",
		        "elementType": "labels.text",
		        "stylers": [
		            {
		                "weight": 0.5
		            },
		            {
		                "color": "#333333"
		            }
		        ]
		    },
		    {
		        "featureType": "transit.station",
		        "elementType": "labels.icon",
		        "stylers": [
		            {
		                "gamma": 1
		            },
		            {
		                "saturation": 50
		            }
		        ]
		    }
		]
    });

    //MY LOCATION
    var myMarker = new google.maps.Marker({
        map: map,
        animation: google.maps.Animation.DROP,
        //position: faisalabad
    });

    addYourLocationButton(map, myMarker);



    //DIRECTION SERVICE
	var directionsService = new google.maps.DirectionsService;
	var directionsDisplay = new google.maps.DirectionsRenderer;
	directionsDisplay.setMap(map);
	var onChangeHandler = function() {
    calculateAndDisplayRoute(directionsService, directionsDisplay);
    };

    //GATE POP-UP START
    //$("#building").change(function() {
    document.getElementById('building').addEventListener('change',function(){
    	// javascript
		// if (document.getElementById('building').value === '52.449216, -1.931401'){
		// 	$("#panel").fadeOut();
		// 	}

		// jquery if
		// if ($("#building").val('52.449216, -1.931401')){
		//  	$("#gatePop").animate({bottom:'0'});
		//  	break;
		// }

		switch ($("#building").val()){
			case ("AstonWebbBBlock"):
				mulGate = true;

				$("#gatePop").animate({bottom:'0'});
				$("#gateA").click(function(){
					navDest = "52.449216, -1.931401";
				});
				document.getElementById('gateA').addEventListener('click',onChangeHandler);
				$("#gateB").click(function(){
					navDest = "52.449216, -1.929126";
				});
				document.getElementById('gateB').addEventListener('click',onChangeHandler);
				break;

				// if($("#gateA").click()){
				// 	//$("#gateA").click(function(){
				// 	navDest = "52.449216, -1.931401";
				// 	//});
				// 	document.getElementById('gateA').addEventListener('click',onChangeHandler)
				// }else if($("#gateB").click()){
				// 	navDest = "52.450322, -1.929126"
				// 	document.getElementById('gateB').addEventListener('click',onChangeHandler)
				// }
				
			case ("AstonWebbGreatHall"):
				mulGate = true;
				navDest = "52.449093, -1.930821"
				$("#gatePop").animate({bottom:'-3rem'},onChangeHandler);
				break;
			case ("WatsonBuilding"):
				mulGate = false;
				navDest = "52.450322, -1.929126"
				$("#gatePop").animate({bottom:'-3rem'},onChangeHandler);
				break;
			case ("StaffHouse"):
				$("#gateA").append("<img id='staffhouse1' src='../img/staffhouse1.png'/>")
				$("#gatePop").animate({bottom:'0'});
				$("#gateA").click(function(){
					navDest = "52.450400, -1.932921";
				});
				document.getElementById('gateA').addEventListener('click',onChangeHandler);
				$("#gateB").click(function(){
					navDest = "52.450541, -1.931957";
				});
				document.getElementById('gateB').addEventListener('click',onChangeHandler);
				break;
		}

	}); //GATE POP-UP END




	// var onChangeHandler = function() {
 //          calculateAndDisplayRoute(directionsService, directionsDisplay);
 //        };
        //document.getElementById('building').addEventListener('change', onChangeHandler);
        //if this building is a multi gate building
        //document.getElementById('gateA').addEventListener('click', onChangeHandler)
        
        // if (mulGate === true) {
        // 	document.getElementById('gateA').addEventListener('click', onChangeHandler);
        // } else {
        // 	document.getElementById('building').addEventListener('change', onChangeHandler);
        // }
    }


    function calculateAndDisplayRoute(directionsService, directionsDisplay) {
    	
    	//GET CURRENT LOCATION
    	navigator.geolocation.getCurrentPosition(function(position) {
    		//CREATE A VAR FOR CURRENT LOCATION
			var latlng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
			
	        //DIRECTIONS SERVICE
	        directionsService.route({
	          origin: latlng,
	          destination: navDest,//document.getElementById('building').value,//GET OPTIONS FROM HTML
	          travelMode: 'WALKING'
	        }, function(response, status) {
	          if (status === 'OK') {
	            directionsDisplay.setDirections(response);
	          } else {
	            window.alert('Directions request failed due to ' + status);
	          }
	      });
      });
    }

//GATE SELECT
// function gateSelect() {
// 	if (document.getElementById('building').value === '52.449216, -1.931401'){
// 		$("#panel").fadeOut();
// 	}
// }




// $(document).ready(function(e) {
//     initMap();
// });


		// });