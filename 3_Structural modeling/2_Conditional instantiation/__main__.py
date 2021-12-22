from myhdl import block

SLOW, MEDIUM, FAST = range(3)

@block
def top(..., speed=SLOW):
    ...
    def slowAndSmall():
       ...
    ...
    def fastAndLarge():
       ...
    if speed == SLOW:
        return slowAndSmall()
    elif speed == FAST:
        return fastAndLarge()
    else:
        raise NotImplementedError