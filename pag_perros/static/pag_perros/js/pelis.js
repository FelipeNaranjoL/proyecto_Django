// este documento imprimira los datos de la pelicula ingresada
$(document).ready(function(){
    var llave = "1823f857"
    // la variable llave es necesaria solo por esta api
    $("#formulario_pelis").submit(function(event){
        event.preventDefault()
        // traera el nombre de la pelicula del input "#pelicula"
        var pelicula = $("#pelicula").val()
        var url = "http://www.omdbapi.com/?apikey="+llave
        var resultado = ""
        $.ajax({
            method:'GET',
            url:url+"&t="+pelicula,
            success:function(data){
                console.log(data)
                // si todo esta onkeydown, en la consola imprimira los datos de la pelicula
                resultado = `
                    <img src="${data.Poster}"/>
                    <h2>Director: <br>
                    ${data.Director}<br>----------------------<br/> 
                    Año de estreno: 
                    <br/> ${data.Year}<br>----------------------<br/>
                    Genero: 
                    <br/>${data.Genre} <br>----------------------<br/>
                    Actores Principales: 
                    <br/> ${data.Actors} <br>--------------------<br/>
                    Duracion:
                    <br/> ${data.Runtime}</h2>  
                `
                $("#resultado_busqueda").html(resultado)
            }
        })
    })
})


