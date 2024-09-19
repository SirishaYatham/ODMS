// new_organ_donation.js

document.addEventListener('DOMContentLoaded', function() {
    const donorForm = document.getElementById('donorForm');
    
    donorForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(donorForm);

        fetch(donorForm.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Donor information submitted successfully!');
                // Optionally, redirect or update the page
                window.location.href = data.redirect_url;

            } else {
                alert('An error occurred: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
