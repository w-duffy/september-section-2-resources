console.log('Hello World!');

fetch('http://localhost:8004/players')
    .then((res) => res.json())
    .then((res) => res.players.map((el) => `${el.firstName} ${el.lastName}`))
    .then((res) => {
        const ul = document.getElementById('player-list');

        res.forEach((el) => {
            const li = document.createElement('li');
            li.innerText = el;

            ul.appendChild(li);
        });
    })
    .then((res) => console.log(res));
