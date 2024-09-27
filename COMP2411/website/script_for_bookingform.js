function getUrlParameter(name) {
    name = name.replace(/[$$]/, '\\[').replace(/[$$]/, '\\]');
    const regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
    const results = regex.exec(location.search);
    return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
}

// Get the selected restaurant from the URL
const selectedRestaurant = getUrlParameter('restaurant');
console.log("Selected Restaurant in Booking Page:", selectedRestaurant); // Log the selected restaurant

const selectedRestaurantDisplay = document.getElementById('selectedRestaurantDisplay');
        if (selectedRestaurant) {
            selectedRestaurantDisplay.innerHTML = `<h2>You have selected: ${selectedRestaurant}</h2>`;
        } else {
            selectedRestaurantDisplay.innerHTML = `<h2>No restaurant selected.</h2>`};