
def check_colors(color_combination , solution):
    color_combination_copy = color_combination[:]
    solution_copy = solution[:]
    success_percentage = 0
    right_color = []

    for position, color in enumerate(color_combination_copy):
        if color == solution_copy[position]:
            success_percentage += 2
            solution_copy[position] = None
            color_combination_copy[position] = "None"
        

    for color in color_combination_copy:
        if color in solution_copy and color not in right_color:
            success_percentage += 2
            right_color.append(color)
        else:
            success_percentage += 1
            
    return success_percentage


if __name__ == "__main__":
    check_colors(["r","r","a","a"],["r","r","v","v"])