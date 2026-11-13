document.addEventListener("DOMContentLoaded", function() {
    const venueHeader = document.getElementById('venueName');
    const hiddenInput = document.getElementById('hiddenStadiumName');
    const selectedStadium = localStorage.getItem('selectedStadium') || "M. Chinnaswamy Stadium";

    if (venueHeader) {
        venueHeader.innerText = "Availability: " + selectedStadium;
    }
    if (hiddenInput) {
        hiddenInput.value = selectedStadium;
    }

    populateSports(selectedStadium);
});

function goToAvailability(stadiumName) {
    localStorage.setItem('selectedStadium', stadiumName);
    window.location.href = "/availability/"; 
}

function populateSports(stadium) {
    const sportPicker = document.getElementById('sportPicker');
    if (!sportPicker) return;

    let sports = ["Cricket", "Football", "Volleyball"]; 
    if (stadium.includes("Indoor")) sports = ["Badminton", "Basketball", "Tennis"];
    if (stadium.includes("Aquatic")) sports = ["Swimming"];
    if (stadium.includes("Combat")) sports = ["MMA"];

    sportPicker.innerHTML = sports.map(s => `<option value="${s}">${s}</option>`).join('');
}

function finalizeCOD() {
    const stadium = localStorage.getItem('selectedStadium');
    // Matches the default 500.00 in your ArenaBooking model
    alert("Booking Reserved for " + stadium + "! Please pay ₹500.00 at the venue counter.");
    window.location.href = "/"; 
}

function goBack() {
    window.history.back();
}