# Main draft for the game

import random

# Diccionario de combinaciones: cada clave es una tupla de elementos y el valor es el resultado de la combinación
combinaciones = {
    ('oveja', 'lingote de oro'): 'abogado recién licenciado',
    ('zanahoria', 'computadora'): 'pizza de zanahoria',
    ('unicornio', 'helado'): 'sirena congelada',
    ('espada', 'piedra'): 'canción épica',
    ('café', 'libro'): 'teletransportador de papel',
    ('dragón', 'plátano'): 'barco volador',
    ('panda', 'cohete'): 'lámpara mágica, no tan mágica',
    ('espárrago', 'guitarra eléctrica'): 'anguila vegetariana',
    ('banana', 'sombrero de copa'): 'mono elegante',
    ('unicornio', 'pasta de dientes'): 'sonrisa mágica',
    ('sandía', 'martillo'): 'batidora gigante',
    ('plátano', 'piano'): 'sinfonía frutal',
    ('pingüino', 'teléfono'): 'llamada antártica',
    ('cactus', 'café'): 'desierto energético',
    ('espejo', 'queso'): 'reflejo delicioso',
    ('tiburón', 'globo aerostático'): 'paseo acuático',
    ('silla', 'fresa'): 'sabor a asiento',
    ('araña', 'pantalones vaqueros'): 'tejido arácnido',
    ('dinosaurio', 'paraguas'): 'era jurásica lluviosa',
    ('elefante', 'trampolín'): 'circo aéreo',
    ('mariposa', 'silla de ruedas'): 'vuelo asistido',
    ('agua', 'guitarra'): 'melodía acuática',
    ('pizza', 'catapulta'): 'lunch volador',
    ('gato', 'paracaídas'): 'aterrizaje en cuatro patas',
    ('dragón', 'cámara de fotos'): 'selfie ardiente',
    ('pirata', 'globos de colores'): 'fiesta en alta mar',
    ('tostadora', 'mariposa'): 'tostada voladora',
    ('abeja', 'parlante'): 'zumbido musical',
    ('castillo', 'papel higiénico'): 'mazmorra higiénica',
    ('caballo', 'caja fuerte'): 'robo galopante',
    ('botella de vino', 'robot'): 'inteligencia artificial etílica',
    ('caramelo', 'heladera'): 'dulce congelado',
    ('camello', 'saxofón'): 'jazz del desierto',
    ('sombrero', 'trampolín'): 'salto elegante',
    ('sushi', 'paraguas'): 'lluvia de sabor',
    ('zapatilla', 'cohetes'): 'carrera espacial',
    ('cerdo', 'piano'): 'sonata de cerdo',
    ('lagarto', 'teléfono móvil'): 'llamada reptiliana',
    ('elefante', 'globo'): 'vuelo paquidermo',
    ('robot', 'sandía'): 'tecnología frutal',
    ('pastel', 'lanzallamas'): 'fogata dulce',
    ('gato', 'helado'): 'miau frío',
    ('cerebro', 'bolígrafo'): 'idea escrita',
    ('monstruo', 'cafetera'): 'café monstruoso',
    ('dragón', 'microondas'): 'fuego a alta velocidad',
    ('libro', 'tobogán'): 'lectura emocionante',
    ('lámpara', 'pingüino'): 'luz antártica',
    ('delfín', 'helicóptero'): 'acrobacias marinas',
    ('radio', 'mariposa'): 'ondas aladas',
    ('galleta', 'paracaídas'): 'vuelo con sabor',
    ('foca', 'cohete'): 'salto interestelar',
    ('cohete', 'plátano'): 'comida espacial',
    ('hamburguesa', 'cometa'): 'sabor cósmico',
    ('avión', 'paraguas'): 'vuelo protegido',

}

def juego_alquimia():
    print("¡Bienvenido al juego de alquimia surrealista!")
    print("Combina dos elementos básicos para descubrir resultados sorprendentes y divertidos.")
    print("Por ejemplo, 'oveja' + 'lingote de oro' = 'abogado recién licenciado'")
    
    while True:
        input("Presiona Enter para combinar dos elementos...")
        elemento1 = random.choice(list(combinaciones.keys()))[0]
        elemento2 = random.choice(list(combinaciones.keys()))[1]
        
        resultado = combinaciones.get((elemento1, elemento2))
        if not resultado:
            resultado = "¡La combinación no generó ningún resultado! Inténtalo de nuevo."
        
        print(f"¡Has combinado '{elemento1}' y '{elemento2}' y has creado: '{resultado}'!")

# Inicia el juego
juego_alquimia()
