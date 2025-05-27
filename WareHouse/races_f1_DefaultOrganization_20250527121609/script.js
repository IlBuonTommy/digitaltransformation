// Function to generate dynamic text (simulated by NLP agent)
function generateHistoryText() {
    return "La Formula 1 ha una lunga storia che risale agli anni '50, quando il primo Gran Premio fu organizzato in Belgio. Oggi è uno degli sport più seguiti al mondo.";
}
function generateBiographyText(name) {
    if (name === "Charles Leclerc") {
        return "Charles Leclerc è un pilota svizzero che ha vinto diversi titoli mondiali con la Ferrari. È noto per la sua abilità nel controllo della macchina e per il suo spirito competitivo.";
    } else if (name === "Lewis Hamilton") {
        return "Lewis Hamilton è uno dei piloti più premiati nella storia della Formula 1, con sette titoli mondiali. È noto per la sua velocità e per il suo impegno sociale fuori dal circuito.";
    }
    return "";
}
// Function to generate image URLs (simulated by image agent)
function getHistoricalImageURL() {
    return "https://picsum.photos/800/400?random=1";
}
function getDriverImageURL(name) {
    if (name === "Charles Leclerc") {
        return "https://picsum.photos/600/400?random=2";
    } else if (name === "Lewis Hamilton") {
        return "https://picsum.photos/600/400?random=3";
    }
    return "";
}
// Load dynamic content based on the page
document.addEventListener("DOMContentLoaded", function () {
    const currentPage = window.location.pathname.split("/").pop();
    const historyTextElement = document.getElementById("history-text");
    const biographyTextElement = document.getElementById("biography-text");
    const historicalImageElement = document.getElementById("historical-image");
    const driverImageElement = document.getElementById("driver-image");
    if (currentPage === "index.html") {
        historyTextElement.textContent = generateHistoryText();
        historicalImageElement.src = getHistoricalImageURL();
    } else if (currentPage === "charles-leclerc.html" || currentPage === "lewis-hamilton.html") {
        const driverName = currentPage.split("-")[0].charAt(0).toUpperCase() + currentPage.split("-")[0].slice(1) + " " + currentPage.split("-")[1].split(".")[0];
        biographyTextElement.textContent = generateBiographyText(driverName);
        driverImageElement.src = getDriverImageURL(driverName);
    }
});