let question = document.getElementById('questionBlock');
let author = document.getElementById('author')
let grandy = document.getElementById('grandy')
let map = document.getElementById("map")

function test(elt){
    /*info.innerText = question.value;
    const ul = document.getElementById('author');*/
    const url = 'http://127.0.0.1:5000/api/';

    var request = new Request(url, {
        method: 'POST',
        headers: new Headers(),
        body: question.value
    });

    fetch(request)
    .then((resp) => resp.json())
    .then(function(data) {
        /*grandy.appendChild(document.createTextNode('Haha'));*/
        let li = document.createElement('li');
        let span = document.createElement('span');
        author.appendChild(li)
        li.appendChild(span)
        span.innerText = data.formatted_address + ' (' + data.lat + ', ' + data.lng + ')'
        if ( map !== null ){
            map.style['height'] = '200px';
            initMap(data.lat, data.lng);}
        /*return {'data': question.value}*/
    })
    .catch(error => alert("Erreur : " + error));
}

function initMap(latitude, longitude) {
    new google.maps.Map(map, {
        center: {lat: latitude, lng: longitude},
        zoom: 13});
}