class Nodo :
    def __init__(self,valor):
        self.valor = valor 
        self.hijoIzquierda = None
        self.hijoDerecho = None

    def getHijoIzquierdo (self) :
        return self.hijoIzquierda
    
    def getHijoDerecho (self) :
        return self.getHijoDerecho
    
    def setHijoIzquierdo(self, nodo ):
        self.hijoIzquierda = nodo

    def setHijoDerecho (self, nodo)  :
        self.hijoDerecho = nodo

    def getValor (valor) :
        return self.valor
    def setValor (self, valor) :
        self.valor = valor 
           