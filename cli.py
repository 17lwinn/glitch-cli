import cmd

class GlitchCli(cmd.Cmd):
    """Simple command processor example."""
    
    def do_greet(self, line):
        print ("hello user, hope you have a good day using our service")
    
    def do_exit(self, line):
        return True

    def help_greet(self):
         print ([ "greet",
                  "Greet the named person",
                           ])
if __name__ == ("__main__"):
    GlitchCli().cmdloop()