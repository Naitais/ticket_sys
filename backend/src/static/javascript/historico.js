

// agregar funcion para ver cantidad de tickets en un mismo dia o mes o año
// o buscar un ticket en especifico

// funcion para cerrar sesion
cerrar_sesion_btn.onclick = function(){
    usuario_logueado = null
    window.location.href = '/api/login/';
}

// funcion para ir a historicos
ticketera_btn.onclick = function(){
    window.location.href = '/api/tickets/';
}

// funcion filtrar y hacer consulta de tickets
filtrar_tickets_btn.onclick = function(){
     //armo los datos del post request obteniendo la info que cargo en cada id del form que cree en el index de html
     var data = {
        mes: $("#mes").val(),
        año: $("#año").val(),
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
    };

    // ajax modificacion de ticket
    $.ajax({
        type: 'POST',
        url: '/api/historico-tickets/',
        data: data,
        error: function(error) {
            //mensaje de error
            console.error("Ocurrio un error al modificar el ticket.", error);
            alert("Ocurrio un error al modificar el ticket.")
            //eliminar_ticket_pantalla.style.display = "none";
            
        }
    });
    
    window.location.href = '/api/consulta-tickets/';
}