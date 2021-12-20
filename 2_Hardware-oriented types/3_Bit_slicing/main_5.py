from myhdl import bin, intbv
if __name__ == "__main__":
        a = intbv(24)[5:]
        print(a.min)
        print(a.max)
        print(len(a))

