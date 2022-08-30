class TV:
    numTV=0
    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.control = None
        self.precio=500
        self.volumen=1
        self.canal=1
        TV.numTV += 1 
    def getMarca(self):
        return self.marca
    def setMarca(self, marca):
        self.marca=marca
    def getControl(self):
        return self.control
    def setControl(self, control):
        self.control=control
    def getPrecio(self):
        return self.precio
    def setPrecio(self, precio):
        self.precio=precio
    def getVolumen(self):
        return self.volumen
    def setVolumen(self, volumen):
        if ((self.estado == True) and (volumen <8 and volumen >0)):
            self.volumen=volumen
    def getCanal(self):
        return self.canal
    def setCanal(self, canal):
        self.canal=canal
    @classmethod
    def setNumTV(self, numTV):
        self.numTV=numTV
    @classmethod
    def getNumTV(self):
        return self.numTV
    def turnOn(self):
        if estado ==False:
            estado = True
    def turnOff(self):
        if estado ==True:
            estado = False
    def canalUp(self, canal):
        if (canal > 0 and canal <= 120)and(self.estado==True):
            canal+=1
    def canalDown(self, canal):
        if (canal > 1 and canal < 121)and(self.estado==True):
            canal-=1
    def volumenUp(self, volumen):
        if (volumen >=0 and volumen <=7)and(self.estado==True):
            volumen+=1
    def volumenDown(self, volumen):
        if (volumen < 8 and volumen >=0)and(self.estado == True):
            volumen-=1
    def getEstado(self):
        return self.estado