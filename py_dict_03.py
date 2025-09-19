contacts = [
    {
        'id': 1,
        'first_name': 'Pero',
        'last_name': 'Peric',
        'email': 'pero.peric@email.com'
    },
    {
        'id': 2,
        'first_name': 'Ana',
        'last_name': 'Anic',
        'email': 'ana.anic@email.com'
    }
]
print()

for contact in contacts:
    # # print(contact)
    # for key in contact.keys():
    #     print(key)
    
    # for value in contact.values():
    #     print(value)

    for key, value in contact.items():
        # print(key, value)
        print(f'{key.upper():<12}{value:<25}')

    print()

