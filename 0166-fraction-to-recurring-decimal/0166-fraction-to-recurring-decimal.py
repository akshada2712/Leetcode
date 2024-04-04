class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
#         rem = numerator % denomintor
        
#         if rem == 0:
#             return str(numerator / denominator)
        
#         else:
        sign = '-' if numerator * denominator < 0 else ''
        q, r = divmod(abs(numerator), abs(denominator))
        res = [sign, str(q), '.']

        remain = []

        while r not in remain:
            remain.append(r)
            q, r = divmod(r * 10, abs(denominator))
            res.append(str(q))

        idx = remain.index(r)
        res.insert(idx+3, '(')
        res.append(')')
        #res = ''.join(result).replace('(0)','').rstrip('.')
        res = ''.join(res).replace('(0)','').rstrip('.')
        return res