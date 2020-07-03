import numpy
#Steven Tucker
#112829702
#Lab2
print("*****STEVEN TUCKER*****")
print("*****112829702*****")
print("*****LAB2*****")


#PROBLEM ONE-----classicalGS that takes an nxk matrix.  Outputs an nxk matrix Q and a kxk upper matrix R
def classicalGS(A):
    Q = A.copy()
    n = len(A)
    R=numpy.zeros_like(A)
    for j in range(0,n):
        #v= Q[:,j]
        for i in range(0, j):  #this translates to 0 (or 1) to j-1 because it stops BEFORE J
            R[i,j]=numpy.matmul(Q[:,i],A[:,j])
            Q[:, j] = Q[:, j] - R[i, j] * Q[:,i]
        norm = numpy.linalg.norm(Q[:, j])
        R[j, j] = norm
        Q[:, j] = Q[:, j] / R[j, j]


    return Q, R

#PROBLEM 2---- Modified to be stable
def modifiedGS(A):
    Q = A.copy()
    n = len(A)
    R=numpy.zeros_like(A)
    for j in range(0,n):
        #v= Q[:,j]
        for i in range(0, j):  #this translates to 0 (or 1) to j-1 because it stops BEFORE J
            R[i,j]=numpy.matmul(Q[:,i],Q[:,j])
            Q[:, j] = Q[:, j] - R[i, j] * Q[:,i]
        norm = numpy.linalg.norm(Q[:, j])
        R[j, j] = norm
        Q[:, j] = Q[:, j] / R[j, j]

    return Q, R


def BackwardsSubstitution(mat):

    returnArray=[1] * len(mat)
    i = len(mat) -1 

    returnArray[i] = mat[i][i+1]/mat[i][i]
    i -=1
    while i >= 0:


        for col in range(i+1, len(mat)):
            if mat[i][col] > 0:

                num = mat[i][col] * returnArray[col]
                newNum = mat[i][len(mat)]-num
                mat[i][len(mat)] = newNum
                mat[i][col] = 0
                #BackwardsSubstitution(mat)
            else:

                returnArray[i] = mat[i][len(mat)]/mat[i][i]
        i-=1

    return(returnArray)





#PROBLEM 3A
ThreeAmatrix = numpy.array([[1., 3., 2., 1.,],
                            [4., 2., 1., 2.,],
                            [2., 1., 2., 3.,],
                            [1., 2., 4., 1.,]])

ThreeAMatB = numpy.array([[-2.], [2.], [1.], [-1]])
print("PROBLEM 3a)")
A = ThreeAmatrix 
Q, R = classicalGS(A)
QTB = numpy.matmul(Q,ThreeAMatB)
Augmented = numpy.append(R, QTB, axis =1)
print("QTB\n", QTB)
print("Augmented\n", Augmented)

print("Final Answer- Result of backsub: \n", BackwardsSubstitution(Augmented), "\n\n")


#PROBLEM 3B---- Repeated using ModifiedGS
print("PROBLEM 3b)")
A = ThreeAmatrix 
Q, R = modifiedGS(A)
QTB = numpy.matmul(Q,ThreeAMatB)
Augmented = numpy.append(R, QTB, axis =1)
print("QTB\n", QTB)
print("Augmented\n", Augmented)
print("Final Answer- Result of backsub: \n", BackwardsSubstitution(Augmented), "\n\n")
#PROBLEM 3C
print("PROBLEM 3c) i:")
<<<<<<< HEAD
A = numpy.loadtxt('numerical_files/lab2mat.txt') 
=======
A = numpy.loadtxt('lab2mat.txt') 
>>>>>>> fa9bfceb818b75d7783748369b42281da70ec0e4
Qc, Rc = classicalGS(A)
Qm, Rm = modifiedGS(A)

#first Calculate the inner
QcRc=numpy.matmul(Qc,Rc)
norm = numpy.linalg.norm(A-QcRc, ord = "fro")
print("Classical Norm \n", norm)

