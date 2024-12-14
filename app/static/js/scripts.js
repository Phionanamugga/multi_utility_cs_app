document.addEventListener('DOMContentLoaded', function () {
    console.log('Document is ready!');
    const toggleButton = document.getElementById('toggleButton');
    if (toggleButton) {
        toggleButton.addEventListener('click', function () {
            alert('Button clicked!');
        });
    }
});
