
document.addEventListener("DOMContentLoaded", () => {
    const carrito = JSON.parse(localStorage.getItem("carrito")) || [];

    function mostrarResumenCarrito() {
        const resumenCarrito = document.querySelector("#resumen-carrito tbody");
        const totalCompra = document.getElementById("total-compra");
        let total = 0;

        carrito.forEach(item => {
            const fila = document.createElement("tr");
            fila.innerHTML = `
                <td><img src="${item.foto}" alt="${item.producto}" width="50"></td>
                <td>${item.producto}</td>
                <td>${item.cantidad}</td>
            `;
            resumenCarrito.appendChild(fila);

            total += item.precioUnitario * item.cantidad;
        });

        totalCompra.textContent = `$${total}`;
    }

    mostrarResumenCarrito();

    const confirmarCompraButton = document.getElementById("confirmar-compra");
    confirmarCompraButton.addEventListener("click", () => {
        const confirmacion = confirm("¡Gracias por tu compra!");

        if (confirmacion) {
            window.location.href = "home.html";
        }
    });
});
function formatNumeroTarjeta(input) {
const cleanedInput = input.value.replace(/\D/g, "");

const formattedInput = cleanedInput.replace(/(\d{4})(?=\d)/g, "$1 ");

input.value = formattedInput;
}

function formatVencimientoTarjeta(input) {
const cleanedInput = input.value.replace(/\D/g, "");

if (cleanedInput.length > 2) {
input.value = cleanedInput.slice(0, 2) + '/' + cleanedInput.slice(2, 4);
} else {
input.value = cleanedInput;
}
}
function formatNombreTarjeta(input) {
input.value = input.value.toUpperCase();
}

