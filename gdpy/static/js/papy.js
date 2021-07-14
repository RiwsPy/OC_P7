var question = document.getElementById('questionBlock');
var response = document.getElementById('response');
var questionButton = document.getElementById("questionButton");
var map = document.getElementById("map");
var wikiLink = document.getElementById('wikiLink');
var loader = document.getElementById('loader');

let attr_list = ['id', 'class', 'name', 'placeholder', 'autocomplete',
'rows', 'readonly', 'type', 'href', 'target', 'spellcheck']

function gdPy(){
    //alert('coucou1')
    if (questionButton.hasAttribute('_counter') |
        question.value == '') return
    questionButton.setAttribute('_counter', 1)

    let request = new Request('/api/', {
        method: 'POST',
        headers: new Headers(),
        body: question.value
        })
    show(loader)

    fetch(request)
    .then((resp) => resp.json())
    .then((data) => {
        //alert('coucou2')
        hide(loader)
        response.innerText += data.papy_blabla
        show(response);
    
        if ( map !== null & data.found_place){
            initMap(data.position);
            show(map);

            if (wikiLink !== null &
                data.found_wiki & 
                data.wiki_url !== undefined) {
                    wikiLink.setAttribute('href', data.wiki_url);
                    show(wikiLink);
            }
        }
        new_question = createNewBlock(question);
        question.setAttribute('readonly', 0)
        question = new_question

        response = createNewBlock(response);
        map = createNewBlock(map);
        wikiLink = createNewBlock(wikiLink);

        questionButton.removeAttribute('_counter');
    })
    .catch((error) => {
        hide(loader)
        alert("Erreur : " + error)});
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