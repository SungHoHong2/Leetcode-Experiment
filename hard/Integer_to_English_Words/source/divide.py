class Solution:
    def numberToWords(self, num):
        def one(num):
            switcher = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return switcher.get(num)

        def twenty(num):
            switcher = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return switcher.get(num)

        def ten(num):
            switcher = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return switcher.get(num)

        # get the string from the number with three digits
        def two(num):
            # case1: number is below 10
            if num < 10:
                return one(num)
            # case2: number is below 20
            elif num < 20:
                return twenty(num)
            # case3: number is between 21 ~ 99
            else:
                tenner = num // 10
                rest = num - tenner * 10
                return ten(tenner) + ' ' + one(rest) if rest else ten(tenner)

        def three(num):
            # get the number above hundred
            hundred = num // pow(10,2)
            rest = num - hundred * pow(10,2)
            # case1: 123 or 103
            if hundred and rest:
                return one(hundred) + ' Hundred ' + two(rest)
            # case2: 100
            elif hundred and not rest:
                return one(hundred) + ' Hundred'
            # case3: 023 or 003
            elif not hundred and rest:
                return two(rest)

        # get the number above billion
        billion = num // pow(10,9)
        # get the number above million
        million = (num - billion * pow(10,9)) // pow(10,6)
        # get the number above thousand
        thousand = (num - billion * pow(10,9) - million * pow(10,6)) // pow(10,3)
        # get the below thousand
        rest = num - billion * pow(10,9) - million * pow(10,6) - thousand * pow(10,3)
        # return string 'zero' of the input is invalid
        if not num:
            return 'Zero'
        # construct a string from the integer
        result = ''
        if billion:
            result = three(billion) + ' Billion'
        if million:
            result += ' ' if result else ''
            result += three(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += three(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += three(rest)
        # return the accumulated string
        return result