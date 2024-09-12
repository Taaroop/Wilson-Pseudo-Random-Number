# Dice roll
# This program relies on the fact that a (p-1)x(p-1) grid is a Latin square if p is a prime and the value of the (i, j)th cell is ij (mod p).
# To show this, consider the ith row. Say two columns j and j' give the same cell value, that is, ij = ij' (mod p). Since i < p and p is a prime, gcd(i, p) = 1.
# So, dividing both sides of the congruence by i, we get j = j' (mod p). Since j and j' are both also smaller than p, it implies that j = j'.
# We can use the same argument for a fixed column.
# Thus, the grid is a Latin Square where each row and each column contains the values 1 to p-1.
# Coincidentally, six is the number of faces on a dice and it just so happens that 6+1 = 7 is a prime!

def dice():
    from datetime import datetime

    row = int(str(datetime.now())[20:23])%6
    column = int(str(datetime.now())[23:])%6

    if row == 0:
        row = 6
    if column == 0:
        column = 6
    
    return (row*column)%7 # 7 is a prime number


li = [0, 0, 0, 0, 0, 0]

for i in range(1000):
    result = dice()
    li[result-1] += 1

print(li)
