from myhdl import bin, intbv
if __name__ == "__main__":
        a = intbv(-3)
        print(bin(a, width=5))
        b = a[5:]
        b
        print(bin(b))


