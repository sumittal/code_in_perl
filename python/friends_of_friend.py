"""
1. Friend of friends
 
Implement a method in a Person class below to return their friends of friends (or 2nd-degree network - in LinkedIn terminology).   
 
Example: B is A's friend. C is B's friend. Therefore C is A's friend of friends. 
(A) --> B --> C
"""
class Person():

    def __init__(self, name, friends=None):
        self.name = name
        if friends is None:
            friends = []
        self.friends = friends

    def friendsOfFriends(self):

        pair_counts = len(self.friends)

        if pair_counts <= 1:
            return -1

        friends_list = {}
        for pair in self.friends:

            if type(pair) is not tuple:
                continue

            k, v = pair
            friends_list.setdefault(k,[]).append(v)


        sorted_keys = sorted(friends_list.items())

        friends_of_friend = {}
        for key in sorted_keys:
            k, v = key

            if len(v) > 0:
                for member in friends_list[k]:
                    if friends_list.get(member) is not None:
                        if  k in friends_list[member]:
                            continue
                        friends_of_friend[k] =  friends_list[member]
        
        if not friends_of_friend:
            return -1
        
        # for friend in (sorted(friends_of_friend)):
        #     print(friend, ' => ', friends_of_friend[friend])

        return friends_of_friend[self.name]
        

l1 = [('A','B'),('B','C'),('B','D'),('C','E'),('D','E'),('E','F'),('F','A'),('E','B')]
l2 = [('A','B'),('B','A')]
l3 = [('A','B'),('B','C'),('B','D')]
l4 = [('A','B')]
l5 = [('A','A')]

groups = [l1, l2, l3, l4, l5]

for frnds in groups:
    person = 'A'
    f = Person(person, frnds)
    result = f.friendsOfFriends()
    print("List of friends: ", frnds)
    if result != -1:
        print("2nd degree friend of " + person + " are : ", result)
    else:
        print('No 2nd degree friends of ' + person)
    print("\n")


