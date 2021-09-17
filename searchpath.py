import pathlib

'''
Created to fast searchs and querys up!.
'''

class Search_Path:
    '''
    Created to fast searchs and querys up!.
    Use Search_exten to find extensions, or
    Search_files to search for names in filepath.
    '''
    def Search_Exten(folder_path,extension,):
        ''' 
        This function takes a path to a FOLDER and a extendion,
            then it loops into all paths in the folder in search
            of the extenxion.

        It returns a list with the paths.
        '''
        extension:str
        extensions = extension
        filelist=[]
        print(extensions)
        for path in folder_path.glob(r'**/*'):
            if path.suffix in extensions:
                filelist.append(path)
        else:
            pass
            
        return filelist

    def Search_Files(folder_path,name_):
        ''' 
        This function takes a path to a FOLDER and a NAME,
            then it loops into all paths in the folder in search
            of the NAME.

        It returns a list with the paths.
        '''
        name_:str.lower()
        name_:str.format()
        name_list = [name_]

        filelist_name=[]
        
        for path in folder_path.glob(r'**/*'):

            # Transformação para Pure Path
            sss = pathlib.PurePath(path)

            # De Pure Path para String
            pathname = str(sss).lower()
            
            # Check for Multipe arg
            if len(name_list) > 1:
                for name in name_list:
                    if name in pathname:
                        filelist_name.append(path)

            else:
                if name_ in pathname:
                    filelist_name.append(path)

        return filelist_name