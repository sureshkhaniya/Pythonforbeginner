import sys

def milesPerGallon(miles, gallons):
    if gallons == 0:
        return 0.0
    else:
        return miles/gallons

def createNotebook():
    return []

def recordTrip(notebook, date, miles, gallons):
    return notebook.append({'date': date, 'miles': miles, 'gallons': gallons})

def listTrips(notebook):
    notebook2 = []
    for item in notebook:
        notebook2.append('\nOn '+ str(item['date'])+": "+str(item['miles'])+' miles traveled using '+ str(item['gallons'])+' gallons. '+ 'Gas milegae: '+str(milesPerGallon(item['miles'],item['gallons']))+' MPG\n')
    return notebook2

def calculateMPG(notebook):
    total_gallons = 0.0
    total_miles = 0.0
    if not notebook:
        return 0.0
    for item in notebook:
        total_miles = total_miles + item['miles']
        total_gallons = total_gallons + item['gallons']
    if total_gallons != 0.0:
        average_MPG = total_miles/total_gallons
        return average_MPG
    else:
        return 0.0

def formatMenu():
    return ['What would you like to do?', '[r] Record Gas Consumption', '[l] List Mileage History', '[c] Calculate Gas Mileage', '[q] Quit']

def formatMenuPrompt():
    return 'Enter an option: '

def getUserString(prompt):
    while True:
        user_input = input(prompt)
        user_input = user_input.strip()
        if user_input:
            return user_input
        else:
            continue

def getUserFloat(prompt):
    user_input = input(prompt)
    while True:
        try:
            user_input = float(user_input)
            if user_input <= 0:
                user_input = input('Please enter a number greater than zero.')
                continue
            else:
                return user_input
        except ValueError:
            user_input = input('Please enter a number.')
            continue

def getDate():
    return getUserString('What is the date? ')

def getMiles():
    return getUserFloat('How many miles did you drive since last filling up?')

def getGallons():
    return getUserFloat('How many gallons of gas did you add to your tank?')

def recordTripAction(notebook):
    recordTrip(notebook, getDate(), getMiles(), getGallons())
    print('\nSaved!\n')

def listTripsAction(notebook):
    trip_list = listTrips(notebook)
    if trip_list:
        for trip in trip_list:
            print(trip)
    else:
        print('\nYou first need to record your gas consumption!\n')

def calculateMPGAction(notebook):
    MPG = calculateMPG(notebook)
    if MPG == 0.0:
        print('\nThere is no trip data.\n')
    else:
        print('Average gas mileage: '+str(MPG)+' MPG')

def quitAction(notebook):
    print('Good bye, See you next time!')
    sys.exit(0)

def applyAction(notebook, choice):
    if choice == 'r':
        return recordTripAction(notebook)
    elif choice == 'l':
        return listTripsAction(notebook)
    elif choice == 'c':
        return calculateMPGAction(notebook)
    elif choice == 'q':
        return quitAction(notebook)
    else:
        print('Sorry, that option is invalid')

def main():
    notebook = createNotebook()
    while True:
        for item in formatMenu():
            print(item)
        user_choice = getUserString(formatMenuPrompt())
        applyAction(notebook, user_choice)

        continue

#if __name__ == '__main__':
   # main()