invoice = {
    'id': 1,
    'number': '00001-1-2025',
    'date': '19.09.2025.',
    'items': [
        {
            'number': 1,
            'description': 'Loerm ipsum dolor sit ...',
            'amount': 5,
            'unit_price': 9.99,
            'discount': 0.0,
            'total': 50.99 # izraccunati cijenu
        }
    ],
    'sub_total': 50.99,
    'tax': 12.59,
    'total': 75.99
}

print(invoice['items']) # dohvatimo element pod kljucem items -> to je lista
print(invoice['items'][0]) # iz liste dohvatimo element pod indeksom 0 -> rjecnik
print(invoice['items'][0]['total']) # iz rjecnika dohvatimo element pod kljucem -> to je float
