def main():
  camel = input('camelCase: ')
  snake = from_camel_to_snake(camel)
  print(f'snake_case: {snake}')

def from_camel_to_snake(camel):
  camel_letters = list(camel)

  for index in range(len(camel_letters)):
    if camel_letters[index].isupper():
      camel_letters[index] = '_{0}'.format(camel_letters[index].lower())

  return ''.join(camel_letters)

main()