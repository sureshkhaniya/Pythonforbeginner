class CaloricBalance():

    def __init__(self, gender, age, height, weight):
        self.weight = weight
        self.balance = - self.getBMR(gender, age, height, weight)
        pass

    def getBMR(self, gender, age, height, weight):
        if gender == 'm':
            BMR = 66 + (12.7 * height)+(6.23 * weight) - (6.8 * age)
            return BMR
        elif gender == 'f':
            BMR = 655 + (4.7 * height)+(4.35 * weight) - (4.7 * age)
            return BMR
        else:
            return 0.0

    def getBalance(self):
        return self.balance

    def recordActivity(self, caloric_burn_per_pound_per_minute, minutes):
        calories_per_minute = caloric_burn_per_pound_per_minute * self.weight
        total_caloric_burn = calories_per_minute * minutes
        self.balance = self.balance - total_caloric_burn
        return self.balance

    def eatFood(self, calories):
        self.balance = self.balance + calories
        return self.balance