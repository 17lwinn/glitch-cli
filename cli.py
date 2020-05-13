#! /usr/bin/env bash

import cmd
import zipfile
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
          
        if node == "N":
          print("okay, I totally understand")
          
    def do_pack(self, line):
      print("packing your very nice parcel...")
      zip_file = zipfile.ZipFile('app.zip', 'w')
      zip_file.write("*", compress_type=zipfile.ZIP_DEFLATED)
      zip_file.close()
      sleep(2)
      
    def do_exit(self, line):
        return True
# -----------------------------------------------------------------------
#                              help
# -----------------------------------------------------------------------
    def help_greet(self):
         print ( "greet: ", "Greet the current user")
      
    def help_exit(self):
         print ( "exit: ", "exit the CLI")   
        
    def help_node(self):
         print ( "node: ", "wraps your app in an express server, node in other words")
        
        
        
        
if __name__ == ("__main__"):
    GlitchCli().cmdloop()