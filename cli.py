import cmd
import os
from time import *


class GlitchCli(cmd.Cmd):
  
    prompt = "GlitchCLI: "
    
    def do_greet(self, line):
        print ("hello user, hope you have a good day using our service")
    
    def do_node(self, line):
        print("are you sure you want to make your project a node app? Y or N")
        node = input("choice: ")
        
        if node == "Y":
          print("I REALLY hope you know what your doing")
          print("prepare for hyperspace... NODIFY!")
          sleep(2)
          os.system("curl https://nodify.glitch.me|bash")
          
    
    def do_exit(self, line):
        return True
# -----------------------------------------------------------------------
#                              help
# -----------------------------------------------------------------------
    def help_greet(self):
         print ( "greet: ", "Greet the current user")
      
    def help_exit(self):
         print ( "exit: ", "exit the CLI")   
    def help_exit(self):
         print ( "exit: ", "exit the CLI")
        
        
        
if __name__ == ("__main__"):
    GlitchCli().cmdloop()