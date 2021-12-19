from myhdl import bin, intbv
if __name__ == "__main__":
        a = intbv(24)
        print(bin(a))
        print(int(a[0]))
        print(int(a[3]))
        b = intbv(-23)
        print(bin(b))
        print(int(b[0]))
        print(int(b[3]))
        print(int(b[4]))


        