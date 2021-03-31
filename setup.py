import configparser
import time
config = configparser.ConfigParser()
print("Welcome to the Setup!")
print("\n")
print("First the program needs to know the order of your characters in the "
      "choose screen in Valorant! Go to this screen and setup the program!")
time.sleep(8)
print("\n")
print("Pay Attention! The order will change if your buy a new character! To "
      "change the order, simply run setup.py again!")
time.sleep(8)
print("\n")
print("These are the number. Every number stands for a character!")
print("1  = Astra")
print("2  = Breach")
print("3  = Brimstone")
print("4  = Cypher")
print("5  = Jett")
print("6  = Killjoy")
print("7  = Omen")
print("8  = Phoenix")
print("9  = Raze")
print("10 = Reyna")
print("11 = Sage")
print("12 = Skye")
print("13 = Sova")
print("14 = Viper")
print("15 = Yoru")
time.sleep(0.5)
time.sleep(1)


order1 = input("Who is your first character?[enter the number from above]")
order2 = input("Who is your second character?[enter the number from above]")
order3 = input("Who is your third character?[enter the number from above]")
order4 = input("Who is your fourth character?[enter the number from above]")
order5 = input("Who is your fifth character?[enter the number from above]")
order6 = input("Who is your sixth character?[enter the number from above]")
order7 = input("Who is your seventh character?[enter the number from above]")
order8 = input("Who is your eighth character?[enter the number from above]")
order9 = input("Who is your ninth character?[enter the number from above]")
order10 = input("Who is your tenth character?[enter the number from above]")
order11= input("Who is your eleventh character?[enter the number from above]")
order12 = input("Who is your twelfth character?[enter the number from above]")
order13 = input("Who is your thirteenth character?[enter the number from above]")
order14 = input("Who is your fourteenth character?[enter the number from above]")
order15 = input("Who is your fifteenth character?[enter the number from above]")

config['main'] = {      '1': order1,
                        '2': order2,
                        '3': order3,
                        '4': order4,
                        '5': order5,
                        '6': order6,
                        '7': order7,
                        '8': order8,
                        '9': order9,
                        '10': order10,
                        '11': order11,
                        '12': order12,
                        '13': order13,
                        '14': order14,
                        '15': order15
                 }

configfile = open('config.ini', 'w')
config.write(configfile)

exit()
