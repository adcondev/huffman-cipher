# %% Definir clases para construir Huffman Tree con Compresor y descompresor
import sys
from collections import defaultdict
from math import log
class HuffmanTree():
    """Estructura de Huffman Tree. Consta de vertices y aristas, además de una cola de prioridad"""
    __slots__ = ("_vertices","_cola","_texto","_frecuencias","_codigos","_simbolos","_root","_decodigos")
    def __init__(self, Texto = "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG'S BACK 1234567890", Frecuencias = {}):
        """Constructor de árbol. Declarará atributos y métodos. Iniciará vacio en vértices. Se puede usar un diccionario con frecuencias
        o se puede obtar por insertar un texto para obtener las frecuencias

        Representación de Arbol como mapa de incidencia Arbol = {Destino:{Origen:Arista}}"""
        self._cola = self.PQ()
        self._vertices = {}
        self._codigos = {}
        self._decodigos = {}
        self._simbolos = []
        if isinstance(Texto, dict):
            self._frecuencias = Texto
            self._texto = ""
            self.Codes(self._frecuencias)
        else:
            self._texto = Texto
            self._frecuencias = Frecuencias
            self.Codes()
    def Coding(self, string):
        """Método para codificar con una frecuencia dada o con un texto dado."""
        code = ""
        for char in string:
            code = code + self._codigos[char]
        return "1" + code
    def Decoding(self, code):
        """Método para decodificar con una frecuencia dada o con un texto dado."""
        binary, key, word = str(code), "", ""
        for bit in binary[1:]:
            key = key + bit
            if key in self._decodigos:
                word = word + self._decodigos[key]
                key = ""
        return word
    def DecToBin(self, number):
        """Convertir de decimal a binario y retornarlo como generador"""
        if(number > 1):
            yield from self.DecToBin(number//2)
        yield str(number%2)
    def Arbol(self, frecs = None):
        """Construye el árbol dado el histograma del texto(Probabilidad de cada carácter), si no hay texto cronstruye por un diccionario de frecuencias"""
        for char, frec in self.Histograma().items() if frecs is None else frecs.items():
            self._cola._Push(self.insertarVertice(frec, char))
        self._simbolos = self._cola._Queue().copy()
        while not self._cola._Empty():
            a = self._cola._Pop()
            b = self._cola._Pop()
            if b is not None:
                c = self.insertarVertice(a._Frecuencia() + b._Frecuencia())
                self.insertarArista(c,a,"0")
                self.insertarArista(c,b,"1")
                self._cola._Push(c)
            else:
                self._root = a
                return self._root
    def Codes(self, frecs = None):
        """Genera los códigos de los símbolos en las hojas dada la raíz del heap."""
        fistNode = self.Arbol(frecs)
        for v in self._simbolos:
            self._codigos[v._Dato()] = ""
            step = v
            while not step == self._root:
                direccion = self._vertices[step]
                for vertice, arista in direccion.items():
                    self._codigos[v._Dato()] = arista._Dato() + self._codigos[v._Dato()]
                    step = vertice
        self._decodigos = {y:x for x,y in self._codigos.items()}
    def Histograma(self):
        """Obtener las probabilidades de cada letra dado un texto"""
        if self._texto is not "":
            total = len(self._texto)
            for keys in self._texto:
                if keys in self._frecuencias:
                    self._frecuencias[keys] = self._frecuencias[keys] + 1.0/total
                else:
                    self._frecuencias[keys] = 1.0/total
        return self._frecuencias
    def HuffmanCodes(self, value = True):
        """Retorna los códigos de Huffman para un texto dado."""
        return self._codigos if value else self._decodigos
    def insertarVertice(self, Frecuencia, Dato = None):
        v = self.Vertices(Frecuencia, Dato)
        self._vertices[v] = {}
        return v
    def insertarArista(self, orig, dest, Dato = None):
        """Inserta y una arista nueva"""
        a = self.Arista(orig, dest, Dato)
        self._vertices[dest][orig] = a
    class Arista():
        """Estructura de arista para grafo"""
        __slots__ = ("_origen","_destino","_elemento")
        def __init__(self, V_Origen, V_Destino, Dato = None):
            """Constructor de arista."""
            self._origen, self._destino, self._elemento = V_Origen, V_Destino, Dato
        def _Dato(self):
            """Retornar valor o etiqueta de arista(función de transformación)"""
            return self._elemento
        def __hash__(self):
            """ Retornarse a si mismo como tupla de incidencia para usarse como llave/valor,
                en diccionario"""
            return hash((self._origen, self._destino))
    class Vertices():
        """Estructura de vertices"""
        __slots__ = ("_elemento","_frecuencia")
        def __init__(self, Frecuencia, Dato = None):
            """Constructor de vértice con dato y frecuencia"""
            self._elemento = Dato
            self._frecuencia = Frecuencia
        def _Dato(self):
            """Retornar dato asociado o etiqueta de vértice"""
            return self._elemento
        def _Frecuencia(self):
            return self._frecuencia
        def __le__(self, otherNode):
            """Forma de evaluación para <="""
            return self._frecuencia <= otherNode._frecuencia
        def __eq__(self, otherNode):
            """Forma de evaluación para =="""
            return self._frecuencia == otherNode._frecuencia
        def __hash__(self):
            """Retornarse a si mismo para usarse como key/set/map."""
            return hash(id(self))
    class PQ:
        """Clase de cola de prioridad"""
        __slots__ = ("_queue","_orden","_duplis")
        def __init__(self, Ord = True, Dup = True):
            self._queue = []
            self._orden = Ord
            self._duplis = Dup
        def _Push(self, newState):
            """Ingresar elemento a la cola, y ordernalo. Dados los parametros Ord(Ordenada) y
            Dup(Duplicados), ordena y evita duplicados"""
            if self._duplis or self._Empty():
                self._queue.append(newState)
            elif not self._Find(newState):
                self._queue.append(newState)
            if self._orden:
                for x in range(len(self._queue)-1,0,-1):
                    if self._queue[x] <= self._queue[x-1]:
                        self._queue[x], self._queue[x-1] = self._queue[x-1],self._queue[x]
                    else:
                        break
        def _Empty(self):
            """Determinar sí cola esta vacía"""
            return self._queue == []
        def _Pop(self):
            """Retirar elemento de la cola"""
            if not self._Empty():
                return self._queue.pop(0)
            else:
                return None
        def _Queue(self):
            """Retorna la cola"""
            return self._queue
filename = "LongText.txt"
file = open(filename, encoding="utf8")

def countletters(file):
    results = {}
    total = 0
    for line in file:
        for char in line:
            if char in results:
                if char is "\n":
                    results["Salto"] += 1
                else:
                    results[char] += 1
            else:
                if char is "\n":
                    results["Salto"] = 1
                else:
                    results[char] = 1
            total += 1
    for l,v in results.items():
        results[l] = v/total
    return (results,total)
Frecuencias, total = countletters(file)
H = HuffmanTree(Frecuencias)
Codigos = H.HuffmanCodes(True)
print("Longitud del mensaje:", total)
alpha = len(Frecuencias)
print("Longitud de alfabeto:", alpha)
print("Histograma y codificación:")
for k,v in Frecuencias.items():
    print(k,":",v,":",Codigos[k])
Decodigos = H.HuffmanCodes(False)
Frecs = [y for _,y in Frecuencias.items()]
Codes = [x for x,_ in Decodigos.items()]
Codes.reverse()
NumBits = sum([f*len(c) for f,c in zip(Frecs, Codes)])
Entropy = sum([x*log(1/x,2) for x in Frecs])
R = Entropy
print("Entropia:", R, "bits/letter")
r = Entropy/alpha
print("Rango Absoluto:", r, "bits/letter")
print("Redundancia:", R - r)
print("Promedio de bits(Huffman Codes):", NumBits)
InfoQuant = {}
for l,v in Frecuencias.items():
    InfoQuant[l] = log(1/v,2)
print("Información por caracter:")
for k,v in InfoQuant.items():
    print(k,"",v)
print("Entropía:", Entropy, "AvBits:", NumBits, "Entropía + 1:", Entropy + 1)
