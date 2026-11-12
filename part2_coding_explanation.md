# Part 2 — Variable-length coding

## Why my coding is decodable

My coding follows the **prefix rule**, which means no letter’s code is the beginning of another letter’s code. The three 3-bit codes are `000`, `001`, and `010`. None of the 4-bit codes begins with any of those patterns. All codes are unique, so the decoder can read from left to right and output a letter as soon as it finds a complete code. For example, `0001001` decodes to `op` because `000` represents `o` and `1001` represents `p`.

## Why my coding outperforms 4-bit fixed-length coding

The sentence “fanchao is a super cool person” contains **25 letters** when spaces are excluded. Fixed-length coding uses 4 bits per letter, for a total of **25 × 4 = 100 bits**.

In my coding, `o`, `a`, and `s` appear **10 times combined** and use 3 bits per occurrence, for a total of 30 bits. The other 15 letter occurrences use 4 bits each, for a total of 60 bits. The encoded message uses **30 + 60 = 90 bits**, saving **10 bits (10%)** on this sentence.
