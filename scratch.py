acronyms = ['LOL', 'IDK', 'SMH', 'TBH']

for acronym in acronyms:
    print(acronym)
    
acronymsDict = {
    'LOL': 'laugh out loud',
    'IDN': 'I don\'t know'
}

definitionBtw = acronymsDict.get('BTW')
definitionLol = acronymsDict.get('LOL')

print('BTW:', definitionBtw)
print('LOL:', definitionLol)
print(acronymsDict)