#first Calculate the inner
QmRm=numpy.matmul(Qm,Rm)
norm = numpy.linalg.norm(A-QmRm, ord = "fro")
print("Modified Norm \n", norm)
print("Q:   Do Q and R for each algorithm accurately represent A?")
print("A:   They both look pretty similar judging by the norm comparisons.\n\n")

#Testing for Othogon-mality(? is that the word?)
print("PROBLEM 3c) ii:")
QTc = Qc.transpose()
QTcQc = numpy.matmul(QTc,Qc)
I = numpy.identity(len(QTcQc))
inner = numpy.subtract(QTcQc,I)
norm = numpy.linalg.norm(inner, ord="fro")
print("Classical norm\n", norm)

QTm = Qm.transpose()
QTmQm = numpy.matmul(QTm,Qm)
I = numpy.identity(len(QTcQc))
inner = numpy.subtract(QTmQm,I)
norm = numpy.linalg.norm(inner, ord="fro")
print("Modified norm\n", norm)
print("Q:    Are Qc and Qm approximately orthogonal?")
print("A:    Yes they are approximately orthoganal\n\n")

#Lab2btxt
<<<<<<< HEAD
B = numpy.loadtxt('numerical_files/lab2b.txt') 
=======
B = numpy.loadtxt('lab2b.txt') 
>>>>>>> fa9bfceb818b75d7783748369b42281da70ec0e4
Q, R = classicalGS(A)
QTB = numpy.matmul(Q.transpose(),B)
QTB = numpy.array([QTB.tolist()])
QTB = numpy.transpose(QTB, (1,0))

Augmented = numpy.append(R, QTB, axis =1)
print("Backsub on ClassicalGS with lab2b.txt\n\n", BackwardsSubstitution(Augmented))

#Repeated using ModifiedGS
Q, R = modifiedGS(A)
QTB = numpy.matmul(Q.transpose(),B)
QTB = numpy.array([QTB.tolist()])
QTB = numpy.transpose(QTB, (1,0))
Augmented = numpy.append(R, QTB, axis =1)
print("\nBacksub on ModifiedGS with lab2b.txt\n\n", BackwardsSubstitution(Augmented))


# --- Output ---
"""
*****STEVEN TUCKER*****
*****112829702*****
*****LAB2*****
PROBLEM 3a)
QTB
 [[ 0.5335105 ]
 [-2.16514725]
 [-1.47238993]
 [ 1.69102685]]
Augmented
 [[ 4.69041576  3.19801075  2.98481003  3.41121146  0.5335105 ]
 [ 0.          2.78796113  3.03251913  0.39129279 -2.16514725]
 [ 0.          0.          2.62578309  1.00220729 -1.47238993]
 [ 0.          0.          0.          1.4852969   1.69102685]]
Final Answer- Result of backsub:
 [1, 1, 1, 1.1385109964350721]


PROBLEM 3b)
QTB
 [[ 0.5335105 ]
 [-2.16514725]
 [-1.47238993]
 [ 1.69102685]]
Augmented
 [[ 4.69041576  3.19801075  2.98481003  3.41121146  0.5335105 ]
 [ 0.          2.78796113  3.03251913  0.39129279 -2.16514725]
 [ 0.          0.          2.62578309  1.00220729 -1.47238993]
 [ 0.          0.          0.          1.4852969   1.69102685]]
Final Answer- Result of backsub:
 [1, 1, 1, 1.1385109964350728]


PROBLEM 3c) i:
Classical Norm
 3.3647040155923796e-16
Modified Norm
 3.5048391058910664e-16
Q:   Do Q and R for each algorithm accurately represent A?
A:   They both look pretty similar judging by the norm comparisons.


PROBLEM 3c) ii:
Classical norm
 0.7999804096464574
Modified norm
 2.751109354006973e-11
Q:    Are Qc and Qm approximately orthogonal?
A:    Yes they are approximately orthoganal


Backsub on ClassicalGS with lab2b.txt

 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -7.069928782744028e-06]

Backsub on ModifiedGS with lab2b.txt

 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7.588988732643001e-09]
 """
