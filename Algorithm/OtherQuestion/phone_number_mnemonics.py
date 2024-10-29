from typing import Dict, Tuple, Iterable, List
from itertools import product


phone_mapping: Dict[str, Tuple[str, ...]] = {"1": ("1",),
                                             "2": ("a", "b", "c"),
                                             "3": ("d", "e", "f"),
                                             "4": ("g", "h", "i"),
                                             "5": ("j", "k", "l"),
                                             "6": ("m", "n", "o"),
                                             "7": ("p", "q", "r", "s"),
                                             "8": ("t", "u", "v"),
                                             "9": ("w", "x", "y", "z"),
                                             "0": ("0",)}


def possible_mnemonics(phone_number:str) -> Iterable[Tuple[str, ...]]:
    letter_tuple: List[Tuple[str, ...]] = []
    for digit in phone_number:
        letter_tuple.append(phone_mapping.get(digit, (digit,)))
    return product(*letter_tuple)


if __name__ == '__main__':
    phone_number: str = input("Enter your phone number: ")
    print("Here are the potential mnemonics:")
    for mnemonic in possible_mnemonics(phone_number):
        print("".join(mnemonic))
