const formularz = document.getElementById("orderForm");
const imie = document.getElementById("imie");
const email = document.getElementById("email");
const telefon = document.getElementById("telefon");
const swieca = document.getElementById("swieca");
const ilosc = document.getElementById("ilosc");
const dedykacja = document.getElementById("dedykacja");
const imieError = document.getElementById("imieError");
const emailError = document.getElementById("emailError");
const telefonError = document.getElementById("telefonError");
const swiecaError = document.getElementById("swiecaError");
const iloscError = document.getElementById("iloscError");
const charCount = document.getElementById("charCount");
const successMessage = document.getElementById("successMessage");
const buttons = document.querySelectorAll(".add-to-cart");
console.log(buttons.length);

console.log(imie.value);
console.log(email.value);
console.log(telefon.value);

formularz.addEventListener("submit", function(event) {
    event.preventDefault();
   
    imieError.textContent = "";
    emailError.textContent = "";
    telefonError.textContent = "";
    swiecaError.textContent = "";
    iloscError.textContent = "";
    
    if (imie.value === "") {
        imieError.textContent = "Nie wpisano imienia!";
    }
    
    if (email.value === "") {
        emailError.textContent = "Nie wpisano emaila!";
    }
    else if (!email.value.includes("@")) {
        emailError.textContent = "Niepoprawny email!";
    }

    if (telefon.value === "") {
        telefonError.textContent = "Nie wpisano telefonu";
    }
    else if (!/^[0-9]{9}$/.test(telefon.value)) {
        telefonError.textContent = "Telefon jest niepoprawny";
    }

    if (swieca.value === "") {
        swiecaError.textContent = "Nie wybrano świecy!";
    }

    if (ilosc.value === "") {
        iloscError.textContent = "Nie podano ilości!";
    }
    
    if (ilosc.value < 1 || ilosc.value > 20) {
        iloscError.textContent = "Ilość musi być od 1 do 20!";
    }

    if (dedykacja.value.length > 40) {
        console.log("Dedykacja może mieć maksymalnie 40 znaków!");
    }
    
    if (
        imie.value !== "" &&
        email.value.includes("@") &&
        email.value.includes(".") &&
        /^[0-9]{9}$/.test(telefon.value) &&
        swieca.value !== "" &&
        ilosc.value >= 1 &&
        ilosc.value <= 20
    ) {
        formularz.style.display = "none";

        successMessage.textContent =
        "Dziękujemy, " + imie.value + 
        "! Potwierdzenie zamówienia wyślemy na " +
        email.value + ".";
    }

    console.log("Kliknięto Zamawiam!");
});

dedykacja.addEventListener("input", function() {
    charCount.textContent = dedykacja.value.length + " / 40";
});

let total = 0;

buttons.forEach(button => {
    button.addEventListener("click", function() {

        const price = Number(this.dataset.price);

        total += price;

        const shipping = document.getElementById("free-shipping");

        if (total >= 150) {
            shipping.textContent = "Darmowa wysyłka!";
        } else {
            shipping.textContent = "";
        }

        document.getElementById("total-price").textContent = total.toFixed(2);

    });
});