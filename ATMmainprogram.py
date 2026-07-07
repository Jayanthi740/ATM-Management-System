from ATMExcept import DepositError,WithDrawError,InsufFundError
from ATMoperation import deposit,withdraw,bal_Enquery
from ATMmenu import menu
while(True):
    try:
        #menu()
        print("_"*50)
        ch=int(input("ENter your choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("\tdont enter -ve and zero values --try again")
                except ValueError():
                    print("\tDOnt enter the str,symbols,alnums")
            case 2:
                try:
                    withdraw()
                except WithDrawError:
                    print("\tdont try to withdraw -ve and zero values--try again")
                except InsufFundError:
                    print("\tAccout xxxx123 does not have funds---check balance")
                except ValueError:
                    print("\tDOnt enter the str,symbols,alnums")
            case 3:
                bal_Enquery()
            case 4:
                print("\tThanx for for using this project")
                break
            case _:
                print("\tur selction of choice is wrong try again")
    except ValueError:
        print("\tDOnt enter the str,symbols,alnums")