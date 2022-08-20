class caja:
    def __init__(self,largo,ancho,costo=10):
        self.largo=largo
        self.ancho=ancho
        self.costo=costo
    
    def perimetro(self):
        return 2*(self.largo + self.ancho)

    def area(self):
        return self.largo* self.ancho

    def precio(self):
        area=self.area()
        return area*self.costo
r=caja(160,120,2000)
print("el area de la caja es :",(r.area()))
print("el material de la caja cuesta:",(r.precio()))
