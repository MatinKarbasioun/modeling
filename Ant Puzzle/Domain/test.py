import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        self.x += dx
        self.y += dy

    def get_position(self):
        return (self.x, self.y)


class AntModel:
    def __init__(self, num_ants, x_min, x_max, y_min, y_max):
        self.ants = [Ant(random.randint(x_min, x_max), random.randint(y_min, y_max)) for _ in range(num_ants)]
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def update(self):
        for ant in self.ants:
            ant.move()

    def get_positions(self):
        return [ant.get_position() for ant in self.ants]


# create an instance of the AntModel with 50 ants
model = AntModel(50, 0, 100, 0, 100)

# create the figure and axes
fig, ax = plt.subplots()


# define the initial plot
def init():
    ax.set_xlim(model.x_min, model.x_max)
    ax.set_ylim(model.y_min, model.y_max)
    return []


# define the update function
def update(frame):
    # update the model
    model.update()

    # clear the axes
    ax.clear()

    # get the ant positions and plot them
    positions = model.get_positions()
    x_positions, y_positions = zip(*positions)
    ax.scatter(x_positions, y_positions, color='red')

    # add labels and title
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.set_title('Ant Movement Model')

    return []


# create the animation
ani = animation.FuncAnimation(fig, update, init_func=init, frames=100, interval=50, blit=True)

# show the animation
plt.show()