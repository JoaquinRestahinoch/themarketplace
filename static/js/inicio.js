const countryDropdown = document.getElementById("countryDropdown");
const flagImage = document.getElementById("flagImage");

countryDropdown.addEventListener("change", function() {
    const selectedFlagUrl = countryDropdown.value;
    if (selectedFlagUrl) {
        flagImage.src = selectedFlagUrl;
        flagImage.style.display = "block";
    } else {
        flagImage.src = "";
        flagImage.style.display = "none";
    }
});

fetch("https://restcountries.com/v3.1/all")
    .then(response => response.json())
    .then(data => {
        data.sort((a, b) => a.name.common.localeCompare(b.name.common));

        data.forEach(country => {
            const option = document.createElement("option");
            option.value = country.flags.png;
            option.textContent = country.name.common;
            countryDropdown.appendChild(option);
        });
    })
    .catch(error => console.error("Error al cargar la lista de países: " + error));


    document.getElementById("selectButton").addEventListener("click", function() {
        window.location.href = "/home.html";
    });