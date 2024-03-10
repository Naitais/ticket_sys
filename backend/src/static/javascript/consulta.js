function pintar_tickets_segun_estado(){
    // ticket row es una coleccion de elementos asi que hay que loopearlos
    var ticket_rows = document.getElementsByClassName("ticket_row");
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
}

// funcion para ir a historicos
volver_tabla_tickets.onclick = function(){
    window.location.href = '/api/historico-tickets/';
}

pintar_tickets_segun_estado()