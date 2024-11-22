import turtle

# Atur layar
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Bintang dengan Python")

# Atur turtle
star = turtle.Turtle()
star.shape("turtle")
star.color("yellow")
star.speed(10)

# Fungsi menggambar bintang
def draw_star(size):
    for _ in range(5):
        star.forward(size)
        star.right(144)

# Gambar bintang dengan ukuran tertentu
star.penup()
star.goto(0, 0)
star.pendown()
draw_star(200)

# Selesai
star.hideturtle()
screen.mainloop()