from os import listdir, path
from rich import print
from loguru import logger
from config import *

if not DEBUG:
    logger.disable(__name__)

class FTREE:
    def __init__(self) -> None:
        pass
    
    @logger.catch
    def fileName(self, file) -> str:
        """"""
        file = file.split(".")
        file = file[len(file)-1]
        return file
    
    @logger.catch
    def color_file(self, file) -> str:
        """"""
        if self.fileName(file) == "txt":
            logger.debug(PREFIX,file)                 
            return f"[bold]{PREFIX}{file}[/bold]"       
        elif self.fileName(file) == "py":
            logger.debug(PREFIX,file)
            return f"[bold yellow]{PREFIX}{file}[/bold yellow]"       
        elif path.isdir(file):
            logger.debug(PREFIX,file)
            return f"[bold darkgrey]{PREFIX}{file}[/bold darkgrey]"        
        else:
            logger.debug(PREFIX,file)
            return f"{PREFIX}{file}"
        
    @logger.catch    
    def func(self, _path):
        """"""
        if _path =="":
            files = listdir()
        else:       
            files = listdir(_path)

        for file in files:
            global LEVEL 

            print(self.color_file(file))
                
            if path.isdir(file):
                LEVEL+=1
                if _path != "":
                    self.func(_path+"/"+file)
                else:
                    self.func(file)
                LEVEL-=1


