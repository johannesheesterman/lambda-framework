import os
from typing import List
import abc

class ScriptEngine():

    __filename_by_methodname = {}

    def __init__(self, script_paths: List[str], fileExtension:str):
        self.__script_paths = script_paths
        self.__file_extension = fileExtension
        self.__load_scripts()
        

    def isMethodDefined(self, methodname:str) -> bool:
        return methodname in self.__filename_by_methodname

    def executeMethod(self, methodname:str, args: List[any]) -> any:
        return self.__execute_method__(self.__filename_by_methodname[methodname], methodname, args)

    def __load_scripts(self) -> None:
        for directory in self.__script_paths:
            for filename in [filename for filename in os.listdir(directory) if filename.endswith(self.__file_extension)]:
                fullPath = os.path.join(directory,filename)
                for method in self.__list_methods_in_file__(fullPath):
                    self.__filename_by_methodname[method] = fullPath

    @abc.abstractmethod
    def __list_methods_in_file__(self, filename:str) -> None:
        raise Exception("Abstract method __list_methods_in_file not implemented.")

    @abc.abstractmethod 
    def __execute_method__(self, filename:str, methodName:str, args: List[any]) -> any:
        raise Exception("Abstract method __list_methods_in_file not implemented.")
