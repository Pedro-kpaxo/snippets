import pathlib
import os

class Open_Service:
    
    ''' 
        This class is used to speed the opening and closing of .txt files
        using instance of with, to deal with the process.

        You can choose how you want to 'tag' your files.
        Tuples, Dict or none.
    '''
        
    
    def _Tuples(list_):
            
        ''' 
            This function the Tuple style Opening to a list.
            It takes a list, open the .TXT files, 
            and returns a tuple, with (filename,lines of the file)
         '''

        return Open_Service.List_Iter(list_,Open_Service.Open_style.Open_With_Tuple)


    def _TagDict(list_):
            
        ''' 
            This function the Tag(Dict) style Opening to a list.
            It takes a list, open the .TXT files, 
            and returns a Dict, with (filename,lines of the file)
         '''

        return Open_Service.List_Iter(list_,Open_Service.Open_style.Open_With_Tag)    

    
    def List_Iter(list_,func_):
        ''' 
        This function applies a function to a list.
            It retunrns a list with the opend files.
        '''
        op_list = []
        for x in list_:
            func_(x)
            op_list.append(func_(x))
        return op_list


    class Open_style:

        def Open(path):
            ''' 
            This functions simple open a .TXT file an returns a 
                list of string lines.           
            '''
            
            with open(path, encoding="ISO-8859-1") as f:
                lines = f.readlines()
            return lines

        def Open_With_Tuple(path):
            ''' 
            This function takes a TXT file PATH
                and returns a TUPLE whose X[0] = PATHNAME
                and X [1] a list of LINES strings that the file contains
            
            '''
            # Transformação para Pure Path
            sss = os.path.split(path)[1]
            
            #print(sss)
            AGP_Tuple_list = []
            #ssss = str.join(sss)
            # De Pure Path para String
            pathname = str(sss).upper()
            with open(path, encoding="ISO-8859-1") as f:
                lines = f.readlines()
            AGP_TUPLE = (pathname,lines)
            return AGP_TUPLE

        def Open_With_Tag(path):
            ''' 
            This function takes a PATH 
            and returns a list of strings that the file contains, in form of a
            DICT, the key is the filepath, purepath.
            '''
            # Transformação para Pure Path
            sss = os.path.split(path)[1]
            
            #print(sss)
            AGP_TAG = {}
            #ssss = str.join(sss)
            
            # De Pure Path para String
            pathname = str(sss).upper()
            with open(path, encoding="ISO-8859-1") as f:
                lines = f.readlines()
            AGP_TAG.setdefault(pathname,lines)
            return AGP_TAG