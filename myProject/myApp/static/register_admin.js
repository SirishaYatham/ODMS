document.addEventListener('DOMContentLoaded', (event) => {
    const password = document.getElementById('registerInputAdmin');
    const confirmPassword = document.getElementById('registerInputAdminRecheck');
    const passwordMatchMsg = document.getElementById('passwordMatch');

    confirmPassword.addEventListener('input', function() {
        if (password.value !== confirmPassword.value) {
            passwordMatchMsg.innerHTML = "Passwords do not match";
            passwordMatchMsg.style.color = "red";
        } else {
            passwordMatchMsg.innerHTML = "Passwords match";
            passwordMatchMsg.style.color = "green";
        }
    });
    const toggleRegisterPassword = document.getElementById('toggleRegisterPassword');
    const registerInputAdmin = document.getElementById('registerInputAdmin');
    const toggleRegisterPasswordRecheck = document.getElementById('toggleRegisterPasswordRecheck');
    const registerInputAdminRecheck = document.getElementById('registerInputAdminRecheck');

    toggleRegisterPassword.addEventListener('click', function() {
        const type = registerInputAdmin.getAttribute('type') === 'password' ? 'text' : 'password';
        registerInputAdmin.setAttribute('type', type);
        this.classList.toggle('fa-eye-slash');
    });

    toggleRegisterPasswordRecheck.addEventListener('click', function() {
        const type = registerInputAdminRecheck.getAttribute('type') === 'password' ? 'text' : 'password';
        registerInputAdminRecheck.setAttribute('type', type);
        this.classList.toggle('fa-eye-slash');
    });
});
    
function validateForm() {
    const phoneInput = document.getElementById('phNum').value;
    const dobInput = document.getElementById('dob').value;
    const successMsg = document.getElementById('regPageSuccessMsg');
    const today = new Date();
    const dob = new Date(dobInput);
    const age = today.getFullYear() - dob.getFullYear();
    const monthDiff = today.getMonth() - dob.getMonth();

    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < dob.getDate())) {
        age--;
    }

    // Reset success message
    successMsg.innerHTML = '';

    // Validate phone number length
    if (phoneInput.length !== 10) {
        alert("Phone number must be 10 digits.");
        return false;
    }

    // Validate age
    if (age < 18) {
        alert("You must be at least 18 years old to register.");
        return false;
    }

    // If all validations pass, show success message
    successMsg.innerHTML = "Successfully registered";
    successMsg.style.color = "green";
    return true;
};
