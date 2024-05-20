import matplotlib.pyplot as plt
import matplotlib.animation as animation

def plot_map(My_Map: list):
    # point_list = []
    # for x, y in My_Map:
    #     point_list.append(x)
    #     point_list.append(y)

    x, y = zip(*My_Map)
    # plt.plot(*point_list, marker = '.', linestyle = 'dotted', color='brown')
    # plt.plot(*point_list, marker = '.', linestyle = 'dashdot', color='brown')
    plt.plot(x, y, marker = '.', linestyle = 'solid', color='brown')
    plt.ion()
    plt.show()

def plot_remove_plot():
    from time import sleep
    line1 = [2, 4, 8]
    line2 = [3, 6, 12]

    plt.plot(line1)
    plt.title("Plot one line")
    plt.ion()
    plt.show()
    plt.pause(1)
    # plt.pause(0.001)
    # sleep(2)


    line_2 = plt.plot(line2, linestyle='dashed')
    plt.margins(0.2)
    plt.title("With extra lines")
    plt.draw()
    plt.pause(1)
    # plt.pause(0.001)
    # sleep(2)

    # plt.plot(line1)
    l = line_2.pop(0)
    l.remove()
    plt.title("Removed extra lines")
    plt.draw()
    plt.pause(1)
    # plt.pause(0.001)
    # sleep(2)


    line_2 = plt.plot(line2, linestyle='dashed')
    plt.title("Another, add extra lines")

    plt.draw()
    plt.pause(1)
    # plt.pause(0.001)
    # sleep(2)
    input("Press [enter] to continue.")

def add_plot():
    frame_size = 2
    land = [(0, 1000), (300, 1500), (350, 1400), (500, 2000), (800, 1800), (1000, 2500), (1200, 2100), (1500, 2400), (2000, 1000), (2200, 500), (2500, 100), (2900, 800), (3000, 500), (3200, 1000), (3500, 2000), (3800, 800), (4000, 200), (5000, 200), (5500, 1500), (6999, 2800)]
    all_path = [
        [(0, 1000), (800, 2800), (1500, 2500), (2500, 1000), (3800, 1100), (6999, 3000)],
        [(0, 2000), (1000, 2500), (2000, 2000), (3000, 3500), (4000, 2000), (6999, 5000)],
        [(0, 3000), (800, 3800), (1500, 3500), (2500, 2000), (3800, 2100), (6999, 3500)],
        [(0, 4000), (1000, 3500), (2000, 3000), (3000, 4500), (4000, 3000), (6999, 4500)],
    ]
    x0, y0 = zip(*land)
    plt.title("Plot Land")

    fig, ax = plt.subplots()
    line, = ax.plot(x0, y0, color='k')
    plt.ion()
    plt.show()
    plt.pause(1)

    for path in all_path:
        x, y = zip(*path)
        ax.plot(x[:frame_size], y[:frame_size])
        x, y = x[frame_size:], y[frame_size:]
        plt.draw()
        plt.pause(0.1)
        while len(x) >= frame_size:
            ax.lines[0].data

        if len(ax.lines) > 2:
            ax.lines[0].remove()
        if len(ax.collections) > 2:
            ax.collections[0].remove()

    while len(ax.lines) > 0:
        ax.lines[0].remove()
        if len(ax.collections) > 0:
            ax.collections[0].remove()

def ani_plot():
    land = [(0, 1000), (300, 1500), (350, 1400), (500, 2000), (800, 1800), (1000, 2500), (1200, 2100), (1500, 2400), (2000, 1000), (2200, 500), (2500, 100), (2900, 800), (3000, 500), (3200, 1000), (3500, 2000), (3800, 800), (4000, 200), (5000, 200), (5500, 1500), (6999, 2800)]
    all_path = [
        [(0, 1000), (800, 2800), (1500, 2500), (2500, 1000), (3800, 1100), (6999, 3000)],
        [(0, 2000), (1000, 2500), (2000, 2000), (3000, 3500), (4000, 2000), (6999, 5000)]
    ]
    x0, y0 = zip(*land)
    plt.title("Plot Land")

    fig, ax = plt.subplots()
    line, = ax.plot(x0, y0, color='k')
    plt.ion()
    plt.show()
    plt.pause(1)

    def update(num, x, y, line):
        line.set_data(x[:num], y[:num])
        line.axes.axis([0, 7000, 0, 3000])
        return line,

    for path in all_path:
        x, y = zip(*path)
        # line, = ax.plot(x, y, color='k')
        ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, line],
                                interval=25, blit=True, repeat=False)
        plt.draw()
        plt.pause(1)


if __name__ == '__main__':
    add_plot()
