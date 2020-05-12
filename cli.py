import cmd

class GlitchCli(cmd.Cmd):
  
    prompt = "GlitchCLI: "
    
    def do_greet(self, line):
        print ("hello user, hope you have a good day using our service")
    
    def do_exit(self, line):
        return True
# -----------------------------------------------------------------------
#                              help
# -----------------------------------------------------------------------
    def help_greet(self):
         print ([ "greet",
                  "Greet the current user",
                        )
        
        
        
if __name__ == ("__main__"):
    GlitchCli().cmdloop()