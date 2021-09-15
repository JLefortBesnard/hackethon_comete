import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


# classe qui represente le jeu
class Radar:
    def __init__(self, screen_x, screen_y):
        super().__init__()
        fig, ax = plt.subplots()
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.ax = ax

    def create_rectangle(self,root_x, root_y, size_x, size_y, color):
        root_x = root_x / 10
        root_y = root_y / 10
        size_x = size_x / 10
        size_y = size_y / 10
        self.ax.add_patch(Rectangle((root_x, root_y), size_x, size_y, color=color))

    def define_title(self, title):
        plt.title('Radar {}'.format(title))
    def show(self):
        plt.xlim(0, self.screen_x/10)
        plt.ylim(self.screen_y/10)
        plt.show()




