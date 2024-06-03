
from random import randint
from math import cos, sin, radians

from Plot_Mars_Landing import Plot_Mars_Landing


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
        # Contraintes
        # 2 ≤ surfaceN < 30
        # 0 ≤ X < 7000
        # 0 ≤ Y < 3000

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


class Movement():

    def __init__(   self,
                    x = 0,
                    y = 0,
                    h_speed = 0,
                    v_speed = 0,
                    fuel = 0,
                    rotate = 0,
                    power = 0) -> None:
        self.x       = x
        self.y       = y
        self.h_speed = h_speed
        self.v_speed = v_speed
        self.fuel    = fuel
        self.rotate  = rotate
        self.power   = power

    def command(self, rotate: int, power: int):
        self._set_rotate(rotate)
        self._set_power(power)
        self._set_speed()
        self._set_position()

    def _set_rotate(self, rotate: int):
        # rotate est l’angle de rotation souhaité pour Mars Lander.
        # à noter que la rotation effective d’un tour à l’autre est limitée à +/- 15° par rapport à l’angle du tour précedent.
        # -90 ≤ rotate ≤ 90
        rotate_min = max(self.rotate - 15, -90)
        rotate_max = min(self.rotate + 15, 90)
        self.rotate = max(min(rotate, rotate_max), rotate_min)

    def _set_power(self, power: int):
        # power est la puissance des fusées. 0 = éteintes. 4 = puissance maximum. La puissance effective d'un tour à l'autre est limitée à +/- 1.
        # 0 ≤ power ≤ 4
        power_min = max(self.power - 1, 0)
        power_max = min(self.power + 1, 4)
        self.power = max(min(power, power_max), power_min)

    def _set_speed(self):
        # -500 < hSpeed, vSpeed < 500
        h_acceleration = round(cos(radians(self.rotate)) * self.power)
        v_acceleration = round(-sin(radians(self.rotate)) * self.power)
        # Since one turn correspond to 1s, the new speed is obtain by addind acceleration
        self.h_speed = int( min( max( self.h_speed + h_acceleration,         -500 ), 500 ) )
        self.v_speed = int( min( max( self.v_speed + v_acceleration - 3.711, -500 ), 500 ) )

    def _set_position(self):
        # Since one turn correspond to 1s, the new position is obtain by addind speed
        self.x = self.x + self.h_speed
        self.y = self.y + self.v_speed


if __name__ == '__main__':
    my_map = My_Map()
    # Plot_Mars_Landing(my_map.land)

    B_TEST = False
    # 6 (surfaceN) Sol constitué de 6 points
    my_map.surface_n = 6
    #    0 1500 (landX landY)
    # 1000 2000 (landX landY)
    # 2000  500 (landX landY) Début zone de plat
    # 3500  500 (landX landY) Fin zone de plat
    # 5000 1500 (landX landY)
    # 6999 1000 (landX landY)
    my_map.land = [
        (0, 1500),
        (1000, 2000),
        (2000, 500),
        (3500, 500),
        (5000, 1500),
        (6999, 1000)]
    # plot_mars_landing = Plot_Mars_Landing(my_map.land)

    # Entrée pour le tour 1
    # 5000 2500 -50 0 1000 90 0 (X Y hSpeed vSpeed fuel rotate power)
    mov = Movement(5000, 2500, -50, 0, 1000, 90, 0)
    # Sortie pour le tour 1
    # -45 4 (rotate power)
    mov.command(-45, 4)
    print(f"Next position expected x = 4950, y = 2498 => "
          f"\n\t Test x {'OK' if mov.x == 4950 else f'FAIL x = {mov.x}'}"
          f"\n\t Test y {'OK' if mov.y == 2498 else f'FAIL y = {mov.y}'}")
    # Nouvel angle demandé vers la droite, poussée des fusées au max
    # Entrée pour le tour 2
    # 4950 2498 -51 -3 999 75 1 (X Y hSpeed vSpeed fuel rotate power)
    # L'angle de rotation n'a évolué que de 15° et la poussée de 1
    # Sortie pour le tour 2
    # -45 4 (rotate power)
    mov.command(-45, 4)
    print(f"Next position expected x = 4898, y = 2493 => "
          f"\n\t Test x {'OK' if mov.x == 4898 else f'FAIL x = {mov.x}'}"
          f"\n\t Test y {'OK' if mov.y == 2493 else f'FAIL y = {mov.y}'}")
    # Même demande que précedemment
    # Entrée pour le tour 3
    # 4898 2493 -53 -6 997 60 2 (X Y hSpeed vSpeed fuel rotate power)
    # Sortie pour le tour 3
    # -45 4 (rotate power)
    # Même demande que précedemment