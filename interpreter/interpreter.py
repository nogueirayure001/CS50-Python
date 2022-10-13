def main():
  expression = input('Expression: ')
  result = calculate_expression(expression)
  print(f'{result:.1f}')

def calculate_expression(expression):
  n1_str, op_str, n2_str = expression.split(' ')

  n1 = int(n1_str)
  n2 = int(n2_str)

  match(op_str):
    case '+':
      return n1 + n2
    case '-':
      return n1 - n2
    case '*':
      return n1 * n2
    case '/':
      return n1 / n2

main()