w1 = 11
b = 5

def perceptron1(a,b):
    w1 = 5
    b = -8
    value = a*w1+b
    
    # 활성함수
    if value>0:
        y1 = 1
    else:
        y1 = 0
    return y1
