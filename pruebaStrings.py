hola = ["10101","010101", "0101"]
newHola = []
for d in hola:
    h = list(d).copy()
    h.pop(0)
    j = "".join(h)
    newHola.append(j)
print(newHola)
