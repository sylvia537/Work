const welcomeScreen = document.getElementById('container');
welcomeScreen.addEventListener('click', () => {
    welcomeScreen.classList.add('slide_up');
    setTimeout(() => {
        welcomeScreen.style.display = 'none';
    }, 800);
});
document.getElementById("copyright-year").textContent = new Date().getFullYear();


function openSearch(){
    document.getElementById("searchBox").style.display = "block";
}
function closeSearch(){
    document.getElementById("searchBox").style.display = "none";
}

let cart = [];

function addToCart(name, price) {

    cart.push({
        name: name,
        price: price
    });

    alert(name + " has been added to your cart!");
}