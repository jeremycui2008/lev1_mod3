"""
Introduction to storing functions in variables
"""
import unittest


def surprise():
    return 'SURPRISE!'

func_1=surprise

# TODO 1) Change what is assigned into the func_1 variable so test_1 will pass


# TODO 2) Change the return statement below so that test_2 will pass
def pizza_surprise():
    return "SURPRISE, here's a pizza!"

# TODO 3) Implement the birthday_surprise function so that test_3 will pass
def birthday_surprise(years):
    ordinal="th"
    years_old = str(years)
    if years_old[-1]=='1':
        ordinal='st'
    elif years_old[-1]=='2':
        ordinal='nd'
    elif years_old[-1]=='3':
        ordinal='rd'
    return 'SURPRISE, Happy '  +str(years_old)+ordinal+  ' birthday!!!'

# TODO 4) Implement the surprise_guests function so that test_3 will pass
#  *HINT* You will have to add input parameters to the function
def surprise_guests(guests):
    people=str(guests)
    welcome=",here's a pizza!"
    partygoer=input('do you need pizza?')
    if partygoer=='pizza':
        return str(people) + 'says'+'SURPRISE!'+str(welcome)
    else:
        return str(people) + 'says'+'SURPRISE!'
    return None

# ================== DO NOT MODIFY THE CODE BELOW ============================

class WriteClassesTests(unittest.TestCase):

    def test_1(self):
        self.assertEqual('SURPRISE!', func_1())

    def test_2(self):
        func_2 = pizza_surprise
        self.assertEqual("SURPRISE, here's a pizza!", func_2())

    def test_3(self):
        func_3 = birthday_surprise
        self.assertEqual('SURPRISE, Happy 1st birthday!!!', func_3(1))
        self.assertEqual('SURPRISE, Happy 2nd birthday!!!', func_3(2))
        self.assertEqual('SURPRISE, Happy 3rd birthday!!!', func_3(3))
        self.assertEqual('SURPRISE, Happy 38th birthday!!!', func_3(38))

    def test_4(self):
        guests = ['Jerry', 'Summer', 'Yusef']
        expected_message =  guests[0] + ' says ' + 'SURPRISE!\n'
        expected_message += guests[1] + ' says ' + 'SURPRISE!\n'
        expected_message += guests[2] + ' says ' + 'SURPRISE!\n'
        self.assertEqual(expected_message, surprise_guests(surprise, guests))

        expected_message =  guests[0] + ' says ' + "SURPRISE, here's a pizza!\n"
        expected_message += guests[1] + ' says ' + "SURPRISE, here's a pizza!\n"
        expected_message += guests[2] + ' says ' + "SURPRISE, here's a pizza!\n"
        self.assertEqual(expected_message, surprise_guests(pizza_surprise, guests))

if __name__ == '__main__':
    unittest.main()
