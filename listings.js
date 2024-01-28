document.addEventListener('DOMContentLoaded', function (event) {
    document.getElementById('myForm').addEventListener('submit', function (e) {
        e.preventDefault();

        fetch('http://localhost:5000/get-rows')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const container = document.getElementById('cardsContainer');
            container.innerHTML = '';

            data.forEach(item => {
                const card = createCard(item);
                container.appendChild(card);
            });
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
    });
});

function createCard(item) {
    const card = document.createElement('div');
    card.className = 'card';

    // Access tuple elements by their index
    const firstName = document.createElement('h3');
    firstName.textContent = item[0];

    const lastName = document.createElement('h4');
    lastName.textContent = item[1];

    const address = document.createElement('p');
    address.textContent = item[2];

    const price = document.createElement('p');
    price.textContent = 'Price: $' + item[3];

    const parkingType = document.createElement('p');
    parkingType.textContent = 'Type: ' + item[4];

    const contact = document.createElement('p');
    contact.textContent = 'Contact: ' + item[5];

    // Append elements to card
    card.appendChild(firstName);
    card.appendChild(lastName);
    card.appendChild(address);
    card.appendChild(price);
    card.appendChild(parkingType);
    card.appendChild(contact);

    return card;
}
