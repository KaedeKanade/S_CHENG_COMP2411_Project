let selectedRestaurant = null; // Variable to store the selected restaurant

document.getElementById('bookNowBtn').addEventListener('click', function() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('active');
    document.body.classList.toggle('no-scroll'); 
});

const restaurants = document.querySelectorAll('.restaurant');
restaurants.forEach(restaurant => {
    restaurant.addEventListener('click', function() {
        restaurants.forEach(r => r.classList.remove('selected')); // Deselect all
        this.classList.add('selected'); // Select the clicked one
        selectedRestaurant = this.getAttribute('data-name');
    });
});

// Redirect to booking form page
document.getElementById('checkAvailabilityBtn').addEventListener('click', function() {
    window.location.href = `booking_form.html?restaurant=${selectedRestaurant}`; // Redirect to booking page
});

document.getElementById('closeSidebarBtn').addEventListener('click', function() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.remove('active'); // Remove active class to hide sidebar
    document.body.classList.remove('no-scroll');
});

