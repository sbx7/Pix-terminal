import os
print("Pix terminal V1 by tucker sur. Type help for commands")

#cmd line
while True:
    #input
    cl = input(os.getcwd())
    spliting=cl.split()
    
    #checks what cmd you typed and gives a response (will optimize soon maybe)
    if cl == "ls":
        for file in os.listdir():
            print(file)
    
    elif cl == "shutdown":
        print("Closing pix terminal")
        exit()
    
    elif spliting[0] == "cd":
        if spliting[1] == "..":
            os.chdir('../')
        else:
            path = spliting[1]
            os.chdir(path)
    
    elif cl == "help":
        print("COMMANDS (tip. AC stands for alter code and they change how the script works)")
        print("ls, lists all files and directories in the active dir")
        print("cd {AC} {dest}, AC=.. goes back a dir")
        print("file [AC] [file] [new name if renaming],(theres alot here) with a AC of d you can delete a file of dir. AC of n makes a file and a AC of v reads the file and a AC of r renames the file")
        print("dir [dir name], makes a new dir")
        print("run [filename] [AC]. this starts a program. having AC as k keeps pix terminal open")
        print("shutdown, stops pix terminal")
    
    elif spliting[0] == "dir":
        os.mkdir(spliting[1])

    # TO:DO find out how the fuck i can run this on a raspberry pi pico        
    elif spliting[0] == "file":
        if spliting[1] == "n":
            file = open(spliting[2], 'w')
            file.close
        elif spliting[1] == "d":
            try:
                os.remove(spliting[2])
            except FileNotFoundError:
                print("ERROR: file was not found. prob dont exsist")
        elif spliting[1] == "e":
            edit = input("replace with")
            file = open(spliting[2], "w")
            file.write(edit)
            file.close()
    
        elif spliting[1] == "v":
            with open(spliting[2]) as file:
                print(file.read())
                
        elif spliting[1] == "r":
            os.rename(spliting[2], spliting[3])
            '''
            #dont work on a pico
            except IsADirectoryError:
                print("Source is a file but destination is a directory.")
  
            except NotADirectoryError:
                print("Source is a directory but destination is a file.")

            except PermissionError:
                print("Operation not permitted.")

            except OSError as error:
                #print(error)
            '''
     
    elif spliting[0] == "say":
        print(spliting[1])
    
    elif spliting[0] == "poxEXE":
        print("comming soon: execute pox scripts")
    else:
        print("ERROR: invalid syntax")