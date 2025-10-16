let edad = 19;
let tieneEntrada = false;   

if (edad >= 18 && tieneEntrada === true) {
    console.log("Puedes entrar al evento.");
}
else if (edad >= 18 && tieneEntrada === false) {
    console.log("No puedes entrar al evento, te falta la entrada.");
}
else if (edad < 18 && tieneEntrada === true) {
    console.log("No puedes entrar al evento, eres menor de edad.");
}
else {
    console.log("No puedes entrar al evento, eres menor de edad y te falta la entrada.");
}
