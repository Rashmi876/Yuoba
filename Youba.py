#--------------------------------------------------------------
#                           Drivers
#--------------------------------------------------------------
#Constructor
def driver_make(firstName, lastName, carMakeAndModel):
    numberOfTripsCompleted = 0
    return ('Driver', [firstName, lastName, carMakeAndModel, numberOfTripsCompleted])
     
#Selector    
def driver_getFirstName(Driver):
    return Driver[1][0]

def driver_getLastName(Driver):
    return Driver[1][1]

def driver_getCarMakeAndModel(Driver):
    return Driver[1][2]

def driver_getNumberOfTripsCompleted(Driver):
    return Driver[1][3]

def getDriverInfo(driver):
    return driver[1]

#Mutator
def driver_increaseTripsCompleted(Driver):
    Driver[1][3] = driver_getNumberOfTripsCompleted(Driver) + 1

#Predicate
def driver_isNewDriver(Driver):
    return driver_getNumberOfTripsCompleted(Driver) == 0

def is_driver(obj):
    return type(obj) == tuple and obj[0] == "Driver"


#--------------------------------------------------------------
#                           Queues
#--------------------------------------------------------------
#Constructor
def availabilityQueue_make(LocationName):
    return ('AvailabilityQueue', LocationName, [])

#Selectors
def availabilityQueue_getLocationName(AvailabilityQueue):
    return str(AvailabilityQueue[1])

def availabilityQueue_getContents(AvailabilityQueue):
    return AvailabilityQueue[2]

def availabilityQueue_front(AvailabilityQueue):
    return AvailabilityQueue[2][0]


#Mutators
def availabilityQueue_enqueue(AvailabilityQueue, Driver):
    if type(AvailabilityQueue) == tuple and AvailabilityQueue[0] == 'AvailabilityQueue'\
       and type(AvailabilityQueue[2]) == list:
        AvailabilityQueue[2].append(Driver)
        
def availabilityQueue_dequeue(AvailabilityQueue):
    AvailabilityQueue[2].pop(0)

#Predicate
def availabilityQueue_isEmpty(AvailabilityQueue):
    return AvailabilityQueue[2] == []

def availabilityQueue_isQueue(AvailabilityQueue):
    return type(AvailabilityQueue) == tuple and AvailabilityQueue[0] == 'AvailabilityQueue'\
           and type(AvailabilityQueue[2]) == list
    
#They made this
def getAvailabilityQueue(LocationName):
    for availabilityQueue in  availabilityQueue_LIST:
        if availabilityQueue_getLocationName(availabilityQueue) == LocationName:
            return availabilityQueue                        

#---------------------------------------------------------------
#                       Creating Availability Queues
#---------------------------------------------------------------

availabilityQueue_UWI = availabilityQueue_make("UWI")
availabilityQueue_Papine = availabilityQueue_make("Papine")
availabilityQueue_Liguanea = availabilityQueue_make("Liguanea")
availabilityQueue_HalfWayTree = availabilityQueue_make("Half-Way-Tree")


#----------------------------------------------------------------
#                       Discount
#----------------------------------------------------------------

def calculateDiscount(PassengerTelephoneNumber):
    for k,v in knownPassengers.items():
        if k == PassengerTelephoneNumber:
            if v >= 1:
                return 0.1 * v
            else:
                return 0.00


#-------------------------------------------------------------
#                       Calculating Fare
#-------------------------------------------------------------

def calculateDiscount(PassengerTelephoneNumber):
    if PassengerTelephoneNumber in knownPassengers:
        if knownPassengers[PassengerTelephoneNumber] < 10:
            return knownPassengers[PassengerTelephoneNumber] * 0.1
        else:
            return 0.0
    else:
        return 0.0
            
def calculateFare(StartLocation, EndLocation, PassengerTelephoneNumber):
    if StartLocation != EndLocation:
        discount = calculateDiscount(PassengerTelephoneNumber)
        return fare - (fare * discount)
    else:
        print("You are at your location already")


#------------------------------------------------------------
#                       Moving the Taxi
#------------------------------------------------------------
def findingQueue(Location):
    if Location == "UWI": return availabilityQueue_UWI
    elif Location == "Papine": return availabilityQueue_Papine
    elif Location == "Liguanea": return availabilityQueue_Liguanea
    elif Location == "Half-Way-Tree": return availabilityQueue_HalfWayTree



    
def movetaxi(startLocation, endLocation):
    start = findingQueue(startLocation)
    taxi = availabilityQueue_front(start)
    print(start)
    print(taxi)
    availabilityQueue_dequeue(start)

    
    end = findingQueue(endLocation)
    print(end)
    availabilityQueue_enqueue(end, taxi)

    #help
    driver_increaseTripsCompleted(taxi)


#--------------------------------------------------------------
#                       Requesting a Taxi
#--------------------------------------------------------------

def requestTaxi(PassengerTelphoneNumber, PassengerLocation, PassengerDestination):
    if PassengerLocation == PassengerDestination:
        print("Error: Location and Destination are the same")
    else:
        calculateFare(PassengerLocation, PassengerDestination, PassengerTelephoneNumber)
        reply = input("Enter Y to confrim trip and N to cancel")
        if reply == "Y":
            queue = findingQueue(PassengerLocation)
            if not availabilityQueue_isEmpty(queue):
                movetaxi(PassengerLocation, PassengerDestination)
                knowPassengers[PassengerTelephoneNumber] = 0
            else:
                for k, v in knowPassengers.items():
                    if k == PassengerTelephoneNumber:
                        v += 1
                print("Error: There are no available taxi drivers for your cuurent location")
        #else:
            #terminate

#--------------------------------------------------------------
#                         Youba Main  
#--------------------------------------------------------------

def youba_main():
    confirmation = input()
    n = 0

    while (confirmation not "N"):
        passenger = passenger_info[n].split()
        PassengerTelephoneNumber = passenger[0]
        PassengerLocation = passenger[1]
        PassengerDestination = passenger[2]
        requestTaxi(PassengerTelephoneNumber, PassengerLocation, PassengerDestination)
        
        n += 1

        confirmation = input()
        
    print()
    print("List of Drivers and their Number of Completed Trips for the Day")
    listof_availabilityQueues = [availabilityQueue_UWI, availabilityQueue_Papine,\
                                 availabilityQueue_Liguanea, availabilityQueue_HalfWayTree]

    for queue in listof_availabilityQueues:
        for driver in availabilityQueue_getContents(queue):
            print(driver_getFirstName(driver) + ' ' + driver_getLastName(driver)\
                  + ' ' + driver_getNumberOfTripsCompleted(driver))

    for queue in listof_availabilityQueues:
        if not availabilityQueue_isEmpty(queue):
            driver = availabilityQueue_front(queue)
            print(availabilityQueue_getLocationName(queue) + ' ' + driver_getFirstName(driver)\
                  + ' ' + driver_getLastName(driver))
       
    
    


#---------------------------------------------------------------
#                        Testing
#---------------------------------------------------------------

"""JohnDoe = driver_make("John", "Doe", "Toyota Corolla 2011", 0)
JaneDoe = driver_make("Jane", "Doe", "Toyota Corolla 2011", 0)
availabilityQueue_enqueue(availabilityQueue_UWI, "John Doe")
availabilityQueue_enqueue(availabilityQueue_Papine, "Jane Doe")

knownPassengers["8765708210"] = 2"""





