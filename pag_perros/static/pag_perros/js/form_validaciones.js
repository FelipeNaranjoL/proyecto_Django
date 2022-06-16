$(document).ready(function(){
    $("#formulario").validate({
        // reglas para validar cada dato del formulario
        rules:{
            usuario:{
                required: true,
                minlength: 3
            },
            contraseña:{
                required: true,
                minlength: 8
            },
            val_contraseña:{
                required: true,
                minlength: 8,
                equalTo: "#contraseña"
            },
            correo:{
                required: true,
                email: true
            },
            numero:{
                required: true,
                number: true,
                minlength: 9
            }
        },
        messages: {
            // mensaje por si la informacion ingresada es erronea
            usuario:{
                required: "Este campo es requerido, porfavor completelo",
                minlength: "Ingresa un nombre de almenos 3 caracteres"
            },
            contraseña:{
                required: "Este campo es obligatorio",
                minlength: "Tu contraseña debe tener almenos 8 caracteres"
            },
            val_contraseña:{
                required: "Este campo es obligatorio",
                minlength: "Tu contraseña debe tener almenos 8 caracteres",
                equalTo: "Porfavor ingrese la misma contraseña de arriba"
            },
            correo:{
                required: "Este campo es obligatorio",
                email: "Ingrese un correo valido"
            },
            numero:{
                required: "Este campo es obligatorio",
                numero: "Ingrese un numero valido",
                minlength: "El minimo de numeros tolerados es 9"
            }
        }
    });
});