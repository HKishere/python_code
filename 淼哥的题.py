import math as m
L = float(input('please input the value of L:'))
A = float(input('please input the value of A:'))
B = float(input('please input the value of B:'))
L_ = m.sqrt(3) / 3 * L + m.sqrt(6) / 6 * A + m.sqrt(2) / 2 * B
M_ = m.sqrt(3) / 3 * L + m.sqrt(6) / 6 * A - m.sqrt(2) / 2 * B
S_ = m.sqrt(3) / 3 * L - m.sqrt(6) / 3 * A
L = pow(10,L_)
M = pow(10,M_)
S = pow(10,S_)
R = 4.4679 * L - 3.5873 * M + 0.1193 * S
G = -1.286 * L + 2.3809 * M - 0.1624 * S
B = 0.0497 * L - 0.2439 * M + 1.2045 * S
print("R = %d" %R)
print("G = %d" %G)
print("B = %d" %B)
