def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    firstLine = []
    secondLine = []
    dashesLine = []
    answersLine = []

    for calc in problems:
        separator = calc.split(' ')
        firstOperand = separator[0]
        secondOperand = separator[2]
        operator = separator[1]

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not firstOperand.isdigit() or not secondOperand.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(firstOperand) > 4 or len(secondOperand) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        space = max(len(firstOperand), len(secondOperand))
        
        firstLine.append(f'{firstOperand:>{space+2}}')
        secondLine.append(f'{operator} {secondOperand:>{space}}')
        dashesLine.append('-' * (space+2))

        if show_answers:
            if operator == '+':
                answer = int(firstOperand) + int(secondOperand)
            elif operator == '-':
                answer = int(firstOperand) - int(secondOperand)

            answersLine.append(f'{(answer):>{space+2}}')

    if answersLine != []:
        result = (f"{'    '.join(firstLine)}\n{'    '.join(secondLine)}\n{'    '.join(dashesLine)}\n{'    '.join(answersLine)}") 
    else:
        result = f"{'    '.join(firstLine)}\n{'    '.join(secondLine)}\n{'    '.join(dashesLine)}"
    
    return result

print(f'arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)')

print('   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028')
