import datetime as dt

header_line = 'Persona\tCan Vote\tSigned Waiver\tDues Paid\tDays of Attendance\tSix Months Played\tFirst Attendance\n'
citizen_attendances = 7

class Player:
    def __init__(self, jline):
        items = [item.strip() for item in jline.split('\t')]
        if len(items) == 7:
            self.persona = items[0]
            self.citizen = items[1] == 'true'
            self.waivered = items[2] == 'true'
            self.dues_paid = items[3] == 'true'
            self.attendances = int(items[4])
            self.six_months = items[5] == 'true'
            self.first_attendance = dt.date.fromisoformat(items[6])
        else:
            return -1
            # Error
            #TODO probably throw exception
    
    @property
    def attendance(self):
        return self.attendances >= 7
    
    # 4 Conditionals to define citizenship
    @property
    def conditions(self):
        return [self.waivered, self.dues_paid, self.attendance, self.six_months]
    
    # 1 - Citizen
    # 2 - Waiver
    # 3 - Dues
    # 4 - Attendance
    # 5 - Six Months
    #
    # Represent the sum of the 5 conditionals as an integer
    # Functionally the same as encoding each as a binary bit
    @property
    def state(self):
        return sum([(2**i)*b for i,b in enumerate([self.citizen] + self.conditions)])

def loadFile(fname):
    with open(fname, 'r') as fid:
        data = fid.readlines()
    
        
    if data[0] != (header_line):
        print(header_line)
        print(data[0])
        return -1
    else:
        return data[1:]
        
def loadPlayersFromFile(data):
    return [Player(line) for line in data]

def main_parse(players):
    citizens = [p for p in players if p.state is 31]
    print(f'Number citizens: {len(citizens)}')
    waiver = [p for p in players if p.state is 28]
    print(f'Number need waiver: {len(waiver)}')
    dues = [p for p in players if p.state is 26 or p.state is 24]
    print(f'Number need dues: {len(dues)}')
    
    return (citizens, waiver, dues)

if __name__ == '__main__':
    d = loadFile('12.19.23-report.txt')
    print(d)
    if d == -1:
        exit
    
    players = loadPlayersFromFile(d)
    [print(f'{p.persona}: {p.state}') for p in players]
    
    data = main_parse(players)
    
    print(f'Following <{len(data[2])}> will be citizens if they pay dues and sign waiver:')
    [print(f'{p.persona}: {p.state}') for p in data[2]]