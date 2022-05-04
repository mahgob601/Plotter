import  numpy as np

class main():

    if __name__ == "__main__":
        eqn = "200 + x"

        eqn = eqn.replace("^","**")
        print(eqn)

        print(eval(eqn,{'x':3.611111111111}))

        x = np.arange(1,100,1.5)
        x = x.tolist()
        print(x)



