            $(function() 
            {
              $("#mi-formulario").validate({
                   rules: {
                          gmail: {
                              required: true,
                              email: true
                          },
                          nombre: {
                            required: true,
                        },
                          apellido: "required",
                          categoria: "required",
                          numero: "required",
                          comentario: "required"    
                          
                      }, //rules
                  messages: {
                      gmail: {
                          required: 'Ingresa tu correo electrónico',
                          email: 'Formato de correo no válido'
                      },
                      nombre: {
                        required: 'Ingrese su nombre',
                    },
                      apellido:{
                          required: 'Ingrese tu apellido',
                      },
                      categoria:{
                        required: 'Seleccione el motivo de su contacto'
                      },
                      numero:{
                          required: 'Ingrese su numero de telefono'
                      },
                      comentario:{
                          required: 'Indique el motivo de su contacto'
                      }
                  }//messages
              }); //$('#mi-formulario').validate
          }); //function


          function CambiarMayusculasNombre()
        {
            var a = document.getElementById("nombre");
            a.value = a.value.charAt(0).toUpperCase()+a.value.substr (1);
        }
        function CambiarMayusculasApellido()
        {
            var a = document.getElementById("apellido");
            a.value = a.value.charAt(0).toUpperCase()+a.value.substr (1);
        }

        function dialogBox(){
            alert('Se han limpiado correctamente los cuadros.');
          }


          
          $(document).ready(function()
          {
              $("#solicitar").click(function(){
  
                  $.get("https://mindicador.cl/api",
                      function(data){
                          
                          $.each(data,function(i,item){
                              $("#monedas").append("<tr><td>"+item.codigo+"</td><td>"+item.nombre +
                              "</td><td>"+'$' +item.valor+ "</td><td>");
                              
  
                          });
  
                      });
              });
          })

