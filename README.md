# Que función cumple esta api?
Para que el componente del mapa de mi app en angular genere los marcadores, necesito obtener las coordenadas de las ciudades que contienen las calles con el nombre buscado.
La api del Servicio de Normalización de Datos Geográficos de Argentina solo permite realizar una consulta por request, y dado que en algunos casos requería 
las coordenadas de hasta 2.000 ciudades, necesitaba otra opcion. 
  Ya que la información de estas coordenadas es libre y está publicada (https://datosgobar.github.io/georef-ar-api), importe los datos en csv a una base de datos en
sqlite y cree una api con un solo endpoint que acepta como único parámetro (POST) una lista de id's de las localidades, y devuelve una lista de coordenadas (long- lat)
