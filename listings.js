document.addEventListener('DOMContentLoaded', function (event) {
    document.getElementById('myForm').addEventListener('submit', function (e) {
        e.preventDefault(); // Prevent the default form submission

        const address = document.getElementById('enter-address').value;
        const url = new URL('http://localhost:5000/get-rows');
        url.searchParams.append('address', address);

        fetch(url, {
            method: 'GET'
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            // Handle success here (e.g., display a success message)
        })
        .catch((error) => {
            console.error('Error:', error);
            // Handle errors here (e.g., display an error message)
        });
    });
});
