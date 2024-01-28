document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('priceInput').addEventListener('input', function(e) {
        var value = e.target.value;
        
        // Replace non-numeric characters (excluding the decimal point)
        value = value.replace(/[^\d.]/g, '');

        // Update the value of the input field
        e.target.value = value;
    });

    document.getElementById('myForm').addEventListener('submit', function(e) {
        e.preventDefault(); // Prevent the default form submission
        // location.href = "index.html";
    });
});

function submitForm(event) {
    event.preventDefault(); // Prevents the default form submission

    const form = document.getElementById('myForm');
    const formData = new FormData(form);
    const jsonData = {};

    console.log("Form Data Entries:");
    let address = "";
    for (let [key, value] of formData.entries()) {
        if (key == "street" || key == "area_code" || key == "city" || key == "state") {
            address += value + " "
            console.log(address)
        }
        
        else {
            console.log(key, value);
            jsonData[key] = value;
        }   
    }
    jsonData["address"] = address;

    console.log("JSON Data:", jsonData);
    // Call the function to handle the HTTP request
    sendFormData(jsonData);
}


function sendFormData(data) {
    fetch('http://localhost:5000/insert-row', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

