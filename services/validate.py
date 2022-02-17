from string import punctuation
import re

class Validate():
    def ValidateText(self,args):
        for val in args:
            msg = False if val in punctuation else True
        return msg
    
    def ValidateEmail(self,args):
        injection = ['insert','select','delete','find']
        for val in args.lower().split():
            if val in injection and  val[0] :
                return False
            else:
                return True
        
    def ValidatePassword(self,args):
        # outcome = re.findall(r'[\d\S]',f'{args}')
        # return True if outcome[0] == None else False
        return True
       
        
validate = Validate();
# msg = "insert oorimark@gmail.com"
# print(validate.ValidateEmail(msg))

# print(msg.split())

# print(validate.ValidatePassword("markoori"))
print("Running validate module")


