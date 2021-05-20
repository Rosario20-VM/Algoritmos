import matplotlib.pyplot as plt

def DDA(x1,y1,x2,y2,color):
    dx= abs(x2-x1)
    dy= abs(y2-y1)
    steps=0

    if (dx)> (dy):
        steps=(dx)
    else:
        steps=(dy)
    xInc = float(dx / steps)
    yInc = float(dy / steps)

    xInc = round(xInc,1)
    yInc = round(yInc,1)

    for i in range(0, int(steps + 1)):
        plt.plot(round(x1),round(y1),color)
        x1+=xInc
        y1+=yInc
        print(x1)
        print(y1)

    plt.show()

def main():
    x1=int(input("Ingresa x1: "))
    y1=int(input("Ingresa y1: "))
    x2=int(input("ingresa x2: "))
    y2=int(input("Ingresa y2: "))
    color="r."

    DDA(x1,y1, x2, y2,color)

if __name__ == '__main__':
    main()