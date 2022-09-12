s = "absolver = to absolve, to acquit\n"
stem = "absuelv"
enStem = "absolve"
esObj = "el criminal"
enObj = "the criminal"

esEnd = ['o', 'es', 'éis', 'e', 'emos', 'en']
pronoun = ['I', 'you (informal)', 'you (vosotros)', 'he', 'we', 'they']
enEnd = {'e': 's'}
for i in range(len(esEnd)):
    enEnding = ''
    if esEnd[i] in enEnd:
        enEnding = enEnd[esEnd[i]]
    s += f"{stem}{esEnd[i]} {esObj} = {pronoun[i]} {enStem}{enEnding} {enObj}\n"
open("temp.txt", "w", encoding="utf-8").write(s)
