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
A = numpy.loadtxt('lab2mat.txt') 
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
B = numpy.loadtxt('lab2b.txt') 
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