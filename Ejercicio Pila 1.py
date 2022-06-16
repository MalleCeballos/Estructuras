class Pila:
     def _init_(self):
         self.items = []

     def estaVacia(self):
         return self.items == []

     def incluir(self, valor):
         self.items.append(valor)

     def extraer(self):
         return self.items.pop()

     def inspeccionar(self):
         return self.items[len(self.items)-1]

     def tamano(self):
         return len(self.items)
        
     def llenarlista(self):
         n=int(input('Ingrese el numero de datos que va a ingresar:'))
         while(n>0):
             self.incluir(input('Escriba el dato a ingresar en la pila:'))
             n-=1
             
     def mostrarlista(self):
         n=self.tamano()
         while(n>0):
             print(self.extraer())
             n-=1
    #modulos 4 punto       
     def pasarapila(self,lista1):
         t=int(len(lista1))
         for i in range(0, t):
             s1.incluir(lista1[i])
             
     def ordenarpila(self):
         n=self.tamano()
         for i in range(0,n):
             if(self.items[i] < self.items[i+1]):
                 temp=self.items[i+1]
                 self.items[i+1]=self.items[i]
                 self.items[i]=temp
        
             
p=Pila()
p.llenarlista()
p.mostrarlista()
print('\n')
#Dadas dos listas ordenadas, mezclarlas en una que también quede ordenada.
lista1=("18","15","11","8","4","1")
lista2=("20","19","5","4")
lista3=lista1+lista2
s1=Pila()
t=int(len(lista3))
s1.pasarapila(lista3)
s1.ordenarpila()
s1.mostrarlista()
