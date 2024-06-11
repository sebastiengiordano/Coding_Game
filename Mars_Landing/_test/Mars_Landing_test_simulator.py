from itertools import product
from Mars_Landing.Mars_Landing import Movement


if __name__ == "__main__":
    Landing_input = [[2500, 2700, 0, 0, 550, 0, 0], [2500, 2699, 0, -3, 549, -15, 1], [2501, 2695, 1, -5, 547, -30, 2], [2503, 2689, 3, -6, 544, -45, 3], [2508, 2683, 6, -7, 540, -45, 4], [2516, 2675, 9, -8, 536, -45, 4], [2526, 2666, 12, -9, 532, -45, 4], [2539, 2657, 15, -10, 528, -45, 4], [2555, 2647, 18, -11, 524, -45, 4], [2574, 2636, 20, -12, 520, -44, 4], [2596, 2624, 23, -12, 516, -43, 4], [2620, 2611, 26, -13, 512, -42, 4], [2647, 2597, 28, -15, 509, -41, 3], [2675, 2582, 29, -17, 507, -40, 2], [2705, 2563, 30, -20, 506, -39, 1], [2735, 2542, 30, -23, 505, -38, 1], [2765, 2518, 31, -25, 504, -37, 1], [2796, 2491, 31, -28, 503, -36, 1], [2828, 2461, 32, -31, 502, -35, 1], [2860, 2429, 33, -34, 501, -34, 1], [2893, 2393, 33, -37, 500, -33, 1], [2927, 2355, 34, -39, 498, -32, 2], [2961, 2316, 36, -40, 495, -31, 3], [2998, 2275, 38, -40, 491, -30, 4], [3037, 2235, 40, -41, 487, -29, 4], [3077, 2194, 41, -41, 483, -28, 4], [3120, 2153, 43, -41, 479, -27, 4], [3164, 2112, 45, -41, 475, -26, 4], [3210, 2071, 47, -41, 471, -25, 4], [3257, 2030, 48, -41, 467, -24, 4], [3307, 1988, 50, -41, 463, -23, 4], [3357, 1947, 51, -41, 459, -22, 4], [3409, 1906, 53, -41, 455, -21, 4], [3463, 1865, 54, -41, 451, -20, 4], [3518, 1824, 56, -41, 447, -19, 4], [3574, 1783, 57, -41, 443, -18, 4], [3631, 1742, 58, -41, 439, -17, 4], [3690, 1701, 59, -41, 435, -16, 4], [3749, 1660, 60, -41, 431, -15, 4], [3810, 1619, 61, -40, 427, -14, 4], [3872, 1579, 62, -40, 423, -13, 4], [3934, 1539, 63, -40, 419, -12, 4], [3997, 1499, 64, -40, 415, -11, 4], [4061, 1459, 64, -40, 411, -10, 4], [4126, 1420, 65, -39, 407, -9, 4], [4191, 1381, 65, -39, 403, -8, 4], [4256, 1342, 66, -39, 399, -7, 4], [4322, 1303, 66, -39, 395, -6, 4], [4389, 1264, 67, -38, 391, -5, 4], [4456, 1226, 67, -39, 388, -4, 3], [4523, 1187, 67, -39, 384, -3, 4], [4590, 1148, 67, -38, 380, -2, 4], [4657, 1109, 67, -39, 377, -1, 3], [4725, 1070, 67, -39, 373, -1, 4], [4792, 1031, 67, -39, 369, -1, 4], [4859, 993, 68, -38, 365, -1, 4], [4927, 954, 68, -39, 362, -1, 3], [4994, 915, 67, -39, 358, 14, 4], [5060, 876, 65, -39, 354, 29, 4], [5123, 837, 62, -40, 350, 44, 4], [5183, 797, 59, -41, 346, 45, 4], [5241, 755, 56, -42, 342, 45, 4], [5296, 713, 53, -43, 338, 45, 4], [5348, 670, 51, -43, 334, 45, 4], [5397, 626, 48, -44, 330, 45, 4], [5443, 582, 45, -45, 326, 45, 4], [5487, 536, 42, -46, 322, 45, 4], [5527, 489, 39, -47, 318, 45, 4], [5565, 442, 36, -48, 314, 45, 4], [5601, 394, 34, -48, 310, 30, 4], [5634, 346, 33, -48, 306, 15, 4], [5668, 298, 33, -48, 302, 0, 4], [5701, 251, 33, -47, 298, 0, 4]]
    Landing_command = [[-15 , 4], [-30 , 4], [-45 , 4], [-45 , 4], [-45 , 4], [-45 , 4], [-45 , 4], [-45 , 4], [-44 , 4], [-43 , 4], [-42 , 4], [-41 , 3], [-40 , 2], [-39 , 1], [-38 , 1], [-37 , 1], [-36 , 1], [-35 , 1], [-34 , 1], [-33 , 1], [-32 , 2], [-31 , 3], [-30 , 4], [-29 , 4], [-28 , 4], [-27 , 4], [-26 , 4], [-25 , 4], [-24 , 4], [-23 , 4], [-22 , 4], [-21 , 4], [-20 , 4], [-19 , 4], [-18 , 4], [-17 , 4], [-16 , 4], [-15 , 4], [-14 , 4], [-13 , 4], [-12 , 4], [-11 , 4], [-10 , 4], [-9 , 4], [-8 , 4], [-7 , 4], [-6 , 4], [-5 , 4], [-4 , 3], [-3 , 4], [-2 , 4], [-1 , 3], [-1 , 4], [-1 , 4], [-1 , 4], [-1 , 3], [14 , 4], [29 , 4], [44 , 4], [45 , 4], [45 , 4], [45 , 4], [45 , 4], [45 , 4], [45 , 4], [45 , 4], [45 , 4], [45 , 4], [0 , 4], [0 , 4], [0 , 4], [0 , 4]]


    mov = Movement(*Landing_input[0])
    print(f'x = {mov.x}')
    print(f'y = {mov.y}')
    print(f'h_speed = {mov.h_speed}')
    print(f'v_speed = {mov.v_speed}')
    
    def check_movement(mov, x, y, h_speed, v_speed, fuel, rotate, power):
        print()
        print(f"\t Test x       {' OK ' if mov.get_x() == x else f'FAIL'} \t x = {mov.get_x()} attendu {x}")
        print(f"\t Test y       {' OK ' if mov.get_y() == y else f'FAIL'} \t y = {mov.get_y()} attendu {y}")
        print(f"\t Test h_speed {' OK ' if mov.get_h_speed() == h_speed else f'FAIL'} \t h_speed = {mov.get_h_speed()} attendu {h_speed}")
        print(f"\t Test v_speed {' OK ' if mov.get_v_speed() == v_speed else f'FAIL'} \t v_speed = {mov.get_v_speed()} attendu {v_speed}")
        print(f"\t Test rotate  {' OK ' if mov.rotate == rotate else f'FAIL'} \t rotate = {mov.rotate} attendu {rotate}")
        print(f"\t Test power   {' OK ' if mov.power == power else f'FAIL'} \t power = {mov.power} attendu {power}")
        print(f"\t Test fuel    {' OK ' if mov.fuel == fuel else f'FAIL'} \t fuel = {mov.fuel} attendu {fuel}")
        return not (    mov.get_x() == x
                    and mov.get_y() == y
                    and mov.get_h_speed() == h_speed
                    and mov.get_v_speed() == v_speed
                    and mov.rotate == rotate
                    and mov.power == power )

    error_count = 0
    for landing_input, command in zip(Landing_input[1:], Landing_command):
        mov.command(*command)
        error_count += check_movement(mov, *landing_input)
        if error_count > 5:
            break
