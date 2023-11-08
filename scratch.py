# jupyter notebook

import camelcase
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

acronym = 'BTW'
try:
    def1 = acronymsDict[acronym]
    print('Definition of', acronym, 'is', def1)
except:
    print('The key ', acronym, 'does not exist')
finally:
    print('The acronyms we have defined are:')
    for x in acronymsDict:
        print(x)

print('The program keeps going...')

c = camelcase.CamelCase()
s = 'how are you here?'
print(c.hump(s))