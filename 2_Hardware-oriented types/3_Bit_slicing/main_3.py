from myhdl import bin, intbv
if __name__ == "__main__":
        a = intbv(6, min=-3, max=7)
        print(len(a))
        b = a[4:]
        intbv(6)
        print(len(b))
        print(b.min)
        print(b.max)


