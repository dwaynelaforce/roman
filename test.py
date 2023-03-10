import random

from roman import from_roman, to_roman, RomanNumeral

TEST_CASES = [
    (2, "II"),
    (10, "X"),
    (20, "XX"),
    (22, "XXII"),
    (222, "CCXXII"),
    (2222, "MMCCXXII"),
    (1922, "MCMXXII"),
    (800, "DCCC"),
    (433, "CDXXXIII"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (4, "IV"),
    (40, "XL"),
    (9, "IX"),
    (999, "CMXCIX"),
]

def main():
    test_to_roman()
    test_from_roman()
    test_class_ops()
    print("\nall tests passed.")
    
def test_from_roman():
    for num, roman in TEST_CASES:
        test = from_roman(roman)
        try:
            assert(test == num)
        except AssertionError as error:
            raise type(error)(f"{roman} should equal {num}, but got {test} instead.")

def test_to_roman():
    for num, roman in TEST_CASES:
        test = to_roman(num)
        try:
            assert(test == roman)
        except AssertionError as error:
            raise type(error)(f"{num} should equal {roman}, but got {test} instead.")

def test_class_ops():
    num = 20
    roman = "XX"
    r = RomanNumeral(20)
    try:
        assert(str(r) == r.roman)
        assert(repr(r) == f"RomanNumeral({num}, {roman})")
        assert(int(r) == r.arabic)
        
        assert(r == RomanNumeral(roman))
        assert(r == num)
        assert(r == roman)
        
        assert(r != RomanNumeral(21))
        assert(r != 21)
        assert(r != "XXI")

        assert(r < RomanNumeral(21))
        assert((r < r) is False)
        assert((r < RomanNumeral(19)) is False)
        assert(r < 21)
        assert((r < num) is False)
        assert((r < 19) is False)
        assert(r < "XXI")
        assert((r < roman) is False)
        assert((r < "XIX") is False)
        
        assert(r <= RomanNumeral(21))
        assert((r <= r) is True)
        assert((r <= RomanNumeral(19)) is False)
        assert(r <= 21)
        assert((r <= num) is True)
        assert((r <= 19) is False)
        assert(r <= "XXI")
        assert((r <= roman) is True)
        assert((r <= "XIX") is False)
        
        assert((r > RomanNumeral(21)) is False)
        assert((r > r) is False)
        assert((r > RomanNumeral(19)) is True)
        assert((r > 21) is False)
        assert((r > num) is False)
        assert((r > 19) is True)
        assert((r > "XXI") is False)
        assert((r > roman) is False)
        assert((r > "XIX") is True)
        
        assert((r >= RomanNumeral(21)) is False)
        assert((r >= r) is True)
        assert((r >= RomanNumeral(19)) is True)
        assert((r >= 21) is False)
        assert((r >= num) is True)
        assert((r >= 19) is True)
        assert((r >= "XXI") is False)
        assert((r >= roman) is True)
        assert((r >= "XIX") is True)
        
        assert(r + RomanNumeral(10) == RomanNumeral(30))
        assert(r + 10 == RomanNumeral(30))
        assert(r + "X" == RomanNumeral(30))
        
        assert(r - RomanNumeral(10) == RomanNumeral(10))
        assert(r - 10 == RomanNumeral(10))
        assert(r - "X" == RomanNumeral(10))
        
        assert(r * RomanNumeral(10) == RomanNumeral(200))
        assert(r * 10 == RomanNumeral(200))
        assert(r * "X" == RomanNumeral(200))

        try:
            r / 2
        except NotImplementedError:
            pass
        else:
            raise AssertionError
        
        assert(r // RomanNumeral(11) == RomanNumeral(1))
        assert(r // 11 == RomanNumeral(1))
        assert(r // "XI" == RomanNumeral(1))

        assert(r % RomanNumeral(3) == RomanNumeral(2))
        assert(r % 3 == RomanNumeral(2))
        assert(r % "III" == RomanNumeral(2))
        
        assert(divmod(r, RomanNumeral(3)) == (RomanNumeral(6), RomanNumeral(2)))
        assert(divmod(r, 3) == (RomanNumeral(6), RomanNumeral(2)))
        assert(divmod(r, "III") == (RomanNumeral(6), RomanNumeral(2)))
        
        assert(r ** RomanNumeral(2) == RomanNumeral(400))
        assert(r ** 2 == RomanNumeral(400))
        assert(r ** "II" == RomanNumeral(400))
        
        try:
            -r
        except NotImplementedError:
            pass
        else:
            raise AssertionError


    except BaseException as e:
        print(f"{num=}, {roman=}")
        raise e


if __name__ == "__main__":
    main()