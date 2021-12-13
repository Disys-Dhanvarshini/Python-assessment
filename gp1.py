import googlepay
varsha = googlepay.google_pay("kdvarshini@gmail.com","8076545334","Dhanvarshini")
varsha.emailverify()
varsha.mobileverify()
varsha.usernameverify()
varsha.otpverify(4535,4535)
varsha.bankverify()
varsha.pancardverify()
varsha.pinverify("6789")
varsha.enterpin(6787,6787)
class phonepay(googlepay.google_pay):
    def __init__(self,e,ph,u):
        super().__init__(e,ph,u)
varshini = phonepay("kdvarshinik@gmail.com","8076985334","varshini")
varshini.emailverify()
varshini.mobileverify()
varshini.usernameverify()
varshini.otpverify(4735,4735)
varshini.bankverify()
varshini.pancardverify()
varshini.pinverify("678867")
varshini.enterpin(6447,6447)
gp = [{"name":"varsha", "number":"7658569842","type":"personal","transaction":"regular"},
      {"name":"abinaya", "number":"7689546920","type":"personal","transaction":"regular"},
      {"name":"latha", "number":"8743092467","type":"personal","transaction":"regular"},
      {"name":"abishek", "number":"9685287429","type":"personal","transaction":"rare"},
      {"name":"navin", "number":"9734090045","type":"personal","transaction":"regular"},
      {"name":"nivi", "number":"6745092810","type":"personal","transaction":"rare"},
      {"name":"gokul", "number":"6704185390","type":"personal","transaction":"rare"},
      {"name":"parvathi", "number":"9846073690","type":"personal","transaction":"regular"},
      {"name":"elango", "number":"8704389064","type":"personal","transaction":"regular"},
      {"name":"malathi", "number":"9359705682","type":"personal","transaction":"regular"},
      {"name":"kandasamy", "number":"9308305091","type":"personal","transaction":"regular"},
      {"name":"santhosh", "number":"9964366026","type":"personal","transaction":"rare"},
      {"name":"vijay", "number":"67839260953","type":"personal","transaction":"regular"},
      {"name":"ajith", "number":"9358042701","type":"personal","transaction":"regular"},
      {"name":"rajini", "number":"5792450815","type":"personal","transaction":"rare"},
      {"name":"kamal", "number":"8357035178","type":"personal","transaction":"regular"},
      {"name":"sivakarthikeyan", "number":"8417802717","type":"personal","transaction":"regular"},
      {"name":"vanitha", "number":"9427829520","type":"personal","transaction":"regular"},
      {"name":"sathya", "number":"9536829105","type":"personal","transaction":"regular"},
      {"name":"ramachandran", "number":"68709146287","type":"personal","transaction":"regular"},
      {"name":"krishna", "number":"6904579275","type":"personal","transaction":"regular"},
      {"name":"saravana", "number":"6795340956","type":"personal","transaction":"rare"},
      {"name":"sriram", "number":"9735790256","type":"personal","transaction":"regular"},
      {"name":"sriman", "number":"8649095656","type":"personal","transaction":"rare"},
      {"name":"indhu", "number":"8538943467","type":"personal","transaction":"rare"},
      {"name":"dinesh", "number":"6429527953","type":"personal","transaction":"rare"},
      {"name":"ashik", "number":"890321678","type":"personal","transaction":"regular"},
      {"name":"manoranjini", "number":"9444120188","type":"personal","transaction":"regular"},
      {"name":"yashika", "number":"9845679905","type":"personal","transaction":"regular"},
      {"name":"venkat", "number":"8945679844","type":"personal","transaction":"regular"},
      {"name":"meghana", "number":"7276349845","type":"personal","transaction":"regular"},
      {"name":"vishnu", "number":"7650566788","type":"personal","transaction":"rare"},
      {"name":"janani", "number":"9056784322","type":"personal","transaction":"regular"},
      {"name":"kowshik", "number":"7276347790","type":"personal","transaction":"rare"},
      {"name":"akhil", "number":"7889946790","type":"personal","transaction":"regular"},
      {"name":"adhithya", "number":"7642886588","type":"personal","transaction":"rare"},
      {"name":"aniruth", "number":"76585005478","type":"personal","transaction":"rare"}]

for i in gp:
    for j,k in i.items():
        print(f"{j}:{k}")
      
