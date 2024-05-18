import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

class Bat_Move:

    def __init__(self, width:int, height:int, x0:int, y0:int):
        self.debug = False
        self.must_display = False
        self.brutal_force = True

        self.cells = set()
        self.width = width
        self.height = height

        self.x = x0
        self.y = y0
        self.x_prev = x0
        self.y_prev = y0

        for x in range(0, width):
            for y in range(0, height):
                self.cells.add((x, y))
        self.cells.remove((x0, y0))

        if self.brutal_force:
            self.next_jump = None
            self.distance_list = self.set_distance_list ( width, height )
            self.seek_best_choice()
            self.set_first_move()
            self.play_first_move()
        else:
            self.init_square()

        if self.must_display == True:
            self.display()
        self.run()

    def run(self):
        if self.brutal_force:
            while True:
                bomb_dir = input()
                if self.debug:
                    print(f'------> bomb_dir = {bomb_dir}', file=sys.stderr, flush=True)
                self.evaluation(bomb_dir)
                if self.must_display == True:
                    self.display()
                self.seek_best_choice()
                self.bat_move()
        else:
            while True:
                bomb_dir = input()
                self.evaluation(bomb_dir)
                self.jump()
                if self.must_display == True:
                    self.display()

    def evaluation(self, bomb_dir:str):
        if bomb_dir in ('COLDER', 'WARMER', 'SAME'):
            self.clean_cells_list( bomb_dir )

    def clean_cells_list(self, bomb_dir):
        for x, y in self.cells.copy():
            if bomb_dir != self.is_closer(x, y):
                self.cells.remove((x,y))

    def is_closer(self, x, y):
        # old_dist = (self.x_prev - x)**2 +  (self.y_prev - y)**2
        # new_dist = (self.x - x)**2 +  (self.y - y)**2

        old_dist = self.distance_list[abs(self.x_prev - x)][abs(self.y_prev - y)]
        new_dist = self.distance_list[abs(self.x - x)][abs(self.y - y)]

        if old_dist > new_dist:
            return 'WARMER'
        elif old_dist < new_dist:
            return 'COLDER'
        else:
            return 'SAME'

    def dist_compute(self, x, y):
        return (x)**2 +  (y)**2

    def jump(self):
        self.x_prev, self.y_prev = self.x, self.y
        # self.x, self.y = self.cells.pop()
        self.seek_next_cell()

        print( f'{self.x} {self.y}' )

    def bat_move(self):
        print(f'{self.x} {self.y}')

    def seek_next_cell(self):
        x_sum, y_sum = 0, 0
        for x, y in self.cells:
            x_sum += x
            y_sum += y
        x = math.floor( x_sum / len(self.cells) )
        y = math.floor( y_sum / len(self.cells) )
        state = 'U'
        move_counter_x = 1
        move_counter_y = 1
        move_counter_step = 1

        while (x, y) not in self.cells:
            if state == 'U':
                x -= 1
                x = max(x, 0)
                move_counter_x -= 1
            elif state == 'R':
                y += 1
                y = min( y, self.height - 1 )
                move_counter_y -= 1
            elif state == 'D':
                x += 1
                x = min( x, self.width - 1 )
                move_counter_x -= 1
            else:
                y -= 1
                y = max(y, 0)
                move_counter_y -= 1

            if move_counter_x <= 0:
                state = self.seek_next_cell_state_update(state)
                move_counter_step += 1
                move_counter_x = move_counter_step

            if move_counter_y <= 0:
                state = self.seek_next_cell_state_update(state)
                move_counter_y = move_counter_step

            print(x, y, file=sys.stderr, flush=True)

        self.x = x
        self.y = y

        self.cells.remove((x, y))

    def seek_next_cell_state_update(self, state):
        if state == 'U':
            state = 'R'
        elif state == 'R':
            state = 'D'
        elif state == 'D':
            state = 'L'
        else:
            state = 'U'
        return state

    def seek_best_choice(self):
        cells_len = len(self.cells)
        removed_cells_counter = 0
        self.next_jump = None

        if self.debug and cells_len < 5:
                print(f'x = {self.x}\t y = {self.y}', file=sys.stderr, flush=True)

        for x_in_test, y_in_test in self.cells:
            counter = 0
            remaining_cells = cells_len
            if self.debug and cells_len < 5:
                    print(f'x_in_test = {x_in_test}\t y_in_test = {y_in_test}', file=sys.stderr, flush=True)
            for x, y in self.cells:
                new_dist = self.distance_list[abs(x_in_test - x)][abs(y_in_test - y)]
                old_dist = self.distance_list[abs(self.x - x)][abs(self.y - y)]
                counter += new_dist > old_dist
                remaining_cells -= 1
                if self.debug and cells_len < 5:
                    print('\t', x, y, file=sys.stderr, flush=True)
                    print(f'\t old_dist         = {old_dist}',          file=sys.stderr, flush=True)
                    print(f'\t new_dist         = {new_dist}',          file=sys.stderr, flush=True)
                    print(f'\t counter          = {counter}',           file=sys.stderr, flush=True)
                    print(f'\t remaining_cells  = {remaining_cells}',   file=sys.stderr, flush=True)
                    print(f'\t removed_cells_counter = {removed_cells_counter}\n', file=sys.stderr, flush=True)

                if counter + remaining_cells < removed_cells_counter:
                    break

            if counter > removed_cells_counter:
                removed_cells_counter = counter
                self.next_jump = (x, y)

        self.x_prev, self.y_prev = self.x, self.y
        if self.next_jump is not None:
            self.x, self.y = self.next_jump
            self.cells.remove((self.x, self.y))
        else:
            self.x, self.y = self.cells.pop()

    def display(self):
        map_to_display = ''
        for y in range(0, self.height):
            for x in range(0, self.width):
                if (x,y) in self.cells:
                    map_to_display += 'X'
                else:
                    map_to_display += ' '
            map_to_display += '|\n'
        print(map_to_display, file=sys.stderr, flush=True)

    def init_square(self):
        x_middle = math.floor( self.width  / 2 )
        y_middle = math.floor( self.height / 2 )

        self.square_top_left = Square(
                                    'top_left',
                                    0, x_middle - 1,
                                    0, y_middle - 1 )
        self.square_top_right = Square(
                                    'top_right',
                                    x_middle, self.width - 1,
                                    0, y_middle - 1 )
        self.square_bottom_left = Square(
                                    'bottom_left',
                                    0, x_middle - 1,
                                    y_middle, self.height - 1 )
        self.square_bottom_right = Square(
                                    'bottom_right',
                                    x_middle, self.width - 1,
                                    y_middle, self.height - 1 )
        self.squares = [
            self.square_top_left,
            self.square_top_right,
            self.square_bottom_left,
            self.square_bottom_right ]
        for square in self.squares:
            if square.is_in(self.x, self.y):
                square_name = square.name
                break

    def set_square(self):
        x_min = self.width
        x_max = 0
        y_min = self.height
        y_max = 0

        for x, y in self.cells:
            if x >= x_max:
                x = x_max
            elif x < x_min:
                x = x_min
            if y >= y_max:
                y = y_max
            elif y < y_min:
                y = y_min

        x_middle = math.floor( (x_max + x_min) / 2 )
        y_middle = math.floor( (y_max + y_min)  / 2 )

        self.square_top_left = Square(
                                    x_min, x_middle - 1,
                                    y_min, y_middle - 1 )
        self.square_top_right = Square(
                                    x_middle, x_max,
                                    y_min, y_middle - 1 )
        self.square_bottom_left = Square(
                                    x_min, x_middle - 1,
                                    y_middle, y_max )
        self.square_bottom_right = Square(
                                    x_middle, x_max,
                                    y_middle, y_max )

    def valid_cell_arround(self, x, y):
        def next_statee(state):
            if state == 'U':
                state = 'R'
            elif state == 'R':
                state = 'D'
            elif state == 'D':
                state = 'L'
            else:
                state = 'U'
            return state

        state = 'U'
        move_counter_x = 1
        move_counter_y = 1
        move_counter_step = 1
        while (x, y) not in self.cells:
            if state == 'U':
                x -= 1
                x = max(x, 0)
                move_counter_x -= 1
            elif state == 'R':
                y += 1
                y = min( y, self.height - 1 )
                move_counter_y -= 1
            elif state == 'D':
                x += 1
                x = min( x, self.width - 1 )
                move_counter_x -= 1
            else:
                y -= 1
                y = max(y, 0)
                move_counter_y -= 1

            if move_counter_x <= 0:
                state = next_statee(state)
                move_counter_step += 1
                move_counter_x = move_counter_step

            if move_counter_y <= 0:
                state = next_statee(state)
                move_counter_y = move_counter_step

            if self.debug:
                print(x, y, file=sys.stderr, flush=True)

        self.x = x
        self.y = y

        self.remove_cells(x, y)

    def get_next_cell(self):
        pass

    def set_distance_list (self, width, height):
        # base = []
        computed_dist = []
        # for x in range(0, max( width, height )):
        #     base.append(x**2)
        base = list((x**2 for x in range(0, max( width, height ))))
        if width > height:
            b = base[:height]
            for x in range(0, width):
                computed_dist.append(list(i+base[x] for i in b))
        else:
            for x in range(0, width):
                computed_dist.append(list(i+base[x] for i in base))
        return computed_dist

    def set_first_move(self):
        cells = self.cells.copy()
        x_prev, y_prev, x_current, y_current = self.x_prev, self.y_prev, self.x, self.y
        move_and_result = {'X': None, 'Y': None, 'CELLS': None}
        bomb_dir_evaluation = {
            'COLDER':   move_and_result.copy(),
            'WARMER':   move_and_result.copy(),
            'SAME':     move_and_result.copy()
            }

        self.cells_first_moves  = bomb_dir_evaluation.copy()
        self.cells_second_moves = {}
        self.cells_second_moves['COLDER'] = bomb_dir_evaluation.copy()
        self.cells_second_moves['WARMER'] = bomb_dir_evaluation.copy()
        self.cells_second_moves['SAME']   = bomb_dir_evaluation.copy()

        def clean_cells_list(bomb_dir:str, cells:set, x_prev:int, y_prev:int, x_current:int, y_current:int):
            return_cells = cells.copy()
            for x, y in cells.copy():
                if bomb_dir != is_closer(x, y, x_prev, y_prev, x_current, y_current):
                    return_cells.remove((x,y))
            print(f'\n-----> clean_cells_list <-----', file=sys.stderr, flush=True)
            print(f'-----> bomb_dir = {bomb_dir} \t x_prev: {x_prev} 	 y_prev: {y_prev} 	 x_current: {x_current} 	 y_current: {y_current}', file=sys.stderr, flush=True)
            print(f'----------> len(return_cells) = {len(return_cells)}', file=sys.stderr, flush=True)
            return return_cells

        def is_closer(x, y, x_prev, y_prev, x_current, y_current):
            old_dist = self.distance_list[abs(x_prev - x)][abs(y_prev - y)]
            new_dist = self.distance_list[abs(x_current - x)][abs(y_current - y)]

            if old_dist > new_dist:
                return 'WARMER'
            elif old_dist < new_dist:
                return 'COLDER'
            else:
                return 'SAME'

        def seek_best_choice(cells:set, x_current:int, y_current:int):
            print(f'-----> seek_best_choice <----- cells_len {len(cells)}', file=sys.stderr, flush=True)
            # cells_len = len(cells)
            removed_cells_counter = 0
            next_jump = None

            # if self.debug and cells_len < 5:
            #         print(f'x = {self.x}\t y = {self.y}', file=sys.stderr, flush=True)

            for x_in_test, y_in_test in cells:
                counter = 0
                # remaining_cells = cells_len
                # if self.debug and cells_len < 5:
                #         print(f'x_in_test = {x_in_test}\t y_in_test = {y_in_test}', file=sys.stderr, flush=True)
                for x, y in self.cells:
                    new_dist = self.distance_list[abs(x_in_test - x)][abs(y_in_test - y)]
                    old_dist = self.distance_list[abs(x_current - x)][abs(y_current - y)]
                    counter += new_dist > old_dist
                    # remaining_cells -= 1
                    # if self.debug and cells_len < 5:
                    #     print('\t', x, y, file=sys.stderr, flush=True)
                    #     print(f'\t old_dist         = {old_dist}',          file=sys.stderr, flush=True)
                    #     print(f'\t new_dist         = {new_dist}',          file=sys.stderr, flush=True)
                    #     print(f'\t counter          = {counter}',           file=sys.stderr, flush=True)
                    #     print(f'\t remaining_cells  = {remaining_cells}',   file=sys.stderr, flush=True)
                    #     print(f'\t removed_cells_counter = {removed_cells_counter}\n', file=sys.stderr, flush=True)

                    # if counter + remaining_cells < removed_cells_counter:
                    #     break

                if counter > removed_cells_counter:
                    removed_cells_counter = counter
                    next_jump = (x, y)

            return next_jump

        for first_bomb_dir in ['COLDER', 'WARMER', 'SAME']:
            cells_first_moves = clean_cells_list(first_bomb_dir, cells, self.x_prev, self.y_prev, self.x, self.y)
            self.cells_first_moves[first_bomb_dir]['CELLS'] = cells_first_moves.copy()

            x, y = seek_best_choice(cells_first_moves, self.x, self.y)
            self.cells_first_moves[first_bomb_dir]['X'] = x
            self.cells_first_moves[first_bomb_dir]['Y'] = y
            for second_bomb_dir in ['COLDER', 'WARMER', 'SAME']:
                cells_second_moves = clean_cells_list(
                    second_bomb_dir, self.cells_first_moves[first_bomb_dir]['CELLS'], self.x, self.y, x, y)
                self.cells_second_moves[first_bomb_dir][second_bomb_dir]['CELLS'] = cells_second_moves.copy()
                x2, y2 = seek_best_choice(cells_first_moves, self.x, self.y)
                self.cells_second_moves[first_bomb_dir][second_bomb_dir]['X'] = x2
                self.cells_second_moves[first_bomb_dir][second_bomb_dir]['Y'] = y2

    def play_first_move(self):
        bomb_dir = input()
        if self.debug:
            print(f'------> bomb_dir = {bomb_dir}', file=sys.stderr, flush=True)
        self.bat_move()
        first_bomb_dir = input()
        self.cells = self.cells_first_moves[first_bomb_dir]['CELLS']

        self.x_prev, self.y_prev = self.x, self.y
        self.x, self.y = self.cells_first_moves[first_bomb_dir]['X'], self.cells_first_moves[first_bomb_dir]['Y']

        second_bomb_dir = input()
        self.cells = self.cells_second_moves[first_bomb_dir][second_bomb_dir]['CELLS']
        self.x_prev, self.y_prev = self.x, self.y
        self.x, self.y = self.cells_second_moves[first_bomb_dir][second_bomb_dir]['X'], self.cells_second_moves[first_bomb_dir][second_bomb_dir]['Y']


class Square:

    def __init__( self, name:str, x_min:int, x_max:int, y_min:int, y_max:int ):
        self.name = name
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def is_in(self, x, y):
        return (    self.x_min <= x
                and self.x_max >= x
                and self.y_min <= y
                and self.y_max >= y )

bat_mov = Bat_Move (w, h, x0, y0)
