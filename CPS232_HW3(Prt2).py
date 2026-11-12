# Counter counts how many times each letter appears in the sentence.
from collections import Counter


def encode(text, codes):
    # Start with an empty string to hold the encoded message.
    encoded_bits = ""

    # Look up each letter in the code table and add its bits to the message.
    for letter in text:
        encoded_bits += codes[letter]

    return encoded_bits


def decode(bits, codes):
    # The original table maps letters to codes. Reverse it so we can
    # look up a letter when we find its code.
    letters_by_code = {}
    for letter, code in codes.items():
        letters_by_code[code] = letter

    # Keep track of the letters we've decoded and the bits we're reading now.
    decoded_letters = ""
    current_code = ""

    for bit in bits:
        # Build one code a bit at a time.
        current_code += bit

        # The prefix rule lets us use the first match. A complete code
        # cannot be the start of a longer code in this table.
        if current_code in letters_by_code:
            decoded_letters += letters_by_code[current_code]

            # Reset so the next bit starts a new letter's code.
            current_code = ""

    # Leftover bits mean the message ended without a complete code.
    if current_code:
        raise ValueError("The bit string ends with an incomplete or invalid code.")

    return decoded_letters


def main():
    # Use the sentence from Part 2. Remove spaces because the problem
    # asks us to encode the letters in the sentence.
    sentence = "fanchao is a super cool person"
    letters = sentence.replace(" ", "")

    # Count the letters so we can print how often each one appears.
    frequencies = Counter(letters)

    # Give the three most frequent letters 3-bit codes to save one bit
    # each time they appear. Give the remaining letters 4-bit codes.
    # Each 4-bit code starts with a different pattern from 000, 001, and 010.
    codes = {
        "o": "000",
        "a": "001",
        "s": "010",
        "c": "0110",
        "e": "0111",
        "n": "1000",
        "p": "1001",
        "r": "1010",
        "f": "1011",
        "h": "1100",
        "i": "1101",
        "l": "1110",
        "u": "1111",
    }

    # Show the original sentence and how many letters will be encoded.
    print(f"Original sentence: {sentence}")
    print(f"Letters to encode: {len(letters)}")

    # Print one row per letter. The <8 and <11 align the columns.
    print("\nLetter  Frequency  Code")
    for letter, code in codes.items():
        print(f"{letter:<8}{frequencies[letter]:<11}{code}")

    # Start by assuming the table satisfies the prefix rule.
    prefix_free = True

    # Check each code against the codes for all the other letters.
    # Skip comparisons where both letters are the same.
    for letter, code in codes.items():
        for other_letter, other_code in codes.items():
            if letter != other_letter and code.startswith(other_code):
                prefix_free = False

    print(f"\nPrefix rule satisfied: {prefix_free}")

    # Encode the letters, then decode the bits to check that we get
    # back the same sequence of letters.
    encoded = encode(letters, codes)
    decoded = decode(encoded, codes)

    print(f"Encoded bits: {encoded}")
    print(f"Decoded letters: {decoded}")
    print(f"Decoded letters match the input: {decoded == letters}")

    # Fixed-length coding uses 4 bits for every letter.
    fixed_bits = len(letters) * 4

    # For variable-length coding, count the bits the encoder produced.
    variable_bits = len(encoded)

    # Subtract the new size from the original size to find the savings.
    print(f"\nFixed-length coding: {fixed_bits} bits")
    print(f"Variable-length coding: {variable_bits} bits")
    print(f"Bits saved: {fixed_bits - variable_bits}")


# Run the demonstration when this file is run directly.
if __name__ == "__main__":
    main()