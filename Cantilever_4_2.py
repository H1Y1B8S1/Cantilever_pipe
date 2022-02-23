import pandas as pd
import numpy as np
import suggestion_0_2 as sugg
import time, sys, itertools, threading

deldel = []


# Function to find and print pair
def chkPair(A, Mlength):

    Lanlist = np.arange(Mlength - 1, Mlength, 0.05)
    FLanlist = [round(i, 2) for i in Lanlist]
    FLanlist.append(Mlength)
    FLanlist.sort(reverse=True)

    loss = 0
    size = len(A)
    B = [0] * size
    for length in FLanlist:
        count = 0
        if length <= Mlength:
            for i in range(0, size):
                for j in range(i + 1, size):
                    if (B[i] == 0 and B[j] == 0
                            and (round(A[i] + A[j], 2) == length)):
                        print(
                            f"Pair with a length {length} is {round(A[i],2),round(A[j],2)}"
                        )
                        count += 1
                        loss += round((Mlength - round(A[i] + A[j], 2)), 2)
                        deldel.append(round(A[i], 2))
                        B[i] = 1

                        deldel.append(round(A[j], 2))
                        B[j] = 1

        if count > 0:
            print(f"> Total pair with {length} : {count}\n")

    for d in deldel:
        if d in A:
            A.remove(d)
    if (A):
        print(f"Left ele in list :\n> {A}\n")

    for i in range(0, len(A)):
        loss += (Mlength - A[i])

    return round(loss, 2)


df = pd.read_excel('python\Cantilever\Tube_data.xlsx',sheet_name = 0)
A = df["BT"].tolist()
A = [round(ele,2) for ele in A]
# A = [3.1, 3.15, 3.2, 3.3, 3.45, 3.5, 3.6, 3.6, 3.65, 3.7]

dupA = A.copy()
length = 6.95

loss = chkPair(A, length)
print(f"Total loss with length {length} is : {loss}")
print("\n")

###################################################
                    # SUGGESTION #
###################################################

done = False

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write("\r> Calculating and Finding Optimal length " + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!                                                               ')


t = threading.Thread(target=animate)
t.start()

maxval = sugg.Callingfun(dupA, length)
if length == maxval:
    print(f"\n> PERFACT \n>With lenth {length} minimun losses occurs")
else:
    print(
        f"\n> Optimal length found : With length {maxval} there will be minumum losses. Try length : '{maxval}'"
    )

time.sleep(0.1)
done = True