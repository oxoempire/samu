<?php
// Lista con las letras del abecedario
$letras = array('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
          'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z');
?>

<!DOCTYPE html>
<html>
<head>
    <title>Adivina la letra</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <div class="container">
        <div class="frame">
            <!-- Frame izquierdo para la imagen principal -->
            <img id="imagen_letra" src="<?php echo $letras[0] . '.png'; ?>" alt="Imagen">
        </div>
        <div class="frame">
            <!-- Frame derecho para la segunda imagen -->
            <img id="imagen_letra2" src="<?php echo $letras[0] . '_.png'; ?>" alt="Imagen">
        </div>
    </div>

    <input type="text" id="letra" class="letra-input" placeholder="Ingrese una letra" maxlength="1">
    <button id="verificar" onclick="verificarLetra()">Verificar</button>

    <script src="script.js"></script>
</body>
</html>
