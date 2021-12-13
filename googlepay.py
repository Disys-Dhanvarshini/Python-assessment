class google_pay:
    def __init__(self,e,ph,u):
       self.username = u
       self.email = e
       self.phonenumber = ph
    def emailverify(self):
        if type(self.email)== str:
            if len(self.email)<=30:
                print("your email is verified")
            else:
                raise ValueError("invalid email id, please enter the correct email id")
        else:
                raise TypeError("invalid email id, please enter the correct email id")
    def mobileverify(self):
        if len(self.phonenumber)==10:
            if type(self.phonenumber)==str:
                print("your mobile number is verified")
            else:
                raise ValueError("Invalid Phone Number")
        else:
                raise TypeError("Invalid phone number")
    def usernameverify(self):
        if type(self.username)== str:
            if len(self.username)<=25:
                print("your username is verified")
            else:
                raise TypeError("please enter a valid username")
        else:
                raise ValueError("please enter a valid username")
    def otpverify(self,code,otp):
        if(otp == code):
            print("otp verified")
        else:
            raise ValueError("incorrect otp")
    def bankverify(self):
        self.acc = []
        self.accno = 57687898972628
        self.acc.append(self.accno)
        print(self.acc)
        print("Bank account verified")
    def pancardverify(self):
        self.panno = "HIA4676871"
        if(len(self.panno)== 10):
            print("pan verified")
        else:
            raise ValueError("Invalid pan number")
    def pinverify(self,no):
        self.pinno = no
        if(len(self.pinno)==4 or len(self.pinno)==6):
            print("successfully created")
        else:
            raise ValueError("Invalid pin")
    def enterpin(self,m,p):
        self.match = m
        self.pin = p
        if self.match == self.pin:
            print("done")
        else:
            raise ValueError("not matching")
        
        

                      
            
    
