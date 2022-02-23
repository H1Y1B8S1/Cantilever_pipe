import numpy as np
import pandas as pd

lengthL = []


def chk(A, element):
    deldel2 = []
    AAA = A.copy()
    Elelist = np.arange(element - 1, element, 0.05)
    FElelist = [round(i, 2) for i in Elelist]
    FElelist.append(element)
    FElelist.sort(reverse=True)

    loss = 0
    size = len(AAA)
    B = [0] * size
    for length in FElelist:
        if length not in lengthL:
            lengthL.append(length)

            count = 0

            if length <= element:
                for i in range(0, size):

                    for j in range(i + 1, size):
                        if (
                            B[i] == 0
                            and B[j] == 0
                            and (round(AAA[i] + AAA[j], 2) == length)
                        ):
                            count += 1
                            loss += round((element - round(A[i] + A[j], 2)), 2)
                            deldel2.append(round(AAA[i], 2))
                            B[i] = 1

                            deldel2.append(round(AAA[j], 2))
                            B[j] = 1

    for d in deldel2:
        if d in AAA:
            AAA.remove(d)

    for i in range(0, len(AAA)):
        loss += element - A[i]

    # print("total perfect pairs are:",count)
    # print(B)
    return round(loss, 2)
    # print(round(loss,2))


# df = pd.read_excel('python\Cantiliver\Tube_data.xlsx', sheet_name=0)
# A = df["BT"].tolist()
# A = [round(ele, 2) for ele in A]
# A = [3.1, 3.15, 3.2, 3.3, 3.45, 3.5, 3.6, 3.6, 3.65, 3.7]
# A = [3.05, 3.05, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.55, 3.55, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.65, 3.65, 3.65, 3.65, 3.65, 3.65, 3.65, 3.65, 3.65, 3.65, 3.65, 3.85, 3.95, 4.05, 4.05, 4.15, 4.15]
# length = 6.95


def Callingfun(A, length):
    sugglist = np.arange(length - 1, length + 1, 0.05)
    Fsugglist = [round(i, 2) for i in sugglist]
    Fsugglist.append(length)
    # print(Fsugglist)
    list = []

    for ele in Fsugglist:
        list.append(chk(A, ele))

    # print(list)
    Optimalval = Fsugglist[list.index(min(list))]
    # print(Optimalval)
    return Optimalval


# x = Callingfun(A,length)
# print(x)
