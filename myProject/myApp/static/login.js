document.addEventListener('DOMContentLoaded', function() {
    var userloginForm = document.querySelector('#userLoginForm');
    var adminloginForm = document.querySelector('#adminLoginForm');

    var userErrorContainer = document.querySelector('#userErrorContainer');
    var adminErrorContainer = document.querySelector('#adminErrorContainer');

    const toggleRegisterAdminPassword = document.getElementById('toggleRegisterAdminPassword');
    const registerInputAdmin = document.getElementById('registerInputAdmin');

    toggleRegisterAdminPassword.addEventListener('click', function() {
        const type = registerInputAdmin.getAttribute('type') === 'password' ? 'text' : 'password';
        registerInputAdmin.setAttribute('type', type);
        this.classList.toggle('fa-eye-slash');
    });

    const toggleRegisterUserPassword = document.getElementById('toggleRegisterUserPassword');
    const registerInputUser = document.getElementById('registerInputUser');

    toggleRegisterUserPassword.addEventListener('click', function() {
        const type = registerInputUser.getAttribute('type') === 'password' ? 'text' : 'password';
        registerInputUser.setAttribute('type', type);
        this.classList.toggle('fa-eye-slash');
    });

    

    if (userloginForm && userErrorContainer) {
        userloginForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the form from submitting normally
            
            console.log('User form submitted');
            // Move the error container to the user container
            document.querySelector('.login-page-user-container').appendChild(userErrorContainer);

            // Get the form data
            var formData = new FormData(userloginForm);
            
            // Make a POST request to the login endpoint
            fetch('/login/', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json()) // Parse the JSON response
            .then(data => {
                if (data.success) {
                    // Redirect to the specified URL on successful login
                    window.location.href = data.redirect_url;
                } else {
                    // Display the error message in the user error container
                    userErrorContainer.innerText = data.error;
                }
            })
            .catch(error => {
                console.error('Error:', error);
                userErrorContainer.innerText = 'An error occurred. Please try again later.';
            });
        });
    }

    if (adminloginForm && adminErrorContainer) {
        adminloginForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the form from submitting normally
            
            console.log('Admin form submitted');
            // Move the error container to the admin container
            document.querySelector('.login-page-admin-container').appendChild(adminErrorContainer);

            // Get the form data
            var formData = new FormData(adminloginForm);
            
            // Make a POST request to the login endpoint
            fetch('/login/', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json()) // Parse the JSON response
            .then(data => {
                if (data.success) {
                    // Redirect to the specified URL on successful login
                    window.location.href = data.redirect_url;
                } else {
                    // Display the error message in the admin error container
                    adminErrorContainer.innerText = data.error;
                }
            })
            .catch(error => {
                console.error('Error:', error);
                adminErrorContainer.innerText = 'An error occurred. Please try again later.';
            });
        });
    }
});
