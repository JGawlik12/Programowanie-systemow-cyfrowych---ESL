from myhdl import bin, intbv
if __name__ == "__main__":
        a = intbv(24)
        print(bin(a))
        print(bin(a[4:]))
        a[4:] = '0001'
        print(bin(a))
        a[:] = 0b10101
        print(bin(a))