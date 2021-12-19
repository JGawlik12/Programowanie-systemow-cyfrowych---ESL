from myhdl import bin, intbv
if __name__ == "__main__":
        a = intbv(24)
        print(bin(a))
        a[3] = 0
        print(bin(a))
        a = intbv(16)
        b = intbv(-23)
        print(bin(b))
        b[3] = 0
        print(bin(b))
        b = intbv(-31)


        