"The puzzle game Wordle!"

__author__: str = "730824666"


def contains_char(text: str, char: str) -> bool:
    """Check if a given character is present in the given text string."""
    assert len(char) == 1, f"len('{char}') is not 1"

    for letter in text:
        if letter == char:
            return True
    return False


WHITE_BOX = "\U00002B1C"
GREEN_BOX = "\U0001F7E9"
YELLOW_BOX = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Converts a guess into an emoji string based on Wordle's color-coding rules."""
    assert len(guess) == len(secret), "Guess must be the same length as secret"

    emoji_result = ""

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            emoji_result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX

    return emoji_result


def input_guess(expected_length: int) -> str:
    """Prompts the user for a guess of a specified length and ensures valid input."""
    while True:
        guess = input(f"Enter a {expected_length} character word: ")
        if len(guess) == expected_length:
            return guess
        print(f"That wasn't {expected_length} chars! Try again: ")


def main(secret: str) -> None:
    """The entry point of the program and the main game loop."""
    MAX_ATTEMPTS = 6
    attempts = 0
    word_length = len(secret)

    while attempts < MAX_ATTEMPTS:
        print(f"=== Turn {attempts + 1}/{MAX_ATTEMPTS} ===")
        guess = input_guess(word_length)
        print(emojified(guess, secret))
        attempts += 1

        if guess == secret:
            print(f"You won in {attempts}/{MAX_ATTEMPTS} turns!")
            return

    print(f"X/{MAX_ATTEMPTS} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
