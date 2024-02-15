import random
import plotly.graph_objects as go

# Elementos disponibles y sus combinaciones
elementos = [
    'oveja', 'lingote de oro', 'libro de reclamaciones', 'ansiedad', 'ordenador'
]

combinaciones = {
    ('oveja', 'lingote de oro'): 'Barba de metal',
    ('oveja', 'libro de reclamaciones'): 'Ballet de protestas',
    ('oveja', 'ansiedad'): 'Peluca de lana nerviosa',
    ('oveja', 'ordenador'): 'Código de balido',
    ('lingote de oro', 'libro de reclamaciones'): 'Documento dorado de quejas',
    ('lingote de oro', 'ansiedad'): 'Moneda de estrés',
    ('lingote de oro', 'ordenador'): 'Teclado de lingotes',
    ('libro de reclamaciones', 'ansiedad'): 'Registro de preocupaciones',
    ('libro de reclamaciones', 'ordenador'): 'Pantalla de quejas digitales',
    ('ansiedad', 'ordenador'): 'Virus de nerviosismo'
}

# Generar combinaciones bidireccionales
combinaciones_bidireccionales = {}
for combinacion, resultado in combinaciones.items():
    combinaciones_bidireccionales[combinacion] = resultado
    combinaciones_bidireccionales[(combinacion[1], combinacion[0])] = resultado

def combinar_elementos(elemento1, elemento2):
    combinacion = (elemento1, elemento2)
    if combinacion in combinaciones_bidireccionales:
        return combinaciones_bidireccionales[combinacion]
    else:
        return "¡Oops! Parece que esa combinación no produce nada interesante."

def juego_alquimia():
    print("¡Bienvenido al juego de alquimia!")
    print("Puedes combinar los siguientes elementos:")
    for elemento in elementos:
        print("-", elemento)
    print("")

    conteo_categorias = {'Desconocido': 0}  # Inicializar conteo de categorías
    conteo_combinaciones = {}  # Inicializar conteo de combinaciones

    while True:
        elemento1 = input("Elige el primer elemento: ").lower()
        elemento2 = input("Elige el segundo elemento: ").lower()

        if elemento1 in elementos and elemento2 in elementos:
            resultado = combinar_elementos(elemento1, elemento2)
            print(f"\n¡Has combinado {elemento1} y {elemento2}!")
            print(f"¡El resultado es: {resultado}!\n")

            # Obtener la categoría del resultado
            categoria_resultante = random.choice(['Absurdo', 'Divertido', 'Sorprendente'])
            print(f"El nuevo elemento pertenece a la categoría: {categoria_resultante}")

            # Actualizar los datos para la visualización
            conteo_categorias[categoria_resultante] = conteo_categorias.get(categoria_resultante, 0) + 1

            # Registrar la combinación
            combinacion_actual = tuple(sorted([elemento1, elemento2]))
            conteo_combinaciones[combinacion_actual] = conteo_combinaciones.get(combinacion_actual, 0) + 1

        else:
            print("\n¡Ups! Al menos uno de los elementos no es válido. Inténtalo de nuevo.\n")

        continuar = input("¿Quieres seguir combinando elementos? (s/n): ").lower()
        if continuar != 's':
            print("\n¡Gracias por jugar! ¡Hasta la próxima!")
            break

    # Crear visualización de datos
    categorias_grafica = list(conteo_categorias.keys())
    conteos_categorias = list(conteo_categorias.values())

    # Agregar elementos combinados al gráfico
    etiquetas_combinaciones = [f"{', '.join(comb)} ({conteo})" for comb, conteo in conteo_combinaciones.items()]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=categorias_grafica, y=conteos_categorias, name='Categorías'))
    fig.add_trace(go.Scatter(x=categorias_grafica, y=conteos_categorias,
                             mode='markers+text',
                             text=etiquetas_combinaciones,
                             textposition="top center",
                             marker=dict(size=12),
                             showlegend=False))

    fig.update_layout(barmode='group', title='Distribución de Categorías y Elementos Combinados')
    fig.show()

# Iniciar el juego
juego_alquimia()

