//console.log(GOOGLE_MAPS_KEY)
//import GOOGLE_MAPS_KEY from './sample.js';

var question = document.getElementById('questionBlock');
var response = document.getElementById('response');
var questionButton = document.getElementById("questionButton");
var map = document.getElementById("map");
var wikiLink = document.getElementById('wikiLink');

let attr_list = ['id', 'class', 'name', 'placeholder', 'autocomplete',
'rows', 'readonly', 'type', 'href', 'target']

function gdPy(){
    alert('coucou1')
    //alert(GOOGLE_MAPS_KEY)
    if (questionButton.hasAttribute('_counter') |
        question.value == '') return
    questionButton.setAttribute('_counter', 1)

    const url = 'http://127.0.0.1:5000/api/';
    document.getElementById("GOOGLE_URL").src =
    "https://maps.google.com/maps/api/js?key=AIzaSyDICnA0VqhMKNXJkwbZuWP26CMAedvYWVs&callback=initMap&libraries=&v=weekly"
    
    let request = new Request(url, {
        method: 'POST',
        headers: new Headers(),
        body: question.value
        })

    fetch(request)
    .then((resp) => resp.json())
    .then((data) => {
        alert('coucou2')

        response.innerText += data.papy_blabla[0]
        show(response);
    
        if ( map !== null & data.papy_blabla[1]){
            initMap(data.position);
            show(map);

            if (wikiLink !== null &
                data.papy_blabla[2] & 
                data.wiki_url !== undefined) {
                    wikiLink.setAttribute('href', data.wiki_url)
                    show(wikiLink)
            }
        }
        /*for (elt of test_copy.children) {
            console.log(elt.nodeName)
        }*/

        new_question = createNewBlock(question);
        question.setAttribute('readonly', 0)
        question = new_question

        response = createNewBlock(response);
        map = createNewBlock(map);
        wikiLink = createNewBlock(wikiLink);

        questionButton.removeAttribute('_counter');

    })
    .catch(error => alert("Erreur : " + error));
}

function show(cls){
    cls.style['display'] = 'block';
}

function hide(cls) {
    cls.style['display'] = 'none';
}

function createNewBlock(old_block) {
    let new_block = document.createElement(old_block.nodeName)

    /*for (data of old_block.attributes) {
        new_block.setAttribute(data.name, data.value)
    }*/

    for (data of attr_list) {
        if (old_block.hasAttribute(data)) {
            new_block.setAttribute(data, old_block.getAttribute(data))
        }
    }
    new_block.innerText = old_block.innerText

    old_block.parentElement.appendChild(new_block)
    return new_block
}


function initMap(position) {
    // show Map
    let google_plan = new google.maps.Map(map, {
        center: position,
        zoom: 13});

    // show Marker
    new google.maps.Marker({
    	position: position,
    	map: google_plan});
}