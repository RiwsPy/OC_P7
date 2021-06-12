var question = document.getElementById('questionBlock');
var response = document.getElementById('responseBlock')
var questionButton = document.getElementById("questionButton")
var map = document.getElementById("map")
var test_copy = document.getElementById("test_copy")

let attr_list = ['id', 'class', 'name', 'placeholder', 'autocomplete',
'autofocus', 'required', 'rows', 'readonly', 'type', 'onClick', 'height', 'width']

document.getElementById("GOOGLE_URL").src =
    "https://maps.google.com/maps/api/js?key=AIzaSyDICnA0VqhMKNXJkwbZuWP26CMAedvYWVs&callback=initMap&libraries=&v=weekly"

function test(){
    // alert('coucou1')
    const url = 'http://127.0.0.1:5000/api/';

    var request = new Request(url, {
        method: 'POST',
        headers: new Headers(),
        body: question.value
    });

    fetch(request)
    .then((resp) => resp.json())
    .then((data) => {
        // alert('coucou2')
        response.style['display'] = 'inline-block';
        questionButton.style['display'] = 'none';
        response.innerHTML += data.papy_blabla

        if ( map !== null & (data.lat != 0 | data.lng != 0)){
            map.style['height'] = '200px';
            initMap(data.lat, data.lng);}
        
        question = createNewBlock("textarea", question);
        questionButton = createNewBlock("button", questionButton);
        response = createNewBlock("textarea", response);
        map = createNewBlock('div', map)
    })
    .catch(error => alert("Erreur : " + error));
}


function createNewBlock(cls, old_block) {
    let new_block = document.createElement(cls)
    for (let data of attr_list) {
        if (old_block.hasAttribute(data)) {
            new_block.setAttribute(data, old_block.getAttribute(data))
        }
    }
    if (cls == 'textarea') {
        old_block.setAttribute("readonly", "")
    }
    else if (cls == 'button') {
        new_block.innerText = 'GO'
    }

    test_copy.appendChild(new_block)
    return new_block
}


function initMap(latitude, longitude) {
    let location = {lat: latitude, lng: longitude};
    let google_plan = new google.maps.Map(map, {
        center: location,
        zoom: 13});

    // google Marker
    new google.maps.Marker({
    	position: location,
    	map: google_plan,
    });
}