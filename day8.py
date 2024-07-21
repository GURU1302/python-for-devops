##LISTS AND TUPLES

def main():
    list1 = ["guru","sneha","saurabh","anushka"]
    list1.append("maa")
    new_list = list1[1:3] #for slicing the list
    print(new_list)
    new_list.sort()
    print(new_list)

    # print(list1) # to print the complete list
    # print(len(list1)) #to calculate the length
    # list1.remove("guru") #to remove any element
    # print(list1[1]) #to print oe access any element
    # list1.remove(list1[3]) # to remove any element by its index
    # print(type(list1))


main()

#tuple is an immutable list cannot be resized
#tuples has better memory footprints cause they are immutable
#tuples are written in ("   ", "   ", " ")

# def func():
#     tuple1 = ("guru",  "sneha")
#     print(type(tuple1))
#     print(len(tuple1))
#     print(tuple1[1])


# func()



#in list we can add value of different data types

