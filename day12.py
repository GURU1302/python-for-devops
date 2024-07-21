#file operations
#when we need to insert or update or delete a file using python then we use file operations
# import os
# #read operation
# with open("/opt","r"):
    
# #write /update operation on the file
# with open("/opt","w"):




# update the server.config file when the "macimum_connections" from 200 to 500
def update_config(file_path,key,value):
    with open(file_path,"r") as file:
        lines = file.readlines() #to read all lines of the file

    with open(file_path,"w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n") #to write when the condition is matched pura 
                #line hi change kr diya re yeh log aur next line agla line se start hai toh isne 
                # \n use kr liya last mein taaki dikkat na ho jaaye
            else:
                file.write(line)

update_config("server.config","MAX_CONNECTIONS",500)