class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {"M":1000, "CM":900,"D":500,"CD":400,"C":100,"XC":90,"L": 50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
        numeral = ""
        for entry in roman_dict:
            while num - roman_dict[entry] >= 0:
                num = num - roman_dict[entry]
                numeral = numeral + entry
        return numeral
