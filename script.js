var letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
          'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
var letra_actual = 0;

window.onload = function() {
    document.getElementById('imagen_letra').src = letras[letra_actual] + '.png';
    document.getElementById('imagen_letra2').src = letras[letra_actual] + '_.png';
}

function verificarLetra() {
    var letraIngresada = document.getElementById('letra').value.toUpperCase();
    if (letraIngresada.length === 1 && letras.indexOf(letraIngresada) !== -1) {
        if (letraIngresada === letras[letra_actual]) {
            siguienteLetra();
        } else {
            alert('¡Letra incorrecta!');
        }
        document.getElementById('letra').value = '';  // Limpiar la entrada de texto después de verificar la letra
    } else {
        alert('Por favor, ingrese una letra válida.');
    }
}

function siguienteLetra() {
    if (letra_actual < letras.length - 1) {
        letra_actual++;
        document.getElementById('imagen_letra').src = letras[letra_actual] + '.png';
        document.getElementById('imagen_letra2').src = letras[letra_actual] + '_.png';
    } else {
        alert('¡Has adivinado todas las letras!');
    }
}
