s = "abrir = to open\n"
stem = "abr"
enStem = "open"
esObj = "la ventara"
enObj = "the window"

esEnd = ['o', 'es', 'ís', 'e', 'imos', 'en']
pronoun = ['I', 'you (informal)', 'you (vosotros)', 'he', 'we', 'they']
enEnd = {'e':'s'}
for i in range(len(esEnd)):
    enEnding = ''
    if esEnd[i] in enEnd:
        enEnding = enEnd[esEnd[i]]
    s += f"{stem}{esEnd[i]} {esObj} = {pronoun[i]} {enStem}{enEnding} {enObj}\n"
open("temp.txt", "w", encoding="utf-8").write(s)
