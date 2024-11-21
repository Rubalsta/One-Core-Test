uvicorn app.main:app --reload


Probar la API:
Registrar usuario: POST /register con username y password.
Obtener token: POST /token con username y password.
Acceder a endpoint protegido: GET /users/me con el token JWT.
¡Buena suerte con tu proyecto! 🚀

Ejecutar la aplicación: Asegúrate de que tu aplicación esté corriendo. Puedes hacerlo ejecutando el siguiente comando en la terminal desde el directorio donde se encuentra main.py:
uvicorn app.main:app --reload

Usar la documentación interactiva de FastAPI: FastAPI genera automáticamente una documentación interactiva para tu API. Abre tu navegador y ve a http://127.0.0.1:8000/docs. Aquí podrás ver y probar todos los endpoints de tu API.
Registrar un nuevo usuario: En la documentación interactiva, busca el endpoint POST /register. Haz clic en “Try it out” y proporciona un username y password en el cuerpo de la solicitud. Luego, haz clic en “Execute” para registrar un nuevo usuario.
Iniciar sesión y obtener un token: Busca el endpoint POST /token. Haz clic en “Try it out” y proporciona el username y password del usuario que acabas de registrar. Luego, haz clic en “Execute” para obtener un token JWT.
Acceder a un endpoint protegido: Copia el token JWT que obtuviste en el paso anterior. Luego, busca el endpoint GET /users/me. Haz clic en “Try it out” y pega el token en el campo “Authorize” (asegúrate de incluir el prefijo Bearer  antes del token). Luego, haz clic en “Execute” para acceder al endpoint protegido.