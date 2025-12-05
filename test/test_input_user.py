from src.input_user import color_input
import pytest

colores = [
            "rojo",
            "azul",
            "verde",
            "amarillo",
            "morado",
            "naranja",
        ]

@pytest.mark.test_input_color
def test_color_input_exits_program():
    with pytest.raises(SystemExit): color_input(["rojo",
            "añul",
            "verde",
            "amarillo"])
    with pytest.raises(SystemExit): color_input(["rojo",
            "azul",
            "verde",
            "amarillo","morado"])