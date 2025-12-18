# This module only works when color_input takes a parameter, made by the system
# from src.input_user import color_input
# import pytest
#
# colores = [
#    "rojo",
#    "azul",
#    "verde",
#    "amarillo",
#    "morado",
#    "blanco",
# ]
#
#
# @pytest.mark.test_input_color_exits
# def test_color_input_exits_program():
#    with pytest.raises(SystemExit):
#        color_input(["rojo", "añul", "verde", "amarillo"])
#    with pytest.raises(SystemExit):
#        color_input(["rojo", "azul", "verde", "amarillo", "morado"])
#
#
# @pytest.mark.test_input_color_runs
# def test_color_input_runs():
#    assert color_input(["rojo", "azul", "verde", "amarillo"]) == [
#        "rojo",
#        "azul",
#        "verde",
#        "amarillo",
#    ]
#
