from colorama import init, Fore, Style
init()

def return_colors(colors_list):
    colors_representation = {
        "rojo" : Fore.RED + "●" + Style.RESET_ALL,
        "azul" : Fore.BLUE + "●" + Style.RESET_ALL,
        "verde" : Fore.GREEN + "●" + Style.RESET_ALL,
        "amarillo" : Fore.YELLOW + "●" + Style.RESET_ALL,
        "morado" : Fore.MAGENTA + "●" + Style.RESET_ALL,
        "blanco" : Fore.WHITE + "●" + Style.RESET_ALL
    } 

    #Devuelve los cores en forma de string para ser represntado por el terminal
    return " ".join([colors_representation[color] for color in colors_list])


if __name__ == "__main__":
    print(return_colors(["rojo","azul","verde","amarillo"]))
    print(return_colors(["rojo","azul","morado","blanco"]))