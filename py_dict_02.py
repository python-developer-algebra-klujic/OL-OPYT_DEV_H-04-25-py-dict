contacts = []
id = 0


while True:
    person = {}
    id += 1

    person['id'] = id
    person['first_name'] = input('Upisite ime kontakta: ')
    person['last_name'] = input('Upisite prezime kontakta: ')
    person['email'] = input('Upisite email kontakta: ')
    person['phone'] = input('Upisite broj telefona kontakta: ')

    print(person)
    contacts.append(person)

    next_person = input('Zelite li unijeti novi kontakt? (Da/Ne): ')
    if next_person.lower() != 'da':
        break


print()
print(contacts)
print()
