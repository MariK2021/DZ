countries = ("Ukraine", "Spain", "Italy")
adress= {
    countries[0]: 'Kyiv',
    countries[1]: 'Madrid',
    countries[2]: 'Rome'
}

for key, value in adress.items():
    print(key + ": " + value)

