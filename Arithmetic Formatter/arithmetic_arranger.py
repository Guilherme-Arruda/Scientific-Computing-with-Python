def arithmetic_arranger(problems, solution=False):

  if len(problems) > 5:
    return 'Error: Too many problems.'

  top, bottom, dashes, final = [], [], [], []

  for i in range(len(problems)):
    problem = problems[i].split()

    firstNumber = problem[0]
    operator = problem[1]
    secondNumber = problem[2]

    if not firstNumber.isdigit() or not secondNumber.isdigit():
      return 'Error: Numbers must only contain digits.'

    if len(firstNumber) > 4 or len(secondNumber) > 4:
      return 'Error: Numbers cannot be more than four digits.'

    if operator == '+':
      result = int(firstNumber) + int(secondNumber)
    elif operator == '-':
      result = int(firstNumber) - int(secondNumber)
    else:
      return "Error: Operator must be '+' or '-'."

    distance = max(len(firstNumber), len(secondNumber)) + 2

    top.append(firstNumber.rjust(distance))
    bottom.append(operator + ' ' + secondNumber.rjust(distance - 2))
    dashes.append('-' * (distance))
    final.append(str(result).rjust(distance))

  if solution == True:
    return '    '.join(top) + '\n' + '    '.join(bottom) + '\n' + '    '.join(dashes) + '\n' + '    '.join(final)
  else:
    return '    '.join(top) + '\n' + '    '.join(bottom) + '\n' + '    '.join(dashes)
