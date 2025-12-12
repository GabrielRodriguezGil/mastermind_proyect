
def check_colors(color_combination , solution):
    successe_percentage = 0
    for position, color in enumerate(color_combination):
        if color == solution[position]:
            successe_percentage += 3
        elif color in solution:
            successe_percentage += 2
        else:
            successe_percentage += 1
            
    return successe_percentage

