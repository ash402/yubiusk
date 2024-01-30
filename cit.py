import datetime as dt
import sys

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
        
    # Return missing requirements in human readable form (sequence of characters)
    # W - Waiver
    # D - Dues
    # A - Attendance
    # 6 - 6 Months
    @property
    def missing_HR(self):
        ret = ''
        #return f'{"W" if !self.waivered}{"D" if !self.dues_paid}{"A" if !self.attendance}{"6" if !self.six_months}'
        if not self.waivered: ret += 'W'
        if not self.dues_paid: ret += 'D'
        if not self.attendance: ret += 'A'
        if not self.six_months: ret += '6'
        return ret

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
    citizens = [p for p in players if p.state == 31]
    print(f'Number citizens: {len(citizens)}')
    waiver = [p for p in players if p.state == 28]
    print(f'Number need waiver: {len(waiver)}')
    dues = [p for p in players if p.state == 26 or p.state == 24]
    print(f'Number need dues: {len(dues)}')
    
    return (citizens, waiver, dues)
    
def new_players(players):
    # Citizens except for 6-months
    all_but_time = [p for p in players if p.state == 14]
    # Attendance, but not 6-months, and missing dues or waiver or both
    attendance = [p for p in players if p.state in (8, 10, 12)]
    return (all_but_time, attendance)

if __name__ == '__main__':
    finname = 'import.jsork'
    foutname = 'output.txt'
    verbose = False
    # Assume 1 arg = input name
    if (len(sys.argv) == 2):
        finname = sys.argv[1]
    #if (sys.argv[1][0] != '-'):
    #    finname = sys.argv[1]
    # Parse arguments
    if (len(sys.argv) > 2):
        narg = len(sys.argv)
        i = 1
        while(i + 1 < narg):
            carg = sys.argv[i]
            i += 1
            if(carg == '-o'): # output file name
                foutname = sys.argv[i]
                i += 1
            elif(carg == '-i'): # input file name
                finname = sys.argv[i]
                i += 1
            elif(carg == '-v'): # verbose output (print to screen)
                verbose = True
            
    # check file exists
    try:
        d = loadFile(finname)
    except FileNotFoundError:
        print(f'File <{finname}> could not be found. Check file name spelling and try again.')
        exit()
    if (d == -1):
        print(f'File <{finname}> was not properly formatted. Check the first row is the correct header and try again.')
        exit()
    
    if(verbose):
        print(d)
    
    # Interpret file text strings into object list
    players = loadPlayersFromFile(d)
    #[print(f'{p.persona}: {p.state}') for p in players]
    # Interpret list for citizens, citizens minus waiver, and citizens minus dues (and possibly waiver)
    data = main_parse(players)
    
    data2 = new_players(players)
    
    fout = open(foutname, 'w')
    fout.write(f'(A) Citizens ({len(data[0])}):\n')
    [fout.write(f'{p.persona}\n') for p in data[0]]
    fout.write('\n')
    
    fout.write(f'(B) Following <{len(data[2])}> players can become citizens immediately if they pay dues and sign waiver (they meet attendance and start date requirements:\n')
    [fout.write(f'{p.missing_HR}:\t{p.persona}\n') for p in data[2]]
    fout.write('\n')
    
    fout.write(f'(C) Following <{len(data2[0])}> players meet all requirements except 6-months-in-game, and will immediately become citizens 6 months after their listed start date:\n')
    [fout.write(f'{p.missing_HR}:\t{p.persona}\n') for p in data2[0]]
    fout.write('\n')
    
    fout.write(f'(D) Following <{len(data2[0])}> players meet attendance requirements but not 6-months-in-game; they may become citizens 6 months after their listed start date if they pay dues and/or sign waiver:\n')
    [fout.write(f'{p.missing_HR}:\t{p.persona}\n') for p in data2[1]]
    fout.write('\n')
    
    fout.close()