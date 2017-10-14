'''Dictionary = is when you have values and keys of data stored
in a single object
'''
# 1 way to create a dictionary
post={"user_id":207, "message":"DE DA DI", "language":"English",
      "data_time":"3/13/2017", "location":(44.78, -108.7)}
post[0]
dir(post)
type(post)

# 2nd way to create a dictionary
post2 = dict(message="Glenda", lenguage="English")
print(post2)

# Adding new data to the post2 dictionary
post2["user_id"] = 20
post2["user_name"] = "Glenda"
post2["user_lastname"] = "Ascencio"

# Accessing data in a dictionary
post2['message']
post2['user_name']
post2["user_lastname"]

# Returning an error for someone who enters a value not defined
    # One way
if 'location' in post2:
    print post2['location']
else:
    print "The post doesn't contain a location value"
    # Second way
try:
    print post2['location']
except KeyError:
    print "The post don't contain a location value"
