const welcomeScreen = document.getElementById('container');
welcomeScreen.addEventListener('click', () => {
    welcomeScreen.classList.add('slide_up');
    setTimeout(() => {
        welcomeScreen.style.display = 'none';
    }, 800);
});
document.getElementById("copyright-year").textContent = new Date().getFullYear();


function openSearch() {
    document.getElementById("dropdown-content").style.display = "flex";

    document.getElementById("searchInput").focus();
}

function findText() {

    const searchText = document
        .getElementById("searchInput")
        .value
        .trim();

    if (searchText === "") {
        return;
    }

    window.find(searchText);
}