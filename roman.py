"""
This module provides functions for converting integers to roman numerals and
vice versa, along with a RomanNumeral class that can represent a roman numeral
that can be operated on mathematically.
"""

from __future__ import annotations
from typing import Union, Self, Tuple
from warnings import warn

ROMAN_MAP = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000,
}
MIN_NUMBER = 1
MAX_NUMBER = 3999

def to_roman(num: int) -> str:
    """
    Takes an integer and returns its roman numeral representation as a string.
    Cannot convert numbers less than 1 or greater than 3999.
    """
    if not isinstance(num, int):
        raise ValueError("'num' argument must be type <int>.")
    elif num < MIN_NUMBER:
        raise ValueError(f"Only numbers >= {MIN_NUMBER} are supported.")
    elif num > MAX_NUMBER:
        raise ValueError(f"It is not possible to convert a number > {MAX_NUMBER}.")
    
    roman: str = ""
    
    q, r = divmod(num, 1000)
    roman += "M" * q
    if r >= 900:
        roman += "CM"
        r -= 900
    elif r >= 500:
        roman += "D"
        r -= 500
    elif r >= 400:
        roman += "CD"
        r -= 400

    q, r = divmod(r, 100)
    roman += "C" * q
    if r >= 90:
        roman += "XC"
        r -= 90
    elif r >= 50:
        roman += "L"
        r -= 50
    elif r >= 40:
        roman += "XL"
        r -= 40

    q, r = divmod(r, 10)
    roman += "X" * q
    if r == 9:
        roman += "IX"
        r -= 9
    elif r >= 5:
        roman += "V"
        r -= 5
    elif r == 4:
        roman += "IV"
        r -= 4

    roman += "I" * r

    return roman
    
def from_roman(roman: str) -> int:
    """
    Takes a roman numeral string and returns the corresponding arabic integer.
    Numbers above 3999 and below 1 are not supported.
    """
    arabic = 0
    i = 0
    while i < len(roman):
        char = roman[i]
        if i < len(roman) - 1:
            nextchar = roman[i+1]
            if val := ROMAN_MAP.get(char + nextchar, False):
                arabic += val
                i += 2
                continue
        arabic += ROMAN_MAP[char]
        i += 1
    if arabic < MIN_NUMBER:
        raise ValueError(f"Only numbers >= {MIN_NUMBER} are supported.")
    elif arabic > MAX_NUMBER:
        raise ValueError(f"It is not possible to convert a number > {MAX_NUMBER}.")
    return arabic

def raise_not_implemented(type1: str, type2: str):
    raise NotImplementedError(
        f"Incompatible operation: <{type1}> and <{type2}>"
    )

class RomanNumeral:
    """
    Represents a roman numeral between 1 and 3999 inclusive that can be used 
    for basic mathematical operations (only those that will result in 
    positive integers). Fractions and floats are not currently supported.
    """
    roman: str
    arabic: int

    def __init__(self, num: int | str) -> Self:
        if isinstance(num, str):
            self.arabic = from_roman(num)
            self.roman = num
        elif isinstance(num, int):
            self.roman = to_roman(num)
            self.arabic = num
        else:
            raise ValueError("RomanNumeral can only be created from int or str")
        
    def __repr__(self) -> str:
        return f"{__class__.__name__}({self.arabic}, {self.roman})"
    
    def __str__(self) -> str:
        return self.roman
    
    def __int__(self) -> int:
        return self.arabic
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, RomanNumeral):
            return self.arabic == other.arabic
        elif isinstance(other, int):
            return self.arabic == other
        elif isinstance(other, str):
            return self.roman == other
        else:
            raise_not_implemented(self.__class__.__name__, 
                                  other.__class__.__name__)
        
    def __lt__(self, other: object) -> bool:
        if isinstance(other, RomanNumeral):
            return self.arabic < other.arabic
        elif isinstance(other, (int, str)):
            return self < RomanNumeral(other)
        else:
            raise_not_implemented(self.__class__.__name__, 
                                  other.__class__.__name__)

    def __le__(self, other: object) -> bool:
        if isinstance(other, RomanNumeral):
            return self.arabic <= other.arabic
        elif isinstance(other, (int, str)):
            return self <= RomanNumeral(other)
        else:
            raise_not_implemented(self.__class__.__name__, 
                                  other.__class__.__name__)
    
    def __gt__(self, other: object) -> bool:
        if isinstance(other, RomanNumeral):
            return self.arabic > other.arabic
        elif isinstance(other, (int, str)):
            return self > RomanNumeral(other)
        else:
            raise_not_implemented(self.__class__.__name__, 
                                  other.__class__.__name__)
    
    def __ge__(self, other: object) -> bool:
        if isinstance(other, RomanNumeral):
            return self.arabic >= other.arabic
        elif isinstance(other, (int, str)):
            return self >= RomanNumeral(other)
        else:
            raise_not_implemented(self.__class__.__name__, 
                                  other.__class__.__name__)
    
    def __add__(self, other: object) -> RomanNumeral:
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.arabic + other.arabic)
        elif isinstance(other, (int, str)):
            return self + RomanNumeral(other)
        else:
            raise_not_implemented(self.__class__.__name__, 
                                  other.__class__.__name__)

    def __sub__(self, other: object) -> RomanNumeral:
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.arabic - other.arabic)
        elif isinstance(other, (int, str)):
            return self - RomanNumeral(other)
        else:
            raise_not_implemented(self.__class__.__name__, 
                                  other.__class__.__name__)

    def __mul__(self, other: object) -> RomanNumeral:
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.arabic * other.arabic)
        elif isinstance(other, (int, str)):
            return self * RomanNumeral(other)
        else:
            raise_not_implemented(self.__class__.__name__, 
                                  other.__class__.__name__)

    def __truediv__(self, other: object) -> RomanNumeral:
        raise NotImplementedError("True division is not supported at this "
                                  "time. Use floor division instead.")

    def __floordiv__(self, other: object) -> RomanNumeral:
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.arabic // other.arabic)
        elif isinstance(other, (int, str)):
            return self // RomanNumeral(other)
        else:
            raise_not_implemented(self.__class__.__name__, 
                                  other.__class__.__name__)

    def __mod__(self, other: object) -> RomanNumeral:
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.arabic % other.arabic)
        elif isinstance(other, (int, str)):
            return self % RomanNumeral(other)
        else:
            raise_not_implemented(self.__class__.__name__, 
                                  other.__class__.__name__)

    def __divmod__(self, other: object) -> Tuple[RomanNumeral]:
        if isinstance(other, RomanNumeral):
            q, r = divmod(self.arabic, other.arabic)
            return RomanNumeral(q), RomanNumeral(r)
        elif isinstance(other, (int, str)):
            return divmod(self, RomanNumeral(other))
        else:
            raise_not_implemented(self.__class__.__name__, 
                                  other.__class__.__name__)

    def __pow__(self, other: object) -> RomanNumeral:
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.arabic ** other.arabic)
        elif isinstance(other, (int, str)):
            return self ** RomanNumeral(other)
        else:
            raise_not_implemented(self.__class__.__name__, 
                                  other.__class__.__name__)
    
    def __bool__(self) -> True:
        warn("Roman numerals are always positive numbers and will "
             "always resolve True.")
        return True

    def __abs__(self) -> Self:
        warn("Roman numerals are always positive numbers, so their absolute "
             "value will be the same.")
        return self
    
    def __float__(self) -> float:
        return float(self.arabic)
    
    def __neg__(self):
        raise NotImplementedError("RomanNumerals are always positive numbers")
    



