from wordfreq import top_n_list
from collections import Counter
import re

def get_words(language: str, length: int, top_n: int = 10000):
    """Return top N words of a given length in the specified language ('en' or 'fr')."""
    valid_langs = {'en': 'English', 'fr': 'French'}
    if language not in valid_langs:
        raise ValueError("Language must be 'en' or 'fr'")

    words = top_n_list(language, top_n)
    return [w for w in words if len(w) == length and w.isalpha()]

def crossword_candidates(length: int,
                         fixed: list[tuple[str, int]],
                         required: list[str],
                         excluded: list[str] = [],
                         language: str = 'en',
                         top_n: int = 10000):
    """
    Return a list of candidate words of given length and language that:
    - have fixed letters at given positions
    - contain all required letters (unordered)
    - do not contain any excluded letter (unordered)
    - come from the top `top_n` most frequent words
    """
    pattern = ["." for _ in range(length)]
    for letter, pos in fixed:
        if not (1 <= pos <= length):
            raise ValueError(f"Position {pos} is out of bounds for word length {length}")
        pattern[pos-1] = letter.lower()
    fixed_re = re.compile("".join(pattern))

    required_counter = Counter(letter.lower() for letter in required)
    word_list = get_words(language, length, top_n)

    result = []
    for word in word_list:
        if not fixed_re.fullmatch(word):
            continue
        word_counter = Counter(word)
        if all(word_counter[c] >= k for c, k in required_counter.items()):
            result.append(word)

    # filtering excluded letters
    result = [r for r in result if not any(letter in r for letter in excluded)]

    return result

if __name__ == "__main__":
    print("Crossword Solver (EN/FR)")
    lang = input("Choose language (en/fr): ").strip().lower()
    length = int(input("Target word length: "))

    # Get fixed letter constraints
    fixed = []
    print("Enter fixed letter constraints (format: a 1 b 2 for 'a' at position 1 and 'b' at position 2). Blank line to end.")
    line = input("> ").strip()
    parts = line.split()
    if line and len(parts) % 2 == 0:
        for i in range(0, len(parts) - 1, 2):
            try:
                letter, pos = parts[i], int(parts[i + 1])
                fixed.append((letter, pos))
            except Exception as e:
                print("Invalid format. Use character + integer combinations.")
                continue
    elif len(parts) % 2 != 0:
        print("Invalid format. Use: <letter> <position>")

    required = list(input("Enter required letters (in any order, e.g. 'rt' or 'éa'): ").strip())

    excluded = list(input("Enter excluded letters(in any order, e.g. 'rt' or 'éa'): ").strip())

    matches = crossword_candidates(length, fixed, required, excluded, language=lang, top_n=10000)
    print(f"\nFound {len(matches)} matches:\n")
    print(", ".join(matches[:50]))
    if len(matches) > 50:
        print("...")
