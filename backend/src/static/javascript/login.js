iniciar_sesion_btn = document.getElementById("iniciar_sesion_btn");





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
