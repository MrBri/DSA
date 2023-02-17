class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

user2 = "user2"
parent.add_user(user2)

for p in parent.get_groups():
    print('parent groups:', p.get_name())
for c in child.get_groups():
    print('child groups:', c.get_name())

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    else:
        for g in group.get_groups():
            return is_user_in_group(user, g)
    return False

print("sub_child_user in sub_child:", is_user_in_group("sub_child_user", sub_child))
print("sub_child_user in child:", is_user_in_group("sub_child_user", child))
print("sub_child_user in parent:", is_user_in_group("sub_child_user", parent))

print("user2 in sub_child:", is_user_in_group("sub_child_user", sub_child))
print("user2 in child:", is_user_in_group("sub_child_user", child))
print("user2 in parent:", is_user_in_group("sub_child_user", parent))

user3, user4, user5 = 'user3', 'user4', 'user5'

parent2, parent3, child2, child3 = Group('parent2'), Group('parent3'), Group('child2'), Group('child3')
parent2.add_group(child2)
child2.add_user(user3)
child2.add_user('')

parent3.add_group(child3)
parent3.add_user(user5)

print("user3 in child2:", is_user_in_group("user3", child2))
print("user3 in parent2:", is_user_in_group("user3", parent2))

print("user4 in child2:", is_user_in_group("user4", child2))
print("user4 in parent2:", is_user_in_group("user4", parent2))

print("user5 in child3:", is_user_in_group("user5", child3))
print("user5 in parent3:", is_user_in_group("user5", parent3))
