# به نام خدا

import random


def monty_hall_game(switch_doors: bool) -> bool:
    """
    :param bool switch_doors: If True, the contestant will switch their choice after a goat door is revealed.
    """

    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)

    initial_choice = random.choice(range(3))

    # If contestant decides to switch
    if switch_doors:
        doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] != 'car']
        door_revealed = random.choice(doors_revealed)
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        # Keep the initial choice
        final_choice = initial_choice
    
    return doors[final_choice] == 'car'


def simulate_game(number_games: int) -> None:
    num_wins_without_switching = sum([monty_hall_game(False) for _ in range(number_games)])
    num_wins_with_switching = sum([monty_hall_game(True) for _ in range(number_games)])

    return num_wins_without_switching, num_wins_with_switching


if __name__ == '__main__':
    number_games = 1000
    win_percent_without_switching, win_percent_with_switching = simulate_game(number_games)
