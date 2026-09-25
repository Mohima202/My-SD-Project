

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('job-application-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        if (validateForm()) {
            alert('Form submitted successfully!');
            form.reset();  
        }
    });

    function validateForm() {
        let isValid = true;
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;
        const education = document.getElementById('education').value;
        const experience = document.getElementById('experience').value;

  
        clearErrors();

   
        if (name.trim() === '') {
            showError('name', 'Name is required.');
            isValid = false;
        }

 
        if (!validateEmail(email)) {
            showError('email', 'Please enter a valid email address.');
            isValid = false;
        }

 
        if (!validatePhone(phone)) {
            showError('phone', 'Please enter a valid phone number.');
            isValid = false;
        }


        if (education.trim() === '') {
            showError('education', 'Education is required.');
            isValid = false;
        }

      
        if (experience.trim() === '') {
            showError('experience', 'Work experience is required.');
            isValid = false;
        }

        return isValid;
    }

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }

    function validatePhone(phone) {
        const re = /^\d{10}$/;  
        return re.test(String(phone));
    }

    function showError(fieldId, message) {
        const field = document.getElementById(fieldId);
        const error = document.createElement('div');
        error.className = 'error-message';
        error.innerText = message;
        field.parentNode.insertBefore(error, field.nextSibling);
    }

    function clearErrors() {
        const errorMessages = document.querySelectorAll('.error-message');
        errorMessages.forEach(function(error) {
            error.remove();
        });
    }
});
