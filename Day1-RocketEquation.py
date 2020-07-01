def calculate_fuel_requirements(filename):
    with open(filename, 'r') as file:
        content = file.read()
    masses = map(int, content.split('\n'))
    fuel_requirements = [item // 3 - 2 for item in masses]
    print(sum(fuel_requirements))


calculate_fuel_requirements('fuel.txt')
