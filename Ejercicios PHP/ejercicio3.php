<?php


$secreto = 37; // define el número secreto
$intento = 1;
$adivinanza = 1;

while (true) {
    echo "Intento {$intento}: {$adivinanza}" . PHP_EOL;
    if ($adivinanza === $secreto) {
        echo "¡Número secreto {$secreto} encontrado en el intento {$intento}!" . PHP_EOL;
        break;
    }
    $adivinanza++;
    $intento++;
}
?>
