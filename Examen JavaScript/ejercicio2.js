const nombreProducto = "Tablet 10 pulgadas"
let precio = 450.99
let stock = 2
const envioGratis = true

console.log("Nombre del producto:", nombreProducto)
console.log("Precio:", precio)
console.log("Stock disponible:", stock)
console.log("Envío gratis:", envioGratis)

let subtotal = precio * stock
let total = subtotal % 7 + subtotal 

console.log("Subtotal:", subtotal)
console.log("Total (con impuesto del 7%):", total)