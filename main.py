class Nodo: 
    def __init__(self, datos, numero):  
        self.izquierdo = None    
        self.derecho = None 
        self.datos = datos  
        self.numero = numero  

    def insertar(self, datos, numero): 
        if self.datos: 
            if datos < self.datos: 
                if self.izquierdo is None: 
                    self.izquierdo = Nodo(datos, numero) 
                else:
                    self.izquierdo.insertar(datos, numero) 
            elif datos > self.datos:
                if self.derecho is None: 
                    self.derecho = Nodo(datos, numero) 
                else:
                    self.derecho.insertar(datos, numero) 
        else:
            self.datos = datos 
            self.numero = numero 

    def imprimirArbol(self): 
        if self.izquierdo: 
            self.izquierdo.imprimirArbol() 
        if self.datos != "":
            print(self.datos),
            print(" {~} "+str(self.numero)),
        if self.derecho:
            self.derecho.imprimirArbol()  

index = open ("Taller_2/index.txt") 
contenido = index.readlines()  
raiz = Nodo("", 0) 
subTema = [] 
i = 0 
txt = "" 


while (i < len(contenido)): 
    index= contenido[i].strip()
    numero = [] 
    text = "" 
    numeroTemporal = [] 
    textsSub = [] 
    textTemporal = "" 

    for j in index: 
        if (index[0] == "m"): 
            if (j.isdigit() == True): 
                numero.append(j) 
            else: 
                text += j 
                txt = text 
        elif (index[0] == "s"): 

            if (j.isdigit() == True): 
                numeroTemporal.append(j) 
            else: 
                textTemporal += j 

    numeroTemporal.sort() 

    textsSub = [txt, textTemporal+str(numeroTemporal)] 
    subTema.append(textsSub) 
    numero.sort() 
    raiz.insertar(text, numero) 
    i += 1 

print("\n"  + "Lista de términos principales" + "\n")
raiz.imprimirArbol()  
subTema.sort()  

print("\n" + "Lista de subterminos con sus páginas" + "\n") 
c = 0 
temptext = [] 

while c < len(subTema): 
    if (subTema[c][1] != '[]'): 
        print("[*~Tema:] "+subTema[c][0]+ "\n") 
        print("\t * Subtemas con sus páginas ordenadas :" + subTema [c][1] + "\n") 
    c += 1 

