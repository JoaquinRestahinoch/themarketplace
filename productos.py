productos = [
    {'id': 0, 'name': 'Laptop Lenovo negra 15,6 con 512 GB', 'categoria': 'tecnologia', 'price': 800000, 'quantity': 1, 'descripcion': 'Una potente laptop Lenovo con pantalla de 15,6 pulgadas y 512 GB de almacenamiento para tus necesidades tecnológicas.', 'foto': '/static/img/prod0.png'},
    {'id': 1, 'name': 'iPhone 14 Pro Max - Apple', 'categoria': 'tecnologia', 'price': 90000, 'quantity': 2, 'descripcion': 'El último iPhone 14 Pro Max de Apple con características innovadoras para mantenerte conectado y productivo.', 'foto': '/static/img/prod1.png'},
    {'id': 2, 'name': 'Lavadora de carga frontal LG', 'categoria': 'electrodomesticos', 'price': 900000, 'quantity': 2, 'descripcion': 'Una lavadora de carga frontal LG eficiente y silenciosa para mantener tu ropa impecable.', 'foto': '/static/img/prod2.png'},
    {'id': 3, 'name': 'Aspiradora Dyson V11 Absolute', 'categoria': 'electrodomesticos', 'price': 600000, 'quantity': 3, 'descripcion': 'La aspiradora Dyson V11 Absolute para una limpieza impecable en tu hogar.', 'foto': '/static/img/prod3.png'},
    {'id': 4, 'name': 'Bicicleta de montaña Trek 29er', 'categoria': 'deportes', 'price': 1500000, 'quantity': 4, 'descripcion': 'Una bicicleta de montaña Trek 29er para aventuras al aire libre y rutas emocionantes.', 'foto': '/static/img/prod4.png'},
    {'id': 5, 'name': 'Camiseta de fútbol', 'categoria': 'indumentaria', 'price': 50000, 'quantity': 10, 'descripcion': 'Una camiseta de fútbol de alta calidad para mostrar tu pasión por el deporte.', 'foto': '/static/img/prod5.png'},
    {'id': 6, 'name': 'Secadora de ropa Whirlpool', 'categoria': 'electrodomesticos', 'price': 700000, 'quantity': 2, 'descripcion': 'Una secadora de ropa Whirlpool que mantiene tu ropa fresca y seca en todo momento.', 'foto': '/static/img/prod6.png'},
    {'id': 7, 'name': 'Zapatos deportivos Reebok', 'categoria': 'deportes', 'price': 80000, 'quantity': 5, 'descripcion': 'Zapatos deportivos Reebok para una comodidad óptima durante tus actividades deportivas.', 'foto': '/static/img/prod7.png'},
    {'id': 8, 'name': 'Reloj de moda para hombres', 'categoria': 'moda', 'price': 150000, 'quantity': 7, 'descripcion': 'Un elegante reloj de moda para hombres que complementa tu estilo.', 'foto': '/static/img/prod8.png'},
    {'id': 9, 'name': 'Taladro eléctrico Bosch', 'categoria': 'herramientas', 'price': 90000, 'quantity': 3, 'descripcion': 'Un taladro eléctrico Bosch para tus proyectos de bricolaje y reparaciones en el hogar.', 'foto': '/static/img/prod9.png'},
    {'id': 10, 'name': 'Abrigo de invierno para mujeres', 'categoria': 'indumentaria', 'price': 120000, 'quantity': 6, 'descripcion': 'Un abrigo de invierno elegante y cálido para mujeres que enfrentan el frío con estilo.', 'foto': '/static/img/prod10.png'},
    {'id': 11, 'name': 'Cafetera Nespresso', 'categoria': 'electrodomesticos', 'price': 100000, 'quantity': 4, 'descripcion': 'Una cafetera Nespresso para disfrutar de un café delicioso en casa.', 'foto': '/static/img/prod11.png'},
    {'id': 12, 'name': 'Raqueta de tenis Wilson', 'categoria': 'deportes', 'price': 80000, 'quantity': 5, 'descripcion': 'Una raqueta de tenis Wilson de alto rendimiento para tus partidos en la cancha.', 'foto': '/static/img/prod12.png'},
    {'id': 13, 'name': 'Vestido de noche elegante', 'categoria': 'moda', 'price': 180000, 'quantity': 3, 'descripcion': 'Un vestido de noche elegante y sofisticado para ocasiones especiales.', 'foto': '/static/img/prod13.png'},
    {'id': 14, 'name': 'Juego de llaves y destornilladores', 'categoria': 'herramientas', 'price': 60000, 'quantity': 5, 'descripcion': 'Un juego completo de llaves y destornilladores para tus necesidades de reparación.', 'foto': '/static/img/prod14.png'},
    {'id': 15, 'name': 'Pantalones vaqueros de moda', 'categoria': 'moda', 'price': 70000, 'quantity': 8, 'descripcion': 'Pantalones vaqueros de moda que combinan estilo y comodidad.', 'foto': '/static/img/prod15.png'},
    {'id': 16, 'name': 'Horno de microondas Panasonic', 'categoria': 'electrodomesticos', 'price': 90000, 'quantity': 4, 'descripcion': 'Un horno de microondas Panasonic para calentar y cocinar tus alimentos de manera eficiente.', 'foto': '/static/img/prod16.png'},
    {'id': 17, 'name': 'Caja de herramientas completa', 'categoria': 'herramientas', 'price': 120000, 'quantity': 2, 'descripcion': 'Una caja de herramientas completa con todas las herramientas esenciales para tus proyectos.', 'foto': '/static/img/prod17.png'},
    {'id': 18, 'name': 'Gorra de béisbol', 'categoria': 'indumentaria', 'price': 25000, 'quantity': 15, 'descripcion': 'Una gorra de béisbol clásica para protegerte del sol y lucir con estilo.', 'foto': '/static/img/prod18.png'},
    {'id': 19, 'name': 'Mochila deportiva resistente', 'categoria': 'deportes', 'price': 60000, 'quantity': 7, 'descripcion': 'Una mochila deportiva resistente para llevar tus pertenencias mientras te mantienes activo.', 'foto': '/static/img/prod19.png'},
    {'id': 20, 'name': 'Tablet Samsung Galaxy', 'categoria': 'tecnologia', 'price': 400000, 'quantity': 3, 'descripcion': 'Una tablet Samsung Galaxy con pantalla de alta resolución y rendimiento óptimo.', 'foto': '/static/img/prod20.png'},
    {'id': 21, 'name': 'Batidora KitchenAid', 'categoria': 'electrodomesticos', 'price': 120000, 'quantity': 6, 'descripcion': 'Una batidora KitchenAid para preparar deliciosos pasteles y postres.', 'foto': '/static/img/prod21.png'},
    {'id': 22, 'name': 'Zapatillas para correr Nike', 'categoria': 'deportes', 'price': 90000, 'quantity': 8, 'descripcion': 'Zapatillas para correr Nike para un rendimiento excepcional en tus carreras.', 'foto': '/static/img/prod22.png'},
    {'id': 23, 'name': 'Vestido de fiesta elegante', 'categoria': 'moda', 'price': 250000, 'quantity': 4, 'descripcion': 'Un vestido de fiesta elegante y sofisticado para ocasiones especiales.', 'foto': '/static/img/prod23.png'},
    {'id': 24, 'name': 'Sierra circular Makita', 'categoria': 'herramientas', 'price': 150000, 'quantity': 3, 'descripcion': 'Una sierra circular Makita para cortes precisos en tus proyectos de carpintería.', 'foto': '/static/img/prod24.png'},
    {'id': 25, 'name': 'Chaqueta de cuero para hombres', 'categoria': 'indumentaria', 'price': 180000, 'quantity': 5, 'descripcion': 'Una chaqueta de cuero para hombres con estilo atemporal y durabilidad.', 'foto': '/static/img/prod25.png'},
    {'id': 26, 'name': 'Licuadora de alta potencia', 'categoria': 'electrodomesticos', 'price': 80000, 'quantity': 4, 'descripcion': 'Una licuadora de alta potencia para preparar batidos y bebidas saludables.', 'foto': '/static/img/prod26.png'},
    {'id': 27, 'name': 'Pelota de fútbol Adidas', 'categoria': 'deportes', 'price': 40000, 'quantity': 12, 'descripcion': 'Una pelota de fútbol Adidas de alta calidad para tus partidos en la cancha.', 'foto': '/static/img/prod27.png'},
    {'id': 28, 'name': 'Bolso de moda para mujeres', 'categoria': 'moda', 'price': 120000, 'quantity': 6, 'descripcion': 'Un bolso de moda para mujeres que combina estilo y funcionalidad.', 'foto': '/static/img/prod28.png'},
    {'id': 29, 'name': 'Set de herramientas de jardinería', 'categoria': 'herramientas', 'price': 70000, 'quantity': 4, 'descripcion': 'Un set de herramientas de jardinería completo para cuidar tu jardín.', 'foto': '/static/img/prod29.png'},
    {'id': 30, 'name': 'Jersey de lana para invierno', 'categoria': 'indumentaria', 'price': 80000, 'quantity': 7, 'descripcion': 'Un jersey de lana cálido y acogedor para el invierno.', 'foto': '/static/img/prod30.png'},
    {'id': 31, 'name': 'Cocina de gas Whirlpool', 'categoria': 'electrodomesticos', 'price': 300000, 'quantity': 2, 'descripcion': 'Una cocina de gas Whirlpool para cocinar tus comidas favoritas.', 'foto': '/static/img/prod31.png'},
    {'id': 32, 'name': 'Set de destornilladores profesionales', 'categoria': 'herramientas', 'price': 60000, 'quantity': 5, 'descripcion': 'Un set de destornilladores de alta calidad para trabajos profesionales.', 'foto': '/static/img/prod32.png'},
    {'id': 33, 'name': 'Gafas de sol de moda', 'categoria': 'moda', 'price': 35000, 'quantity': 10, 'descripcion': 'Gafas de sol de moda para proteger tus ojos con estilo.', 'foto': '/static/img/prod33.png'},
    {'id': 34, 'name': 'Mesa de picnic plegable', 'categoria': 'herramientas', 'price': 70000, 'quantity': 3, 'descripcion': 'Una mesa de picnic plegable para disfrutar al aire libre.', 'foto': '/static/img/prod34.png'},
    {'id': 35, 'name': 'Lavavajillas Bosch', 'categoria': 'electrodomesticos', 'price': 900000, 'quantity': 2, 'descripcion': 'Un lavavajillas Bosch para una limpieza eficiente de tus platos y utensilios.', 'foto': '/static/img/prod35.png'},
    {'id': 36, 'name': 'Mochila de senderismo', 'categoria': 'deportes', 'price': 80000, 'quantity': 6, 'descripcion': 'Una mochila de senderismo resistente para tus aventuras en la naturaleza.', 'foto': '/static/img/prod36.png'},
    {'id': 37, 'name': 'Vestido de verano para mujeres', 'categoria': 'moda', 'price': 80000, 'quantity': 7, 'descripcion': 'Un vestido de verano ligero y colorido para mujeres.', 'foto': '/static/img/prod37.png'},
    {'id': 38, 'name': 'Herramientas de carpintería', 'categoria': 'herramientas', 'price': 70000, 'quantity': 5, 'descripcion': 'Un conjunto de herramientas de carpintería esenciales para tus proyectos de bricolaje.', 'foto': '/static/img/prod38.png'},
    {'id': 39, 'name': 'Zapatillas de moda para hombres', 'categoria': 'indumentaria', 'price': 60000, 'quantity': 8, 'descripcion': 'Zapatillas de moda para hombres que combinan comodidad y estilo.', 'foto': '/static/img/prod39.png'},
    {'id': 40, 'name': 'Cámara DSLR Canon', 'categoria': 'tecnologia', 'price': 700000, 'quantity': 3, 'descripcion': 'Una cámara DSLR Canon para capturar imágenes de alta calidad.', 'foto': '/static/img/prod40.png'},
    {'id': 41, 'name': 'Reproductor de música Sony', 'categoria': 'tecnologia', 'price': 40000, 'quantity': 10, 'descripcion': 'Un reproductor de música Sony para escuchar tus canciones favoritas.', 'foto': '/static/img/prod41.png'},
    {'id': 42, 'name': 'Heladera de acero inoxidable', 'categoria': 'electrodomesticos', 'price': 800000, 'quantity': 3, 'descripcion': 'Una heladera de acero inoxidable de alta calidad para mantener tus alimentos frescos.', 'foto': '/static/img/prod42.png'},
    {'id': 43, 'name': 'Pantalones deportivos', 'categoria': 'indumentaria', 'price': 50000, 'quantity': 15, 'descripcion': 'Pantalones deportivos cómodos y funcionales para tus actividades físicas.', 'foto': '/static/img/prod43.png'},
    {'id': 44, 'name': 'Set de ollas y sartenes', 'categoria': 'electrodomesticos', 'price': 90000, 'quantity': 6, 'descripcion': 'Un set de ollas y sartenes de alta calidad para cocinar con precisión.', 'foto': '/static/img/prod44.png'},
    {'id': 45, 'name': 'Botas de senderismo', 'categoria': 'deportes', 'price': 70000, 'quantity': 4, 'descripcion': 'Botas de senderismo resistentes para tus excursiones en la montaña.', 'foto': '/static/img/prod45.png'},
    {'id': 46, 'name': 'Vestido de cóctel para mujeres', 'categoria': 'moda', 'price': 120000, 'quantity': 5, 'descripcion': 'Un vestido de cóctel elegante y sofisticado para ocasiones especiales.', 'foto': '/static/img/prod46.png'},
    {'id': 47, 'name': 'Set de herramientas de pintura', 'categoria': 'herramientas', 'price': 30000, 'quantity': 10, 'descripcion': 'Un set de herramientas de pintura para artistas y amantes del arte.', 'foto': '/static/img/prod47.png'},
    {'id': 48, 'name': 'Cinturón de cuero de lujo', 'categoria': 'indumentaria', 'price': 25000, 'quantity': 20, 'descripcion': 'Un cinturón de cuero de lujo para completar tu atuendo con elegancia.', 'foto': '/static/img/prod48.png'},
    {'id': 49, 'name': 'Máquina de coser Singer', 'categoria': 'electrodomesticos', 'price': 60000, 'quantity': 4, 'descripcion': 'Una máquina de coser Singer para tus proyectos de costura y confección.', 'foto': '/static/img/prod49.png'},
    {'id': 50, 'name': 'Smartphone Samsung Galaxy S22', 'categoria': 'tecnologia', 'price': 950000, 'quantity': 3, 'descripcion': 'El último smartphone Samsung Galaxy S22 con pantalla AMOLED y potente rendimiento.', 'foto': '/static/img/prod50.png'},
    {'id': 51, 'name': 'Cocina de inducción Whirlpool', 'categoria': 'electrodomesticos', 'price': 850000, 'quantity': 2, 'descripcion': 'Una cocina de inducción Whirlpool con controles táctiles para una cocción precisa.', 'foto': '/static/img/prod51.png'},
    {'id': 52, 'name': 'Bicicleta de carretera Cannondale', 'categoria': 'deportes', 'price': 1800000, 'quantity': 3, 'descripcion': 'Una bicicleta de carretera Cannondale para ciclistas apasionados y competidores.', 'foto': '/static/img/prod52.png'},
    {'id': 53, 'name': 'Vestido de novia deslumbrante', 'categoria': 'moda', 'price': 300000, 'quantity': 4, 'descripcion': 'Un vestido de novia deslumbrante para tu día especial.', 'foto': '/static/img/prod53.png'},
    {'id': 54, 'name': 'Juego de llaves de tubo', 'categoria': 'herramientas', 'price': 70000, 'quantity': 6, 'descripcion': 'Un juego completo de llaves de tubo para trabajos de fontanería y reparaciones.', 'foto': '/static/img/prod54.png'},
    {'id': 55, 'name': 'Vestido de verano para hombres', 'categoria': 'indumentaria', 'price': 85000, 'quantity': 5, 'descripcion': 'Un vestido de verano ligero y cómodo para hombres.', 'foto': '/static/img/prod5.png5'},
    {'id': 56, 'name': 'Horno eléctrico KitchenAid', 'categoria': 'electrodomesticos', 'price': 120000, 'quantity': 3, 'descripcion': 'Un horno eléctrico KitchenAid para hornear y asar tus platos favoritos.', 'foto': '/static/img/prod56.png'},
    {'id': 57, 'name': 'Balón de baloncesto Spalding', 'categoria': 'deportes', 'price': 45000, 'quantity': 8, 'descripcion': 'Un balón de baloncesto Spalding de alta calidad para tus partidos en la cancha.', 'foto': '/static/img/prod57.png'},
    {'id': 58, 'name': 'Bolso de cuero para hombres', 'categoria': 'moda', 'price': 150000, 'quantity': 7, 'descripcion': 'Un bolso de cuero para hombres con un diseño elegante y funcionalidad.', 'foto': '/static/img/prod58.png'},
    {'id': 59, 'name': 'Set de herramientas de fontanería', 'categoria': 'herramientas', 'price': 60000, 'quantity': 4, 'descripcion': 'Un set de herramientas de fontanería esenciales para reparaciones en el hogar.', 'foto': '/static/img/prod59.png'},
    {'id': 60, 'name': 'Jersey de lana para mujeres', 'categoria': 'indumentaria', 'price': 75000, 'quantity': 5, 'descripcion': 'Un jersey de lana cálido y elegante para mujeres.', 'foto': '/static/img/prod60.png'},
    {'id': 61, 'name': 'Lavavajillas de acero inoxidable', 'categoria': 'electrodomesticos', 'price': 850000, 'quantity': 4, 'descripcion': 'Un lavavajillas de acero inoxidable de alta gama para una limpieza eficiente.', 'foto': '/static/img/prod61.png'},
    {'id': 62, 'name': 'Raqueta de tenis Babolat', 'categoria': 'deportes', 'price': 120000, 'quantity': 6, 'descripcion': 'Una raqueta de tenis Babolat con tecnología de vanguardia para mejorar tu juego.', 'foto': '/static/img/prod62.png'},
    {'id': 63, 'name': 'Vestido de noche deslumbrante', 'categoria': 'moda', 'price': 250000, 'quantity': 3, 'descripcion': 'Un vestido de noche deslumbrante con detalles elegantes para ocasiones especiales.', 'foto': '/static/img/prod63.png'},
    {'id': 64, 'name': 'Set de herramientas de electricista', 'categoria': 'herramientas', 'price': 70000, 'quantity': 2, 'descripcion': 'Un set de herramientas de electricista con aislamiento para trabajos seguros.', 'foto': '/static/img/prod64.png'},
    {'id': 65, 'name': 'Chaqueta de invierno para hombres', 'categoria': 'indumentaria', 'price': 130000, 'quantity': 4, 'descripcion': 'Una chaqueta de invierno cálida y resistente para hombres.', 'foto': '/static/img/prod65.png'},
    {'id': 66, 'name': 'Robot de cocina KitchenAid', 'categoria': 'electrodomesticos', 'price': 180000, 'quantity': 3, 'descripcion': 'Un robot de cocina KitchenAid para preparar una amplia variedad de platos.', 'foto': '/static/img/prod66.png'},
    {'id': 67, 'name': 'Pelota de tenis Dunlop', 'categoria': 'deportes', 'price': 40000, 'quantity': 8, 'descripcion': 'Una pelota de tenis Dunlop de calidad para tus partidos en la pista.', 'foto': '/static/img/prod67.png'},
    {'id': 68, 'name': 'Bolso de viaje elegante', 'categoria': 'moda', 'price': 120000, 'quantity': 6, 'descripcion': 'Un bolso de viaje elegante y espacioso para tus aventuras.', 'foto': '/static/img/prod68.png'},
    {'id': 69, 'name': 'Set de herramientas de fontanería', 'categoria': 'herramientas', 'price': 60000, 'quantity': 5, 'descripcion': 'Un set de herramientas de fontanería de alta calidad para reparaciones eficientes.', 'foto': '/static/img/prod69.png'},
    {'id': 70, 'name': 'Vestido de verano para niñas', 'categoria': 'moda', 'price': 35000, 'quantity': 7, 'descripcion': 'Un vestido de verano colorido y divertido para niñas.', 'foto': '/static/img/prod70.png'},
    {'id': 71, 'name': 'Cafetera espresso Breville', 'categoria': 'electrodomesticos', 'price': 150000, 'quantity': 4, 'descripcion': 'Una cafetera espresso Breville para preparar café de alta calidad en casa.', 'foto': '/static/img/prod71.png'},
    {'id': 72, 'name': 'Balón de fútbol Nike', 'categoria': 'deportes', 'price': 40000, 'quantity': 10, 'descripcion': 'Un balón de fútbol Nike para tus partidos en el campo.', 'foto': '/static/img/prod72'},
    {'id': 73, 'name': 'Bufanda de moda para mujeres', 'categoria': 'indumentaria', 'price': 25000, 'quantity': 9, 'descripcion': 'Una bufanda de moda para mujeres que agrega estilo a tu atuendo.', 'foto': '/static/img/prod73'},
    {'id': 74, 'name': 'Set de herramientas de albañilería', 'categoria': 'herramientas', 'price': 70000, 'quantity': 6, 'descripcion': 'Un set de herramientas de albañilería esenciales para proyectos de construcción.', 'foto': '/static/img/prod74'},
    {'id': 75, 'name': 'Mochila de cuero elegante', 'categoria': 'moda', 'price': 80000, 'quantity': 5, 'descripcion': 'Una mochila de cuero elegante para llevar tus pertenencias con estilo.', 'foto': '/static/img/prod75'},
    {'id': 76, 'name': 'Aspiradora sin bolsa Dyson', 'categoria': 'electrodomesticos', 'price': 60000, 'quantity': 8, 'descripcion': 'Una aspiradora sin bolsa Dyson con potente succión para una limpieza eficiente.', 'foto': '/static/img/prod76'},
    {'id': 77, 'name': 'Guantes de béisbol Rawlings', 'categoria': 'deportes', 'price': 25000, 'quantity': 10, 'descripcion': 'Guantes de béisbol Rawlings de alta calidad para un rendimiento excepcional en el campo.', 'foto': '/static/img/prod77'},
    {'id': 78, 'name': 'Collar de moda para mujeres', 'categoria': 'indumentaria', 'price': 30000, 'quantity': 9, 'descripcion': 'Un collar de moda para mujeres que agrega un toque elegante a tu estilo.', 'foto': '/static/img/prod78'},
    {'id': 79, 'name': 'Set de herramientas de jardinería', 'categoria': 'herramientas', 'price': 70000, 'quantity': 7, 'descripcion': 'Un set de herramientas de jardinería completo para cuidar de tu jardín y plantas.', 'foto': '/static/img/prod79'},
    {'id': 80, 'name': 'Smart TV Samsung 65 pulgadas', 'categoria': 'tecnologia', 'price': 2000000, 'quantity': 2, 'descripcion': 'Un Smart TV Samsung de 65 pulgadas con una increíble calidad de imagen para una experiencia de visualización inmersiva.', 'foto': '/static/img/prod80'},
    {'id': 81, 'name': 'Lavadora y secadora LG', 'categoria': 'electrodomesticos', 'price': 1800000, 'quantity': 3, 'descripcion': 'Una lavadora y secadora LG en un solo aparato para ahorrar espacio y tiempo en tu rutina de lavandería.', 'foto': '/static/img/prod81'},
    {'id': 82, 'name': 'Bicicleta de montaña Specialized', 'categoria': 'deportes', 'price': 2100000, 'quantity': 4, 'descripcion': 'Una bicicleta de montaña Specialized con suspensión de alto rendimiento para enfrentar terrenos difíciles.', 'foto': '/static/img/prod82'},
    {'id': 83, 'name': 'Vestido de fiesta exquisito', 'categoria': 'moda', 'price': 280000, 'quantity': 5, 'descripcion': 'Un vestido de fiesta exquisito con detalles únicos para destacar en eventos especiales.', 'foto': '/static/img/prod83'},
    {'id': 84, 'name': 'Juego de destornilladores de precisión', 'categoria': 'herramientas', 'price': 35000, 'quantity': 6, 'descripcion': 'Un juego de destornilladores de precisión para trabajos delicados y electrónica.', 'foto': '/static/img/prod84'},
    {'id': 85, 'name': 'Blusa de seda para mujeres', 'categoria': 'indumentaria', 'price': 75000, 'quantity': 7, 'descripcion': 'Una blusa de seda elegante y cómoda para mujeres.', 'foto': '/static/img/prod85'},
    {'id': 86, 'name': 'Microondas de acero inoxidable', 'categoria': 'electrodomesticos', 'price': 75000, 'quantity': 2, 'descripcion': 'Un microondas de acero inoxidable con múltiples funciones para calentar y cocinar.', 'foto': '/static/img/prod86'},
    {'id': 87, 'name': 'Balón de rugby Gilbert', 'categoria': 'deportes', 'price': 45000, 'quantity': 8, 'descripcion': 'Un balón de rugby Gilbert de alta calidad para partidos y entrenamientos.', 'foto': '/static/img/prod87'},
    {'id': 88, 'name': 'Vestido de noche elegante', 'categoria': 'moda', 'price': 220000, 'quantity': 6, 'descripcion': 'Un vestido de noche elegante y sofisticado para ocasiones especiales.', 'foto': '/static/img/prod88'},
    {'id': 89, 'name': 'Set de herramientas de electricista', 'categoria': 'herramientas', 'price': 60000, 'quantity': 5, 'descripcion': 'Un set de herramientas de electricista con aislamiento para trabajos seguros.', 'foto': '/static/img/prod89'},
    {'id': 90, 'name': 'Jersey de lana para hombres', 'categoria': 'indumentaria', 'price': 80000, 'quantity': 9, 'descripcion': 'Un jersey de lana cálido y acogedor para hombres.', 'foto': '/static/img/prod90'},
    {'id': 91, 'name': 'Cocina de gas LG', 'categoria': 'electrodomesticos', 'price': 180000, 'quantity': 4, 'descripcion': 'Una cocina de gas LG para cocinar tus platos favoritos con precisión.', 'foto': '/static/img/prod91'},
    {'id': 92, 'name': 'Set de herramientas de carpintería', 'categoria': 'herramientas', 'price': 70000, 'quantity': 6, 'descripcion': 'Un conjunto de herramientas de carpintería esenciales para tus proyectos de bricolaje.', 'foto': '/static/img/prod92'},
    {'id': 93, 'name': 'Sombrero de moda para hombres', 'categoria': 'indumentaria', 'price': 35000, 'quantity': 8, 'descripcion': 'Un sombrero de moda para hombres que agrega estilo a tu atuendo.', 'foto': '/static/img/prod93'},
    {'id': 94, 'name': 'Mesa de picnic plegable', 'categoria': 'herramientas', 'price': 70000, 'quantity': 5, 'descripcion': 'Una mesa de picnic plegable para disfrutar al aire libre.', 'foto': '/static/img/prod94'},
    {'id': 95, 'name': 'Lavavajillas Samsung', 'categoria': 'electrodomesticos', 'price': 900000, 'quantity': 4, 'descripcion': 'Un lavavajillas Samsung para una limpieza eficiente de tus platos y utensilios.', 'foto': '/static/img/prod95'},
    {'id': 96, 'name': 'Botas de fútbol Nike', 'categoria': 'deportes', 'price': 60000, 'quantity': 7, 'descripcion': 'Botas de fútbol Nike de alta calidad para un rendimiento excepcional en el campo.', 'foto': '/static/img/prod96'},
    {'id': 97, 'name': 'Bufanda de lana de moda', 'categoria': 'moda', 'price': 25000, 'quantity': 8, 'descripcion': 'Una bufanda de lana de moda para mantenerte abrigado y con estilo en el invierno.', 'foto': '/static/img/prod97'},
    {'id': 98, 'name': 'Set de herramientas de jardinería', 'categoria': 'herramientas', 'price': 40000, 'quantity': 9, 'descripcion': 'Un set de herramientas de jardinería completo para cuidar de tu jardín y plantas.', 'foto': '/static/img/prod98'},
    {'id': 99, 'name': 'Jersey deportivo para hombres', 'categoria': 'indumentaria', 'price': 35000, 'quantity': 10, 'descripcion': 'Un jersey deportivo para hombres que combina comodidad y estilo en tus actividades físicas.', 'foto': '/static/img/prod99'}]
