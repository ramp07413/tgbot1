premium_user = []
free_user = []

all = []

def add_in_premium(name):
    premium_user.append(name)


def add_in_user(name):
    free_user.append(name)


add_in_premium("ram")
add_in_premium("rahul")
add_in_user("vipin")
add_in_user("king")
add_in_user("bhim")
add_in_premium("annoying")
add_in_user("daddy")
add_in_premium("me")

all.extend(premium_user)
all.extend(free_user)

print(all)