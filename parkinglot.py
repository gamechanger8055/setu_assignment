'''
Parking lot
Statement :
Design and develop a system to manage parking allocation for a parking lot of size X
4-wheelers and Y 2-wheelers.
The system should adhere to the following conditions:
1. Nearest parking slot to the entrance gate is allocated first.-->>stacks
2. Parking rates are static (you can decide).
3. System should support the concept of “rush hours”. Which is, during rush hours,
a 4 wheeler parking lot can be broken into 2 2-wheeler parking lot and similarly 2
2-wheeler parking lot can be merged into 1 4-wheeler parking lot at runtime.
4. The system should optimize the use of the slots, especially during rush hour
5. The system should be able to calculate fees for the time the vehicles have been
parked
6. The system can simulate time, i.e. 1 minute can be 1 hour and every 24 minutes
is a day.
Build an interface, API, CLI or UI to:
1. Create a parking lot with X 4-wheelers and Y 2-wheeler slots.
2. Allocate a slot to an incoming vehicle.
3. Deallocate a slot to an outgoing vehicle and calculate fees.
4. Turn on and off the rush hour flag
5. Get status of the parking lot, includes number of vehicles currently parked, total
amount collected etc,.
'''

from enum import Enum

class ParkingSpot(Enum):
    TWOWHEELER, FOURWHEELER=1,2

class Timings(Enum):
    NORMAL, RUSH=1,2

class ParkingRate(Enum):
    TWOWHEELER_RATE, FOURWHEELER_RATE=5,10
class ParkingLot:
    def __init__(self,name,address,spots):
        self.name=name
        self.address=address
        self.spot=spots
        

class Address(self,street,city,state,country):
    self.street=street
    self.city=city
    self.state=state
    self.country=country

class Spot:
    def __init__(self):
        p=ParkingSpot()
        self.p.TWOWHEELER=X
        self.p.FOURWHEELER=Y
        self.currtwoparking=[]
        self.currfourparking=[]
        self.twowheelerlist=['cycle','bike']
        self.fourwheelerlist=['car','truck','auto']
        self.twowheelercount=0
        self.fourwheelercount=0
        self.totalfees=0
    
    def addparking(self,vtype,time_type,time_taken):
        q=Timings
        if vtype in self.twowheelerlist:
            if self.twowheelercount<self.p.TWOWHEELER:
                self.currtwoparking.append(vtype)
                self.twowheelercount+=1
                fees=self.calculatefees(vtype,time_taken)
                self.totalfees+=fees
            else:
                if time_type==q.RUSH:
                    self.rushparking(vtype)
                else:
                    print("Two wheeler slot full")
        if vtype in self.fourwheelerlist:
            if self.fourwheelercount<self.p.FOURWHEELER:
                self.currfourparking.append(vtype)
                self.fourwheelercount+=1
                fees=self.calculatefees(vtype,time_taken)
                self.totalfees+=fees
            else:
                if time_type==q.RUSH:
                    self.rushparking(vtype)
                else:
                    print("Four wheeler slot full")
    
    def rushparking(self,vtype):
        if vtype in self.twowheelerlist:
            if self.fourwheelercount<self.p.FOURWHEELER:
                self.currfourparking.append(vtype)
                self.fourwheelercount+=0.5
                fees=self.calculatefees(vtype,time_taken)
                self.totalfees+=fees
            else:
                print("No space left")
        if vtype in self.fourwheelerlist:
            if self.twowheelercount<self.p.TWOWHEELER:
                self.currtwoparking.append(vtype)
                self.twowheelercount+=2
                fees=self.calculatefees(vtype,time_taken)
                self.totalfees+=fees
            else:
                print("No space left")
    
    def calculatefees(self,vtype,time_taken):
        w=ParkingRate()
        fees=0
        if vtype in self.twowheelerlist:
            fees=time_taken*w.TWOWHEELER_RATE
        else:
            fees=time_taken*w.FOURWHEELER_RATE
        return fees
    
    def totalfeeslot(self):
        return self.totalfees
    
    def totalparked(self):
            return self.twowheelercount+self.fourwheelercount


        
            
    
    
        
        



    