# ##Advanced list and Exceptional Handling

# # question: print all files from the list of folders

# # algo 
# # step1- read input from the user
# # step2- for loop, folder-list files
# # step3- identify module
# # step 4- to prrint each and every file
# # step 5 - identify and handle all the errors
# import os
# folders = input("please provide folder name with space in between").split()

# for folder in folders:
# #if user give a wrong file name and a write file name then
# #that should be handled wisely and should be user friendly
# #for that we use error handling
#    try:
#     files =  os.listdir(folder)
#    except FileNotFoundError:
#     print("please provide a valid folder name, no folder name exist with name - " + folder)
#     break
#    except PermissionError:
#     print("no access to folder - " + folder)

#    print("Listing all files of folder -  " + folder)
#    for file in files:
#       print(file)

import os

def list_files_in_folder(folder):
   try:
      files = os.listdir(folder)
      return files,None
   except FileNotFoundError:
      return None , "Folder not found" + folder
   except PermissionError:
      return None, "Access denied for folder" + folder



def main():
    folders = input("Enter the names of folders seperated by spaces: ").split()

    for folder in folders:
         files,error_message = list_files_in_folder(folder)
         if files:
            print(f"files in {folder}:")
            for file in files:
                print(file)
         else:
            print(f"Error in {folder}: {error_message}")


if __name__ == "__main__":
   main()