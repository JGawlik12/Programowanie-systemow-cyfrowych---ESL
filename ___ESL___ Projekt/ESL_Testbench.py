#Automat sterujący światłem w pomieszczeniu, jeżeli są w nim osoby
# IRSensor1, IRSensor2 - Czujniki podczerwieni, odpowiadające za kierunek wchodzenia/wychodzenia
# IRLED - dioda podczerwieni, modulowana 38kHz na potrzeby czujników typu TSOPxxxx
# LightRelay - Stan światła
# Reset - reset automatu
from inspect import trace
from myhdl import *
from ESL_Automat import *

def Testbench():

    CLOCK100MHZ, IRSensor1, IRSensor2, Reset, LightRelay = [Signal(bool(0)) for i in range(5)]
    CLOCK1KHZ = Signal(bool(0))
    CLOCK38KHZ = Signal(bool(0))
    IRLED = Signal(bool(0))
    sDividerCounter = Signal(intbv(0, min=0, max=65535))
    sGeneratorCounter = Signal(intbv(0, min=0, max=65535))
    sState = Signal(intbv(0,min=0,max=7))
    sCounter = Signal(intbv(0, min=0, max=65535))

    #Generacja zegara
    @always(delay(5))
    def CLKGen():
        CLOCK100MHZ.next = not CLOCK100MHZ

    #Prescaler zegara
    @always(CLOCK100MHZ.posedge)
    def Prescaler():
        if sDividerCounter != 49999:
            sDividerCounter.next = sDividerCounter + 1
        else:
            sDividerCounter.next = 0
            CLOCK1KHZ.next = not CLOCK1KHZ

    #Generator 38kHz
    @always(CLOCK100MHZ.posedge)
    def Gen():
        if sGeneratorCounter == 1315:
            sGeneratorCounter.next = 0
            CLOCK38KHZ.next = not CLOCK38KHZ
        else:
            sGeneratorCounter.next = sGeneratorCounter + 1

        if CLOCK38KHZ == 1 and CLOCK1KHZ == 1:
            IRLED.next = 1
        else:
            IRLED.next = 0

    #Stimulus
    @instance
    def Stimulus():
        IRSensor1.next = 0
        IRSensor2.next = 0
        Reset.next = 1
        for i in range(3):
            yield CLOCK100MHZ.negedge
        IRSensor1.next = 0
        IRSensor2.next = 0
        Reset.next = 0
        for i in range(3):
            yield CLOCK100MHZ.negedge
        IRSensor1.next = 0
        IRSensor2.next = 0
        Reset.next = 1    
        for i in range(100000):
            yield CLOCK100MHZ.negedge
        IRSensor1.next = 1
        IRSensor2.next = 0
        Reset.next = 1
        for i in range(100000):
            yield CLOCK100MHZ.negedge
        IRSensor1.next = 1
        IRSensor2.next = 1
        Reset.next = 1
        for i in range(100000):
            yield CLOCK100MHZ.negedge
        IRSensor1.next = 0
        IRSensor2.next = 1
        Reset.next = 1
        for i in range(100000):
            yield CLOCK100MHZ.negedge
        IRSensor1.next = 0
        IRSensor2.next = 0
        Reset.next = 1


        #Instancja automatu
    Instance = Automat(CLOCK100MHZ,CLOCK38KHZ,CLOCK1KHZ,sState,sCounter, IRSensor1, IRSensor2, Reset, LightRelay)

    return CLKGen, Gen, Prescaler, Stimulus, Instance

def simulate(timesteps):
    tb = traceSignals(Testbench)
    sim = Simulation(tb)
    sim.run(timesteps)

simulate(10000000)
