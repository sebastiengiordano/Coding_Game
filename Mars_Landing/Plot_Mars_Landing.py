import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mcolors


class Plot_Mars_Landing:

    def __init__(self, land: list=None) -> None:
        self._land = land
        
        self._already_init = False
        
        self._lines = []
        self._colors = []
        self.nb_displayed_curves = 5
        self._width = 7000
        self._hight = 5000
        
        self._fig, self._ax = plt.subplots()
        self._ax.title.set_text('Plot land')
        self.set_axe()
        if self._land is not None:
            self._init_land()

    def _init_land(self):
        self._clean_land()
        if len(self._ax.lines):
            self._ax.lines[0].remove()

        if not self._already_init:
            plt.ion()
            plt.show()
            self._already_init = True

        x0, y0 = zip(*self._land)
        self._ax.plot(x0, y0, color='k')
        plt.draw()
        plt.pause(1)

    def _clean_land(self):
        while len(self._lines) > 0:
            self._lines[0].remove()
            self._lines.pop(0)

    def _get_color(self):
        if len(self._colors) == 0:
            self._colors = list(mcolors.TABLEAU_COLORS.values())
        color = self._colors.pop()
        return color

    def _update(self, num, x, y, line):
        line.set_data(x[:num], y[:num])
        return line

    def set_land(self, land: list=None):
        if land is not None:
            self._land = land
            self._init_land()

    def set_axe(self, width=None, hight=None):
        if width is not None:
            self._width = width
        if hight is not None:
            self._hight = hight

        self._ax.set_xlim([0, self._width]) 
        self._ax.set_ylim([0, self._hight])

    def animate(self, population:list):
        self._clean_land()

        for individu in population:
            x, y = zip(*individu)
            color = self._get_color()
            line, = self._ax.plot([], [], color=color)
            self._lines.append(line)
            ani = animation.FuncAnimation(self._fig, func=self._update, frames=len(x)+1, fargs=[x, y, line],
                                        blit = False, interval = min(len(x)*10, 200), repeat = False)
            plt.draw()
            plt.pause(.5)

            if len(self._lines) > self.nb_displayed_curves:
                self._lines[0].remove()
                self._lines.pop(0)
        plt.pause(0.5)


if __name__ == '__main__':
    land = [(0, 1000), (300, 1500), (350, 1400), (500, 2000), (800, 1800), (1000, 2500), (1200, 2100), (1500, 2400), (2000, 1000), (2200, 500), (2500, 100), (2900, 800), (3000, 500), (3200, 1000), (3500, 2000), (3800, 800), (4000, 200), (5000, 200), (5500, 1500), (6999, 2800)]
    all_path = [
        [(0, 1000), (800, 2800), (1500, 2500), (2500, 1000), (3800, 1100), (6999, 3000)],
        [(0, 2000), (1000, 2500), (2000, 2000), (3000, 3500), (4000, 2000), (6999, 5000)],
        [(0, 3000), (800, 3800), (1500, 3500), (2500, 2000), (3800, 2100), (6999, 3500)],
        [(0, 4000), (1000, 3500), (2000, 3000), (3000, 4500), (4000, 3000), (6999, 4500)],
    ]
    Lcarte =([0, 450], [300, 750], [1000, 450], [1500, 650], [1800, 850], [2000, 1950], [2200, 1850], [2400, 2000], [3100, 1800], [3150, 1550], [2500, 1600], [2200, 1550], [2100, 750], [2200, 150], [3200, 150], [3500, 450], [4000, 950], [4500, 1450], [5000, 1550], [5500, 1500], [6000, 950], [6999, 1750])


    # Init Land
    plot_mars_landing = Plot_Mars_Landing(land)
    plot_mars_landing.nb_displayed_curves = 2
    # Animate some curves
    plot_mars_landing.animate(all_path)
    # Change of map
    plot_mars_landing.set_land(Lcarte)
    # Animate some curves
    plot_mars_landing.animate(all_path)
    plot_mars_landing.animate(all_path)
