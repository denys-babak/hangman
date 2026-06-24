import random

hangman = {
    1: r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    2: r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    3: r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    4: r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
    5: r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
    6: r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
}

answer_word_list = ["PLANET", "ORANGE", "CASTLE", "FOREST", "WINDOW", "PYTHON", "LETTER"]

while True:   # NEW GAME LOOP

    answer_word = random.choice(answer_word_list)

    hidden_word = "_ " * len(answer_word)
    remaining_mistakes = 6
    max_mistakes = 6
    incorrect_letters = []
    used_letters = []


    print("\n🎮 Welcome to Hangman. You have 6 lives to guess a word!")
    print("╰┈➤EXIT➡Type 'EXIT' anytime to quit")
    print("🤔 You can also guess the whole word.")
    print("=" * 40)
    print("❓ Hidden word:", hidden_word)
    print("=" * 40)

    # GAME LOOP
    while remaining_mistakes > 0 and "_" in hidden_word:

        picked_letter = input("Pick a letter or a word: ").upper()

        if picked_letter == "EXIT":
            print("👋 Game exited")
            exit()


        if len(picked_letter) > 1:
            if picked_letter == answer_word:
                print("🎉 You won! The word was:", answer_word)
                break
            else:
                print("❌ Wrong word!")
                remaining_mistakes -= 1
                print(f"❌ Mistakes left: {remaining_mistakes}")
                print(hangman[6 - remaining_mistakes])
                continue

        if not picked_letter.isalpha():
            print("Please enter letters only")
            continue

        if picked_letter in used_letters:
          print("⚠️ You've already used this letter. Try another one.")
          continue

        used_letters.append(picked_letter)

        index_count = 0

        for letter in answer_word:
            if letter == picked_letter:
                hidden_word = (
                    hidden_word[:index_count * 2] +
                    picked_letter +
                    hidden_word[index_count * 2 + 1:]
                )
            index_count += 1

        if picked_letter in answer_word:
            print(f"✅ Correct: {picked_letter}")
        else:
            remaining_mistakes -= 1
            incorrect_letters.append(picked_letter)
            print(f"❌ Mistakes left: {remaining_mistakes}")
            print(hangman[max_mistakes - remaining_mistakes])
            print("Incorrect letters:", incorrect_letters)

        print("❓ Hidden word:", hidden_word)
        print("=" * 40)

    # GAME END
    if remaining_mistakes == 0:
        print("\n" + "💀 GAME OVER 💀".center(40, "-"))
        print("Better luck next time!")
    else:
        print("\n" + "🎉 CONGRATULATIONS!".center(40, "-"))
        mistakes = max_mistakes - remaining_mistakes
        print(f"You saved the word with {mistakes} mistake(s)! 🔥")

    print(f"📝 The word was: {answer_word}")

    # PLAY AGAIN OPTION
    again = input("\nPlay again? (yes/no): ").lower()
    if again not in("yes","y"):
        print("👋 Bye!")
        break
