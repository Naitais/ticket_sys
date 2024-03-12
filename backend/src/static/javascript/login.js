iniciar_sesion_btn = document.getElementById("iniciar_sesion_btn");
crear_cuenta_btn = document.getElementById("crear_cuenta_btn");

aceptar_nuevo_usuario_btn = document.getElementById("aceptar_nuevo_usuario_btn");
cancelar_nuevo_usuario_btn = document.getElementById("cancelar_nuevo_usuario_btn");


iniciar_sesion_btn.onclick = function(e) {
   //armo los datos del post request obteniendo la info que cargo en cada id del form que cree en el index de html
      var data = {
         usuario: $("#usuario_login").val(),
         contraseña: $("#contraseña_login").val(),
         csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
   };

   // ajax nuevo ticket
   $.ajax({
         type: 'POST',
         url: '/api/login/',
         data: data,
         success: function(response) {
            //si existe el usuario en la base de datos
            console.log("Inicio de sesión exitoso", response);
            window.location.href = '/api/tickets/';
            
         },
         error: function(error) {
            //mensaje de error
            console.error("Error de inicio de sesion", error);
            alert("Error de inicio de sesion")
            
         }
   });
};


aceptar_nuevo_usuario_btn.onclick = function(e) {
   var data = {
      usuario: $("#usuario_nuevo").val(),
      contraseña: $("#contraseña_nuevo").val(),
      email: $("#contraseña_nuevo").val(),
      csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
   };
    // ajax nuevo usuario
    $.ajax({
      type: 'POST',
      url: '/api/nuevo-usuario/',
      data: data,
      success: function(response) {
          //mensaje de exito
          console.log("Usuario creado con éxito.", response);
          alert("Usuario creado con éxito.")
          crear_nuevo_usuario.style.display = "none";
          location.reload()
          
      },
      error: function(xhr, status, error) {
          //mensaje de error
          console.error("Ocurrio un error al crear el usuario.", error);
          alert("Ocurrio un error al crear el usuario.")
          crear_nuevo_usuario.style.display = "none";
          
      }
  });
};

crear_cuenta_btn.onclick = function(e) {
   //armo los datos del post request obteniendo la info que cargo en cada id del form que cree en el index de html
   //crear_nuevo_usuario
 
   crear_nuevo_usuario.style.display = "block";
};

cancelar_nuevo_usuario_btn.onclick = function(e) {
   crear_nuevo_usuario.style.display = "none";
}