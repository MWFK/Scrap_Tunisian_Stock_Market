class Month_Days:

    def __init__(self, Year, Month):
        self.Year   = Year
        self.Month  = Month

    def GetDays(self):

        leap = 0
        if self.Year % 400 == 0:
            leap = 1
        elif self.Year % 100 == 0:
            leap = 0
        elif self.Year % 4 == 0:
            leap = 1

        if self.Month == 2:
            return 28 + leap

        list = [1, 3, 5, 7, 8, 10, 12]
        if self.Month in list:
            return 31
        return 30

################################ Test
# MD = Month_Days(2021, 8)
# x = MD.GetDays()
