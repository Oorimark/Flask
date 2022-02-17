# the robot is designed to handle anything involving automations folder

# robo-1
# this guy helps me check if a file is empty so i don't face problem when uploading to github
def robo_1(arg):
        import os;
        
        for (path, dir, files) in os.walk(os.getcwd() + arg):
            for file in files:
                if os.path.isfile(file):
                    if open(file,'r').read() == "":
                        print(file)
                else: continue
                    
# calling robo-1 to action, just feed it the path
robo_1()