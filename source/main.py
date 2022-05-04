class main():

    if __name__ == "__main__":
        eqn = "x^3 + y + 3^2"
        eqn = eqn.replace("^","**")
        print(eqn)

        print(eval(eqn,{'x':3,'y':7}))

