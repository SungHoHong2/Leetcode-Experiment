class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # print(data)

        binaryArray = []

        for item in data:
            temp = item
            tmpArray = []
            while temp > 0:
                # print(temp % 2)
                tmpArray.append(temp % 2)
                temp = temp // 2

            while len(tmpArray) < 8:
                tmpArray.append(0)

            tmpArray.reverse()
            binaryArray.append(tmpArray)

        binaryArray.reverse()
        rdNext = 0
        working = False

        while len(binaryArray):

            item = binaryArray.pop()

            # print(item)
            if not rdNext:
                count = 0
                # print('start',item)
                for i in item:
                    if i == 1:
                        count += 1
                    else:
                        break

                if count > 4:
                    return False

                if item[0] == 1 and item[1] == 0:
                    return False

                rdNext = count - 1

                if rdNext < 0:
                    rdNext = 0

                if item[0] != 0:
                    working = True


            else:
                # print('next', item)
                if not (item[0] == 1 and item[1] == 0):
                    return False

                rdNext -= 1

                if rdNext == 0:
                    working = False

        if working:
            return False

        print(rdNext)
        if rdNext > 0:
            return False

        return True