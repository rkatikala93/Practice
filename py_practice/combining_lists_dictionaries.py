""" menus = {'Breakfast': ['Egg Sandwich', 'Bagel', 'Coffee'],
         'Lunch': ['Bread', 'butter', 'Milk'],
         'Dinner': ['Roll', 'cream', 'butter']
         }
menus.update({'Snacks': ['Ice Cream', 'custard', 'pizza']})
print(menus.fromkeys('Breakfast'))
for item, menu in menus.items():
    print(menu[0]) """

# Nested Dictionaries

contacts = {
    "numbers": 4,
    "students":
    [
        {"name": "Sarah Holderness", "email": "sarah@gmail.com"},
        {"name": "Harry Potter", "email": "harry@gmail.com"},
        {"name": "Ganger", "email": "ganger@gmail,com"},
        {"name": "Ron", "email": "ron@gmail.com"}
    ]
}

for key, value in contacts.items():
    print("\n keys", key)
    for info in value:
        print(info + ':',  value[info])

# print(contacts.keys())
