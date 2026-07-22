import random

# 1. Create cards
def create_cards():
    cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D']
    random.shuffle(cards)
    return cards

# 2. Display board
def display_board(cards, matched):
    print("\nMemory Board")
    for i in range(len(cards)):
        if matched[i]:
            print(cards[i], end=" ")
        else:
            print(i, end=" ")
    print()

# 3. Get user choice
def get_choice():
    first = int(input("Enter first card index: "))
    second = int(input("Enter second card index: "))
    return first, second

# 4. Check if cards match
def check_match(cards, matched, first, second):
    if cards[first] == cards[second]:
        matched[first] = True
        matched[second] = True
        print("✅ Match Found!")
    else:
        print("❌ Not a Match!")

# 5. Check game over
def game_over(matched):
    return all(matched)

# 6. Show result
def show_result():
    print("\n🎉 Congratulations!")
    print("You matched all the cards.")



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
