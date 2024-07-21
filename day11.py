# #DICTIONARY AND SETS

# #why we need dictionary?

# # you need to store property using key value pairs for which we need dictionary 


# # declaration of dictionary
# #list of dictionary

# # student_info = [{
# #     "name":"abhi",
# #     "age":11,
# #     "class":5,
# # },{
# #     "name":"guru",
# #     "age":12,
# #     "class": 4
# # },{
# #     "name":"sneha",
# #     "age":23,
# #     "class": 12
# # }]

# # print(student_info[2]["age"])


# #REAL TIME PROBLEM

# # get pull request information ona repo usung python

# # algo:

# # identify module which is request Module
# # find the api to get access to pull request to github repo can find in github documentation
# #must perform conversion from json to dictionary
# #print


# import requests

# # URL to fetch pull requests from the GitHub API
# url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'

# #get the whole respponse of the api it is in form of object
# response = requests.get(url)

# # print(response.json())

# #to fetch details

# complete_details = response.json()

# print(complete_details[0]["id"])


# #for printing the name of the users
# for i in range(len(complete_details)):
#     print(complete_details[i]["user"]["login"])


##SET

#have unique elements

set1 = {"abhi","abhi","ram"}

print(set1)



