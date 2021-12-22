#Projekt automatu sterowania światłem w pomieszczeniu
from myhdl import *

def Automat(CLOCK100MHZ,CLOCK38KHZ,CLOCK1KHZ,sState,sCounter, IRSensor1, IRSensor2, Reset, LightRelay):

#Sterowanie światłem
    @instance
    def Drive():
        yield CLOCK100MHZ.posedge
        if sCounter != 0:
            LightRelay.next = 1
        else:
            LightRelay.next = 0


#Maszyna stanów
    @instance
    def StateMachine():
        yield CLOCK100MHZ.posedge
        if Reset == 0:
            sState.next = 0
            sCounter.next = 0
        elif CLOCK1KHZ == 1:
            if sState == 0:
                if IRSensor1 == 0 and IRSensor2 == 0:
                    sState.next = 0
                elif IRSensor1 == 1 and IRSensor2 == 0:
                    sState.next = 1
                elif IRSensor1 == 0 and IRSensor2 == 1:
                    sState.next = 4
                elif IRSensor1 == 1 and IRSensor2 == 1:
                    sState.next = 7
            elif sState == 1:
                if IRSensor1 == 0 and IRSensor2 == 0:
                    sState.next = 0
                elif IRSensor1 == 1 and IRSensor2 == 0:
                    sState.next = 1
                elif IRSensor1 == 0 and IRSensor2 == 1:
                    sState.next = 3
                elif IRSensor1 == 1 and IRSensor2 == 1:
                    sState.next = 2                
            elif sState == 4:
                if IRSensor1 == 0 and IRSensor2 == 0:
                    sState.next = 0
                elif IRSensor1 == 1 and IRSensor2 == 0:
                    sState.next = 6
                elif IRSensor1 == 0 and IRSensor2 == 1:
                    sState.next = 4
                elif IRSensor1 == 1 and IRSensor2 == 1:
                    sState.next = 5   
            #############################################
            elif sState == 2:
                if IRSensor1 == 0 and IRSensor2 == 0:
                    sState.next = 0
                elif IRSensor1 == 1 and IRSensor2 == 0:
                    sState.next = 1
                elif IRSensor1 == 0 and IRSensor2 == 1:
                    sState.next = 3
                elif IRSensor1 == 1 and IRSensor2 == 1:
                    sState.next = 2   
            elif sState == 5:
                if IRSensor1 == 0 and IRSensor2 == 0:
                    sState.next = 0
                elif IRSensor1 == 1 and IRSensor2 == 0:
                    sState.next = 6
                elif IRSensor1 == 0 and IRSensor2 == 1:
                    sState.next = 4
                elif IRSensor1 == 1 and IRSensor2 == 1:
                    sState.next = 5 
            ###############################################
            elif sState == 3:
                if IRSensor1 == 0 and IRSensor2 == 0:
                    sState.next = 0
                    sCounter.next = sCounter + 1
                elif IRSensor1 == 1 and IRSensor2 == 0:
                    sState.next = 0
                elif IRSensor1 == 0 and IRSensor2 == 1:
                    sState.next = 3
                elif IRSensor1 == 1 and IRSensor2 == 1:
                    sState.next = 2     
            elif sState == 6:
                if IRSensor1 == 0 and IRSensor2 == 0:
                    sState.next = 0
                    sCounter.next = sCounter - 1
                elif IRSensor1 == 1 and IRSensor2 == 0:
                    sState.next = 6
                elif IRSensor1 == 0 and IRSensor2 == 1:
                    sState.next = 0
                elif IRSensor1 == 1 and IRSensor2 == 1:
                    sState.next = 5    
            ###############################################
            elif sState == 7:
                if IRSensor1 == 0 and IRSensor2 == 0:
                    sState.next = 0
                elif IRSensor1 == 1 and IRSensor2 == 0:
                    sState.next = 6
                elif IRSensor1 == 0 and IRSensor2 == 1:
                    sState.next = 3
                elif IRSensor1 == 1 and IRSensor2 == 1:
                    sState.next = 7
    
    return StateMachine, Drive