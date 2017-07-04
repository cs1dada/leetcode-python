S_ = "John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker"
C_ = "Example"

class Solution(object):
    def solution(self, S, C):
        # write your code in Python 2.7
        S = S.split("; ")
        result = []

        while S:
            oriBuffer = S[0]
            print(oriBuffer)

            strBuffer = oriBuffer.split()
            print(strBuffer)
            print(len(strBuffer))

            if len(strBuffer) == 2:
                temp = strBuffer[1].lower() + "_" + strBuffer[0].lower() + "@" + C.lower() + ".com"
                print(temp)
            elif len(strBuffer) == 3:
                temp = strBuffer[2].lower() + "_" + strBuffer[0].lower() + "_" + strBuffer[1][0].lower() + "@" + C.lower() + ".com"
                print(temp)

            result.append(temp)
            S = S[1:]
            print("============================")

        return(" ".join(result))

if __name__ == "__main__":
    print(Solution().solution(S_, C_))