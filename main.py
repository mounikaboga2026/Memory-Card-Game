from memory_module import *

cards = create_cards()
matched = [False] * len(cards)

print("===== MEMORY CARD GAME =====")

while not game_over(matched):
    display_board(cards, matched)

    try:
        first, second = get_choice()

        if first == second:
            print("Choose two different cards!")
            continue

        if first < 0 or second < 0 or first >= len(cards) or second >= len(cards):
            print("Invalid index!")
            continue

        print("Card", first, "=", cards[first])
        print("Card", second, "=", cards[second])

        check_match(cards, matched, first, second)

    except ValueError:
        print("Please enter valid numbers.")

show_result()