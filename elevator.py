



A_ = [40, 40, 100, 80, 20]
B_ = [3, 3, 2, 2, 3]
M_ = 3 
X_ = 5
Y_= 200

class Solution(object):
    def solution(self, A, B, M, X, Y):
        print(A, B, M, X, Y)
        print("============================")        
        #電梯停幾次
        stepCount = 0
        index = 0
        while A:
            index = self.loading(A, X, Y)
            #print(index)

            if index == 0:
                arrWeightBuffer = A
                arrFloorBuffer = B
            else:
                arrWeightBuffer = A[:index]
                arrFloorBuffer = B[:index]

            print(arrWeightBuffer)
            print(arrFloorBuffer)

            stepCount += len(set(arrFloorBuffer))
            stepCount += 1 #回到ground
            print(stepCount)

            if index == 0:
                A = []
                B = []
            else:
                A = A[index:]
                print(A)
                B = B[index:]
                print(B)
            print("============================")

        return stepCount


    def loading(self, arrWeight,resPeople, resWeight):
        capacity = 0
        for index, elem in enumerate(arrWeight):
            #電梯可以進去幾人
            if capacity + elem < resWeight and index + 1 <= resPeople:
                capacity += elem
            else:
                # full loading
                index -= 1
                break
        index += 1
        print("index {}, capacity {}".format(index, capacity))
        return index









if __name__ == "__main__":
    print(Solution().solution( A_, B_, M_, X_, Y_))
