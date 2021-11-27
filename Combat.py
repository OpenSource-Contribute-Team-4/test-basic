MAX_UNITS = 72000;
planeCrashWin = False
usrArmy = 0 
usrNavy = 0
usrAir = 0
cpuArmy = 30000
cpuNavy = 20000
cpuAir = 22000

def attackFirst():
    global usrArmy,usrNavy,usrAir
    global cpuArmy,cpuNavy,cpuAir
    
    numUnits = 0
    unitType = 0
    
    while unitType<1 or unitType>3:
        print("YOU ATTACK FIRST. TYPE (1) FOR ARMY; (2) FOR NAVY;")
        print("AND (3) FOR AIR FORCE.")
        print("?", end=' ')
        unitType = int(input())
    
    while (numUnits<0) or ((unitType == 1) and (numUnits > usrArmy)) or ((unitType == 1) and (numUnits > usrNavy)) or ((unitType == 1) and (numUnits > usrAir)):
        print("HOW MANY MEN")
        print("?",end=' ')
        numUnits = int(input())
    
    if unitType == 1:
        if numUnits < (usrArmy/3) :
            print("YOU LOST " + numUnits + " MEN FROM YOUR ARMY.")
            usrArmy = usrArmy - numUnits
        elif numUnits < (2*usrArmy/3):
            print("YOU LOST " + int(numUnits/3) +  " MEN, BUT I LOST "+ int(2*cpuArmy/3))
            usrArmy = int(usrArmy - (numUnits/3))
            cpuArmy = 0 
        else:
            print("YOU SUNK ONE OF MY PATROL BOATS, BUT I WIPED OUT TWO")
            print("OF YOUR AIR FORCE BASES AND 3 ARMY BASES.")
            usrArmy =  int(usrArmy/3)
            usrAir = int(usrAir/3)
            cpuNavy = int(2*cpuNavy/3)
    elif unitType == 2:
        if numUnits < cpuNavy / 3 :
            print("YOUR ATTACK WAS STOPPED!")
            usrNavy = usrNavy - numUnits
        elif numUnits < 2*cpuNavy/3:
            print("YOU DESTROYED " + int(2 * cpuNavy / 3) + " OF MY ARMY.")
            cpuNavy = int(cpuNavy/3)
        else:
            print("YOU SUNK ONE OF MY PATROL BOATS, BUT I WIPED OUT TWO")
            print("OF YOUR AIR FORCE BASES AND 3 ARMY BASES.")
            usrArmy = int(usrArmy/3)
            usrAir = int(usrAir/3)
            cpuNavy = int(2*cpuNavy/3)
    elif unitType == 3:
        if numUnits < usrAir/3:
            print("YOUR ATTACK WAS WIPED OUT.")
            usrAir = usrAir - numUnits
        elif numUnits < 2*usrAir/3 :
            print("WE HAD A DOGFIGHT. YOU WON - AND FINISHED YOUR MISSION.")
            cpuArmy = int(2*cpuArmy/3)
            cpuNavy = int(cpuNavy/3)
            cpuAir = int(cpuAir/3)       
        else:
            print("YOU WIPED OUT ONE OF MY ARMY PATROLS, BUT I DESTROYED")
            print("TWO NAVY BASES AND BOMBED THREE ARMY BASES.")
            usrArmy = int(usrArmy/4)
            usrNavy = int(usrNavy/3)
            cpuArmy = int(2*cpuArmy/3)
            
def main():
    attackFirst();
    
if __name__ == '__main__':
    usrArmy = 0 
    usrNavy = 0
    usrAir = 0
    cpuArmy = 30000
    cpuNavy = 20000
    cpuAir = 22000
    main()
    