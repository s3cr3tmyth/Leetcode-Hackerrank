
number = 99999999


def to_words(num):

    below_20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]

    tens = ["","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]

    thousands = ["Thousand","Million","Billion"]

    def helper(num):

        if num == 0:
            return []

        if num < 20:
            return [below_20[num]]

        if num < 100:
            x, y = divmod(num,10)
            return [tens[x-1]] + helper(y)

        if num < 1000:
            x, y = divmod(num, 100)
            return [below_20[x], 'Hundred'] + helper(y)

        for poww, thousand in enumerate(thousands,1):
            if num < 1000**(poww+1):
                x, y =  divmod(num, 1000** poww)
                # x, y = num // 1000 ** poww, num % 1000 ** poww
                return helper(x) + [thousand] + helper(y)

    return ' '.join(helper(num)) or 'Zero'



print(to_words(number))



