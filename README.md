
 
 ## Instrucciones de uso 
 
 Para iniciar la aplicación, solamente escribir en el directorio raiz de esta
 
 * `docker-compose build` (para crear el contenedor)
 * `docker-compose up` (para iniciar el contenedor)
 
 En el caso de la P3 se debe añadir en otra terminal:
 
 * `docker-compose exec mongo /bin/bash`
 * `mongorestore --drop dump`
 
 que restaturará la base de datos 'SampleCollections' con las collecciones que tenga.
 
 La aplicación se encontrará en:
 
 * http://localhost:5000/
 
 
