let question = document.getElementById('questionBlock');

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
    /*.then((resp) => resp.json())*/
    /*.then(function(data) {
        /*let li = document.createElement('li');
        let span = document.createElement('span');
        li.appendChild(span);
        span.innerText = question.value;
        ul.appendChild(li);
        alert(question.value)
        return {'data': question.value}
    })*/
    .catch(error => alert("Erreur : " + error));
}

