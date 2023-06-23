
x = 100 

def add(x,y) :
    print("locals", locals())
    return x+y

if __name__ == "__main__" :       ## 처음으로 모듈을 호출할 때
    print(" 처음 모듈을 출력한다. ")   ## 모듈이 main으로 처리됨 
    print(" globals x =", globals()['x'])
    
    add(100,200)
