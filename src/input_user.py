def color_input():
    user_input = [
        i.lower
        for i in input(
            "Introduce los cuatro colores que quieras dentro de estos colores: "
            "Rojo, Azul, Verde, Amarillo, Morado, Naranja: "
        ).split(" ")
    ]

    if (
        any(user_input)
        not in [
            "rojo",
            "azul",
            "verde",
            "amarillo",
            "morado",
            "naranja",
        ]
        or len(user_input) != 4
    ):
        raise ValueError("No has puesto valores correctos")

    return user_input
