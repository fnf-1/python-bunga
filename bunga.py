# Import library turtle
import turtle

# Inisialisasi objek turtle
t = turtle.Turtle()

# Atur kecepatan turtle
t.speed(10)

# Buat bentuk bunga dengan perulangan
for i in range(36):
  # Atur warna petal sesuai dengan indeks perulangan
  if i % 6 == 0:
    t.color('red')
  elif i % 6 == 1:
    t.color('orange')
  elif i % 6 == 2:
    t.color('yellow')
  elif i % 6 == 3:
    t.color('green')
  elif i % 6 == 4:
    t.color('blue')
  elif i % 6 == 5:
    t.color('purple')
    
  # Gambar petal dengan ujung runcing
  t.begin_fill()
  t.circle(100, 180)
  t.left(90)
  t.forward(100)
  t.left(90)
  t.circle(100, 180)
  t.left(90)
  t.forward(100)
  t.end_fill()
  t.left(170)


# Jangan lupa untuk mengakhiri program dengan menutup jendela turtle
turtle.done()