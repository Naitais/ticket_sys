// obtengo ventana modal del formulario segun id
var modal = document.getElementById("modal");
var ticket_informacion = document.getElementById("ticket_informacion");

// obtengo botones segun id
var nuevo_ticket_btn = document.getElementById("nuevo_ticket_btn");
var aceptar_nuevo_ticket_btn = document.getElementById("aceptar_nuevo_ticket_btn");
var cancelar_nuevo_ticket_btn = document.getElementById("cancelar_nuevo_ticket_btn");

// ticket row es como una coleccion de elementos asi que hay que loopearlos
var ticket_rows = document.getElementsByClassName("ticket_row");

for (var i = 0; i < ticket_rows.length; i++) {
    ticket_rows[i].addEventListener("click", function(event) {
        // afecto al parent del target
        //event.target.parentElement.style.backgroundColor = "tomato";
        ticket_informacion.style.display = "block";
        
        
    });
}

for (var i = 0; i < ticket_rows.length; i++) {
    ticket_rows[i].addEventListener("mouseout", function(event) {
        // afecto al parent del target
        //event.target.parentElement.style.backgroundColor = "white";
        
    });
}

for (var i = 0; i < ticket_rows.length; i++) {
    // busco la columna de estado de ticket y pinto de un color segun corresponda
    var columnText = ticket_rows[i].getElementsByTagName("td")[8].textContent;
    if (columnText == "Pendiente"){
        ticket_rows[i].style.backgroundColor = "orange";
    }

    if (columnText == "Verificar"){
        ticket_rows[i].style.backgroundColor = "yellow";
    }

    if (columnText == "Resuelto"){
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

cerrar_ventana_btn.onclick = function() {
    ticket_informacion.style.display = "none";
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

    // configuro ajax
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
