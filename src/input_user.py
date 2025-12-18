def color_input():
    user_input = (
        input(
            "Introduce 4 colores separados por espacios de estos(rojo, azul, verde, amarillo, morado, blanco): "
        )
        .lower()
        .split()
    )

    colors = ["rojo", "azul", "verde", "amarillo", "morado", "blanco"]
    colors_set = set(colors)

    user_input_set = set(user_input)
    if not user_input_set.issubset(colors_set) or len(user_input) != 4:
        raise SystemExit("No has puesto valores correctos")

    else:
        return user_input


color_input()
