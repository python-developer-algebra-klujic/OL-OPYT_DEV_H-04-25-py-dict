person = {
    'id': 1,
    'first_name': 'Perota',
    'last_name': 'Peric',
    'email': 'pero.peric@email.com'
}

print(person)

# dodavanje elementa u rjecnik
person['oib'] = '12345678901'
print(person)

# promjena elementa u rjecnik
person['first_name'] = 'Pero'
print(person)

# dohvat podataka
person_email = person['email']
print(person_email)
print(person)


# dodavanje
person['id'] = 2

# dohvat
person_id = person['id']
