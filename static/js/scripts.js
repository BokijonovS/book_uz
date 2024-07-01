/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    var form = event.target;
    var formData = new FormData(form);

    fetch(form.action, {
        method: form.method,
        body: formData,
        headers: {
            'Accept': 'application/json'
        }
    }).then(function(response) {
        if (response.ok) {
            // Form was submitted successfully, refresh the page
            alert("Form successfully submitted!"); // Optional: Show a success message
            window.location.reload();
        } else {
            return response.json().then(function(data) {
                throw new Error(data.error || 'Form submission failed');
            });
        }
    }).catch(function(error) {
        console.error('Error:', error);
        alert('There was an error submitting the form. Please try again.');
    });
});
