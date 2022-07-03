'''
Earlier code had a bug with the days, unfortunately could only accept 12 and under as an acceptable day.
Fixed some elements in the program; still fails 2 checks, but it works better than intended now.
There no longer needs to be a comma after the day (if that format is used), and the month no longer
has to be a number if in mm/dd/yyyy format.
Some simplification wouldn't hurt, but I'm currently satisfied with the program for now.
'''
months = {
    "January":'01',
    "February":'02',
    "March":'03',
    "April":'04',
    "May":'05',
    "June":'06',
    "July":'07',
    "August":'08',
    "September":'09',
    "October":'10',
    "November":'11',
    "December":'12'
    }
int_list = "0123456789"
vals = months.values()

def main():
    while True:
        date = input("Date: ")
        try:
            month,day,year = date.split("/")
        except ValueError:
            try:
                month,day,year = date.split(" ")
            except:
                pass
        if get_month(month) != False and get_day(day) != False and len(get_year(year)) == 4:
            print(f"{year.strip()}-{get_month(month)}-{get_day(day)}")
            break


def get_month(inp):
    if inp.title() in months:
        return months[inp.title()]
    for each in vals:
        if int(inp) == int(each):
            return each
    return False



def get_day(inp):
    string = ""
    for char in inp:
        if char in int_list:
            string += char
    try:
        if int(string) < 10:
            return f"0{string}"
        elif int(string) <= 31:
            return string
        else:
            return False
    except ValueError:
        return False

def get_year(inp):
    string = ""
    for char in inp:
        if char in int_list:
            string += char
    return string

main()