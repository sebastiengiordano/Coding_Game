
from random import random, randint

from Plot_Mars_Landing import plot_map

K_NB_GENE = 1000
K_NB_CHROMOSOME = 5
K_NB_INDIVIDU = 50
K_NB_SURVIVANTS = int(K_NB_INDIVIDU * 2/3)
K_PROBA_MUTATION = 10   # %
B_TEST = True


class Gene():
    def __init__(self) -> None:
        self.rotation = 45 - randint(0, 90)
        self.power = randint(0, 4)
        self.x = -1
        self.y = -1

    def mute(self):
        if randint(1, 2) > 1:
            self.power = min(4, max(0,
                                self.power + (1 - ( 2 * randint(0,1) ) )
                                ))
        else:
            self.rotation = min( 90, max( -90,
                                self.rotation + (1 - ( 2 * randint(0,1) ) ) 
                                ))


class Chromosome():
    def __init__(self) -> None:
        self.c = [Gene() for _ in range(K_NB_GENE)]

    def mute(self):
        if randint(0, 100) <= K_PROBA_MUTATION:
            self.c[randint( 0, ( len(self.c) - 1 ) )].mute()
                

class Individu():
    def __init__(self) -> None:
        self.c = [Chromosome() for _ in range(K_NB_CHROMOSOME)]


class Population():
    def __init__(self) -> None:
        self.p = [Individu() for _ in range(K_NB_INDIVIDU)]


class My_Map():
    def __init__(self) -> None:
        if not B_TEST:
            self.surface_n = int(input())  # the number of points used to draw the surface of Mars.
            self.land = []
            for i in range(self.surface_n):
                # land_x: X coordinate of a surface point. (0 to 6999)
                # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
                land_x, land_y = [int(j) for j in input().split()]
                self.land.append((land_x, land_y))
            x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
        else:
            # Gorge profonde
            self.surface_n = 20
            self.land = [(0, 1000), (300, 1500), (350, 1400), (500, 2000), (800, 1800), (1000, 2500), (1200, 2100), (1500, 2400), (2000, 1000), (2200, 500), (2500, 100), (2900, 800), (3000, 500), (3200, 1000), (3500, 2000), (3800, 800), (4000, 200), (5000, 200), (5500, 1500), (6999, 2800)]
            
            x, y, h_speed, v_speed, fuel, rotate, power = 0, 0, 0, 0, 0, 0, 0

        self.land_x_left  = 0
        self.land_x_right = 0
        for i in range(len(self.land) - 1):
            if (    ( self.land[i][1] == self.land[i + 1][1] )
                    and
                    ( self.land[i + 1][0] - self.land[i][0] >= 1000 ) ):
                self.land_x_left = self.land[i][0]
                self.land_x_right = self.land[i +1][0]
                delta = int(abs(self.land_x_right - self.land_x_left) * 20 / 100)
                self.land_x_left = self.land_x_left + delta
                self.land_x_right = self.land_x_right - delta
                self.land_y = self.land[i][1]
                break


if __name__ == '__main__':
    my_map = My_Map()
    plot_map(my_map.land)