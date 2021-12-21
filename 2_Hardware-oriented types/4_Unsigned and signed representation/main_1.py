from myhdl import bin, intbv, Signal
if __name__ == "__main__":
        a = intbv(12, min=0, max=16)
        print(bin(a))
        b = a.signed()
        print(b)
        print(bin(b, width=4))



