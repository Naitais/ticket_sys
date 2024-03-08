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