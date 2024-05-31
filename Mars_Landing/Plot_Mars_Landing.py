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
        frame = max(len(x)//10, 1)
        line.set_data(x[:num*frame], y[:num*frame])
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
            ani = animation.FuncAnimation(
                    self._fig,
                    func=self._update,
                    fargs=[x, y, line],
                    interval = 10,
                    blit = False, repeat = False )
            plt.draw()
            plt.pause(.5)

            if len(self._lines) > self.nb_displayed_curves:
                self._lines[0].remove()
                self._lines.pop(0)
        plt.pause(0.5)


if __name__ == '__main__':
    from _test.FuncAnim_data import land, all_path, Lcarte, Large_Curve, LCurve

    # Init Land
    plot_mars_landing = Plot_Mars_Landing(land)
    plot_mars_landing.nb_displayed_curves = 3
    # # Animate some curves
    plot_mars_landing.animate(all_path)
    # # Change of map
    plot_mars_landing.set_land(Lcarte)
    # # Animate some curves
    plot_mars_landing.animate(all_path)
    plot_mars_landing.animate(all_path)
    # Change of map
    plot_mars_landing.set_land(land)
    # Animate large curve
    plot_mars_landing.animate([Large_Curve, LCurve])
    plt.pause(10)
