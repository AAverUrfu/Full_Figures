class Figure():
  def __init__(self):
    print("Создание figure.")
  def show(self):
    print("I am figure!")
  def perimeter(self):
    print("вычисление периметра.")

class Triangle(Figure):
  def __init__(self,a,b,c):
    super().__init__()
    self.a = a
    self.b = b
    self.c = c
    print("Создание треугольника произошло успешно")
  def show(self):
    super().show()
    print("triangle (%.1f,%.1f,%.1f)" %(self.a,self.b,self.c) )
  def perimeter(self):
    print("вычисление периметра треугольника.")
    return (self.a+self.b+self.c)
f = Figure()
f.show()
f.perimeter()
tr = Triangle(5,2,7)
tr.show()
print(tr.perimeter())
