from myhdl import intbv
if __name__ == "__main__":
        a = intbv(6, min=0, max=7)
        print(len(a))
        a = intbv(6, min=-3, max=7)
        print(len(a))
        a = intbv(6, min=-13, max=7)
        print(len(a))