from ATMExcept import DepositError,WithDrawError,InsufFundError
bal=500.0
def deposit():
    dmat=float(input("ENter your deposit amount: "))
    if(dmat<0):
        raise DepositError
    else:
        global bal
        bal=bal+dmat
        print("\tur accont XXXXXXXXXXXXXX123 credited with INR:{}".format(dmat))
        print("\tur account xxxxxxxxxx23 bal after deposit INR:{}".format(bal))
def withdraw():
    global bal
    wamt = float(input("ENter your withdraw amount: "))
    if (wamt < 0):
        raise WithDrawError
    elif((wamt+500)>bal):
        raise InsufFundError
    else:
        bal=bal+wamt
        print("\tur accont XXXXXXXXXXXXXX123 debited with INR:{}".format(wamt))
        print("\tur account xxxxxxxxxx23 bal after debited INR:{}".format(bal))
def bal_Enquery():
    print("\tUR account xxx123 bal INR:{}".format(bal))