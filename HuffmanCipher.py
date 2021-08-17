from HuffmanEntropy import countletters, HuffmanTree
def Parametros():
    p = int(input("Ingresa p: "))
    q = int(input("Ingresa q: "))
    n = p*q
    lamb_n = lcm(p - 1, q - 1)
    print(lamb_n)
    e = int(input("Ingresa e: "))
    while(lamb_n < e and gcd(e, lamb_n) != 1):
        e = input("Ingresa e: ")
    a = e
    b = lamb_n
    if b == 0:
        z, d, y = a, 1, 0
    x_2, x_1, y_2, y_1 = 1, 0, 0, 1
    while(b > 0):
        q, r = a // b, a % b
        d, y = x_2 - q*x_1, y_2 - q*y_1
        a, b, x_2, x_1, y_2, y_1 = b, r, x_1, d, y_1, y
    z, d, y = a, x_2, y_2
    if d < 0:
        d = lamb_n + d
    Key = (n, e, d)
    print("Valores:", "n =", n, "e =", e, "d =", d)
    print("Llave secreta:", Key)
    return Key
def Encrypt(PlainText, Key):
    Codigo = H.Coding(PlainText)
    cut = 15 - (len(Codigo) % 15)
    CodigoPack = "0"*(cut) + Codigo
    CodigoBlocks = ["1" + CodigoPack[i:i+15] for i in range(0, len(CodigoPack), 15)]
    CodigoBlocks[0] = CodigoBlocks[0][0] + CodigoBlocks[0][cut + 1:]
    print(PlainText, ":", CodigoBlocks)
    P = [H.BinToDec(code) for code in CodigoBlocks]
    print(P)
    CipherBlock = []
    for codes in P:
        C = 1
        for bit in H.DecToBin(Key[1]):
            C = (C**2) % Key[0]
            if bit == "1":
                C = (C*codes) % Key[0]
        CipherBlock.append(C)
    return CipherBlock
def Decrypt(CipherText):
    print("Ingresar datos de llave: ")
    p = int(input("Ingresa n: "))
    e = int(input("Ingresa e: "))
    d = int(input("Ingresa d: "))
    DecipherText = []
    for codes in CipherText:
        P = 1
        for bit in H.DecToBin(d):
            P = P**2 % p
            if bit == "1":
                P = P*codes % p
        DecipherText.append(P)
    Decodigo = ["".join(H.DecToBin(DT)) for DT in DecipherText]
    newDecodigos = []
    for d in Decodigo:
        h = list(d).copy()
        h.pop(0)
        j = "".join(h)
        newDecodigos.append(j)
    print(newDecodigos)
    return "".join(newDecodigos)
def lcm(x, y):
    return x * y / gcd(x, y)
def gcd(x, y):
    return x if not y else gcd(y, x % y)
filename = "LongText.txt"
file = open(filename, encoding="utf8")
Frecuencias, total = countletters(file)
H = HuffmanTree(Frecuencias)
Codigos = H.HuffmanCodes(True)
print("Longitud del mensaje:", total)
alpha = len(Frecuencias)
print("Longitud de alfabeto:", alpha)
print("Histograma y codificación:")
for k,v in Frecuencias.items():
    print(k,":",v,":",Codigos[k])
Mensaje = input("Ingresar mensaje: ")
Llave = Parametros()
TextoCifrado = Encrypt(Mensaje, Llave)
print(TextoCifrado)
TextoDecifrado = Decrypt(TextoCifrado)
print(H.Decoding(TextoDecifrado))
