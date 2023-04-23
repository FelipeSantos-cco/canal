import turtle
import random

# Definindo as constantes
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_SIZE = 10
NUM_CELLS = 10

# Configurando a tela
screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Multiplicação Celular")

# Criando uma lista de células
cells = []
for i in range(NUM_CELLS):
    cell = turtle.Turtle()
    cell.shape('circle')
    cell.penup()
    cell.speed(0)
    cell.color(random.choice(['red', 'blue', 'green']))
    cell.goto(random.randint(-SCREEN_WIDTH//2, SCREEN_WIDTH//2),
                random.randint(-SCREEN_HEIGHT//2, SCREEN_HEIGHT//2))
    cell.dx = random.choice([-CELL_SIZE, CELL_SIZE])
    cell.dy = random.choice([-CELL_SIZE, CELL_SIZE])
    cells.append(cell)

# Configurando a animação
turtle.tracer(2)
while True:
    for cell in cells:
        cell.setx(cell.xcor() + cell.dx)
        cell.sety(cell.ycor() + cell.dy)
        
        # Checando as bordas da tela
        if cell.xcor() > SCREEN_WIDTH/2 - CELL_SIZE or cell.xcor() < -SCREEN_WIDTH/2 + CELL_SIZE:
            cell.dx *= -1
        if cell.ycor() > SCREEN_HEIGHT/2 - CELL_SIZE or cell.ycor() < -SCREEN_HEIGHT/2 + CELL_SIZE:
            cell.dy *= -1

    # Checando colisões entre células
    for i in range(len(cells)):
        for j in range(i+1, len(cells)):
            if cells[i].distance(cells[j]) < CELL_SIZE:
                cells[i].color(random.choice(['red', 'blue', 'green']))
                cells[j].color(random.choice(['red', 'blue', 'green']))
                new_cell = turtle.Turtle()
                new_cell.shape('circle')
                new_cell.penup()
                new_cell.speed(0)
                new_cell.color(random.choice(['red', 'blue', 'green']))
                new_cell.goto(random.randint(-SCREEN_WIDTH//2, SCREEN_WIDTH//2),
                                random.randint(-SCREEN_HEIGHT//2, SCREEN_HEIGHT//2))
                new_cell.dx = random.choice([-CELL_SIZE, CELL_SIZE])
                new_cell.dy = random.choice([-CELL_SIZE, CELL_SIZE])
                cells.append(new_cell)

    turtle.update()