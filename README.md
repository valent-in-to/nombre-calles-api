# Que función cumple esta api?
Para que el _componente_ "mapa" de [ésta app](https://github.com/valent-in-to/tu-nombre-en-las-calles) genere los marcadores, necesito obtener las coordenadas de las ciudades que contienen las calles con el nombre buscado.
La api del Servicio de Normalización de Datos Geográficos de Argentina solo permite realizar una consulta por request, y dado que en algunos casos requería 
las coordenadas de hasta 2.000 ciudades, necesitaba otra opcion. 
  Ya que la información de estas coordenadas es libre y está publicada (https://datosgobar.github.io/georef-ar-api), cree mi propia base de datos en
sqlite importando la información que descargué del sitio supra mencionado y cree una api con un solo endpoint que acepta como único parámetro una lista de id's de las localidades, y devuelve una lista de coordenadas (long- lat)

En resumen: una API que recibe una lista de id's asociadas a localidades argentinas y retora una lista de las coordenadas de cada una de esas localidades.
