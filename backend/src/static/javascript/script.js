// obtengo ventana modal del formulario segun id
var modal = document.getElementById("modal");
var modificar_ticket_pantalla = document.getElementById("modificar_ticket_pantalla");
var ticket_informacion = document.getElementById("ticket_informacion");

// obtengo botones segun id
var nuevo_ticket_btn = document.getElementById("nuevo_ticket_btn");
var aceptar_nuevo_ticket_btn = document.getElementById("aceptar_nuevo_ticket_btn");
var cancelar_nuevo_ticket_btn = document.getElementById("cancelar_nuevo_ticket_btn");
var row_modificar_btn = document.getElementsByClassName("row_modificar_btn");
var row_eliminar_btn = document.getElementsByClassName("row_eliminar_btn");
//var cancelar_cambios_btn = document.getElementById("cancelar_cambios_btn")
//var aceptar_cambios_btn = document.getElementById("aceptar_cambios_btn")

// ticket row es una coleccion de elementos asi que hay que loopearlos
var ticket_rows = document.getElementsByClassName("ticket_row");

//obtengo los inputs del form para modificar su placehold text
var input_form_campo = document.getElementsByClassName("input_form");

// variable para guardar el id del 
var ticket_id

for (var i = 0; i < ticket_rows.length; i++) {
    ticket_rows[i].addEventListener("mouseout", function(event) {
        // afecto al parent del target
        //event.target.parentElement.style.backgroundColor = "white";
        
    });
}

for (var i = 0; i < ticket_rows.length; i++) {
    // busco la columna de estado de ticket y pinto de un color segun corresponda
    var estado_ticket = ticket_rows[i].getElementsByTagName("td")[8].textContent;
    if (estado_ticket == "Pendiente"){
        ticket_rows[i].style.backgroundColor = "orange";
    }

    if (estado_ticket == "Verificar"){
        ticket_rows[i].style.backgroundColor = "yellow";
    }

    if (estado_ticket == "Resuelto"){
        ticket_rows[i].style.backgroundColor = "green";
    }
}

//muestro al hacer click
nuevo_ticket_btn.onclick = function() {
    modal.style.display = "block";
  }

//escondo al cancelar
cancelar_nuevo_ticket_btn.onclick = function() {
    modal.style.display = "none";
  }


aceptar_nuevo_ticket_btn.onclick = function(e) {
    //armo los datos del post request obteniendo la info que cargo en cada id del form que cree en el index de html
    var data = {
        concepto: $("#concepto").val(),
        empresa: $("#empresa").val(),
        legajo: $("#legajo").val(),
        nombre: $("#nombre").val(),
        observaciones: $("#observaciones").val(),
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
    };

    // ajax nuevo ticket
    $.ajax({
        type: 'POST',
        url: '/api/nuevo-ticket/',
        data: data,
        success: function(response) {
            //mensaje de exito
            console.log("Ticket creado con éxito.", response);
            alert("Ticket creado con éxito.")
            modal.style.display = "none";
            location.reload()
            
        },
        error: function(xhr, status, error) {
            //mensaje de error
            console.error("Ocurrio un error al crear el ticket.", error);
            alert("Ocurrio un error al crear el ticket.")
            modal.style.display = "none";
            
        }
    });
};

// funcion para modificar un ticket
row_modificar_btn.onclick = function() {
  }

for (var i = 0; i < row_modificar_btn.length; i++) {
    row_modificar_btn[i].addEventListener("click", function(event) {
        modificar_ticket_pantalla.style.display = "block";
        
        //obtengo los nodos de columna de la row seleccionada
        var columnas = event.target.parentNode.parentNode.getElementsByTagName("td")
        llenarCampoPlaceholderForm(columnas)
        
        
    });
}

cancelar_cambios_btn.onclick = function() {
    modificar_ticket_pantalla.style.display = "none";
  }

function llenarCampoPlaceholderForm(columnas){
    ticket_id = event.target.parentNode.parentNode.getElementsByTagName("td")[0].textContent
    ticket_id = parseInt(ticket_id)
    //quito 2 porque esas dos son columnas con botones y empieza de 3 porque los campos anteriores no necesito modificar
    for (var r = 3; r < columnas.length -2; r ++){

        //obtengo datos de cada columna de la row seleccionada
        var informacion_ticket = event.target.parentNode.parentNode.getElementsByTagName("td")[r].textContent

        // cambio el texto placeholder para tener el del ticket
        // le resto 3 para que coincida con el indice de los campos del form
        input_form_campo[r - 3].value = informacion_ticket
    }
}

aceptar_cambios_btn.onclick = function(e) {
    //armo los datos del post request obteniendo la info que cargo en cada id del form que cree en el index de html
    var data = {
        concepto: $("#concepto_modificar").val(),
        empresa: $("#empresa_modificar").val(),
        legajo: $("#legajo_modificar").val(),
        nombre: $("#nombre_modificar").val(),
        observaciones: $("#observaciones_modificar").val(),
        estado_liquidaciones: $("#estado_liquidaciones_modificar").val(),
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
    };

    // ajax modificacion de ticket
    $.ajax({
        type: 'POST',
        url: '/api/modificar-ticket/'+ticket_id+'/',
        data: data,
        success: function(response) {
            //mensaje de exito
            console.log("Ticket modificado con éxito.", response);
            
            alert("Ticket modificado con éxito.")
            modificar_ticket_pantalla.style.display = "none";
            location.reload()
            
        },
        error: function(xhr, status, error) {
            //mensaje de error
            console.error("Ocurrio un error al modificar el ticket.", error);
            alert("Ocurrio un error al modificar el ticket.")
            modificar_ticket_pantalla.style.display = "none";
            
        }
    });
};


// funcion para eliminar un ticket
row_eliminar_btn.onclick = function() {
}

cancelar_eliminar_ticket_btn.onclick = function() {
    eliminar_ticket_pantalla.style.display = "none";
  }

for (var i = 0; i < row_eliminar_btn.length; i++) {
    row_eliminar_btn[i].addEventListener("click", function(event) {
    eliminar_ticket_pantalla.style.display = "block";
      
    //obtengo los nodos de columna de la row seleccionada
    var columnas = event.target.parentNode.parentNode.getElementsByTagName("td")
    //console.log(columnas)
    llenarCampoPlaceholderForm(columnas)
    ticket_id = event.target.parentNode.parentNode.getElementsByTagName("td")[0].textContent
    ticket_id = parseInt(ticket_id)
  });
}

aceptar_eliminar_ticket_btn.onclick = function(e) {
    var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
    // ajax eliminar ticket
    $.ajax({
        type: 'DELETE',
        url: '/api/eliminar-ticket/'+ticket_id+'/',
        headers: {
            "X-CSRFToken": csrfToken
        },
        success: function(response) {
            //mensaje de exito
            console.log("Ticket eliminado con éxito.", response);
            
            alert("Ticket eliminado con éxito.")
            eliminar_ticket_pantalla.style.display = "none";
            location.reload()
            
        },
        error: function(xhr, status, error) {
            //mensaje de error
            console.error("Ocurrio un error al modificar el ticket.", error);
            alert("Ocurrio un error al modificar el ticket.")
            eliminar_ticket_pantalla.style.display = "none";
            
        }
    });
};