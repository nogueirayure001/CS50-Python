def convert_mass_to_joules(mass):
  light_speed = 300000000;
  return mass * (light_speed * light_speed)

def main():
  mass = int(input('Enter a mass (kg): '))
  joules = convert_mass_to_joules(mass)
  print(f'{mass} kg equals {joules} joules')

main()