def pow_modulo(A, B, C):
    if B == 0:
        return 1 % C
    
    result = pow_modulo(A, B // 2, C)
    result = (result * result) % C
    
    if B % 2 == 1:
        result = (result * A) % C
    
    return result

A,B,C=map(int,input("enter numbers: ").split())
result = pow_modulo(A, B, C)
print(result)

