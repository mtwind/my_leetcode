class Main:
    def is_colorful(self, num):
        results = {}
        numStr = str(num)
        

        # loop through each digit in the number
        for index, val in enumerate(numStr):
            product = int(val)
            if product in results:
                    return False
            results[product] = numStr[index]
            # create a new array with the digits after the current digit
            subNum = numStr[index + 1:]

            newNum = val
            # loop through the numbers after the current digit and add the products of their digits to the dict
            for k, val2 in enumerate(subNum):
                newNum = newNum + "" + val2
                product = self.get_product(int(newNum))
                if product in results:
                    return False
                results[product] = newNum
        return True

    @staticmethod
    def get_product(digits):
        if digits < 10:
            return digits
        num = digits
        product = 1
        while num > 0:
            product *= num % 10
            num //= 10
        return product

if __name__ == "__main__":
    colorful = Main()
    print("326 Colorful -", colorful.is_colorful(3256))
    print("3245 Colorful -", colorful.is_colorful(3245))
    print("32458 Colorful -", colorful.is_colorful(32458))


