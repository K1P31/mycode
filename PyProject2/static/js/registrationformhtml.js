document.addEventListener("DOMContentLoaded", function () {
    var registrationTypeSelect = document.getElementById("registration_type");
    var giRankDiv = document.getElementById("gi_rank_div");
    var noGiRankDiv = document.getElementById("no_gi_rank_div");

    function updateRankVisibility() {
        var selectedValue = registrationTypeSelect.value;
        giRankDiv.style.display = selectedValue === "Gi" ? "block" : "none";
        noGiRankDiv.style.display = selectedValue === "No-Gi" ? "block" : "none";
    }

    registrationTypeSelect.addEventListener("change", updateRankVisibility);
    updateRankVisibility(); // Initial call to set the correct visibility on load
});

function toggleRankOptions() {
    var registrationType = document.querySelector('select[name="registration_type"]').value;
    var giRankDiv = document.getElementById('gi_rank_div');
    var noGiRankDiv = document.getElementById('no_gi_rank_div');

// Hide both rank option divs
// giRankDiv.style.display = 'none';
// noGiRankDiv.style.display = 'none';

    if (registrationType === 'Gi') {
        giRankDiv.style.display = 'block';
    } else if (registrationType === 'No-Gi') {
        noGiRankDiv.style.display = 'block';
    }
}

document.querySelector('select[name="registration_type"]').addEventListener('change', toggleRankOptions);

toggleRankOptions();