# import matplotlib.pyplot as plt
# # generate axes object
# ax = plt.axes()

# # set limits
# plt.xlim(0,10) 
# plt.ylim(0,10)

# for i in range(10):        
#     # add something to axes
#     ax.scatter([i], [i])
#     ax.plot([i], [i+1], 'rx')

#     # draw the plot
#     plt.draw()
#     plt.pause(0.5) #is necessary for the plot to update for some reason

#     # start removing points if you don't want all shown
#     if len(ax.lines) > 4:
#         ax.lines[0].remove()
#         ax.collections[0].remove()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.rcParams['lines.linewidth'] = 5

x = np.linspace(0, 7.5, 100)
y1 = np.sin(x)
y2 = np.sin(x+0.5)
y3 = [0] * len(x)
ys = [y1, y2, y3]

fig, ax = plt.subplots()

line1, = ax.plot(x, y1, label='zorder=2', zorder=2, color='orange') #bottom
line2, = ax.plot(x, y2, label='zorder=4', zorder=4, color='blue')
line3, = ax.plot(x, y3, label='zorder=3', zorder=3, color='lightgrey', linewidth=8)
lines = [line1, line2, line3]

def update(num, x, ys, lines):
    for i in range(len(ys)):
        lines[i].set_data(x[:num], ys[i][:num])

    if num > len(x)/2:
        line1.set_linewidth(10)
        line1.set_zorder(5)       #upper
        line2.set_zorder(1)       #bottom

    print(line1.get_zorder())

    return lines


ani = animation.FuncAnimation(fig, func=update, frames=len(x), fargs=[x, ys, lines],
                            blit = True, interval = 50, save_count = 50, repeat = False)

plt.show()
