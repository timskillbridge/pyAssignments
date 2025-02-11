from __future__ import annotations

class ContactList:
    
    def __init__(self, contact_list=[]):
        self.contact_list = contact_list

    
    def add_contact(self,info={}):
        self.contact_list.append(info)
        print(self.contact_list)


    def remove_contact(self,name):
        to_remove = None
        for x in self.contact_list:
            if x.get('name') == name:
               to_remove = x
               print(to_remove)
        if to_remove:
            self.contact_list.remove(to_remove)
            print(self.contact_list)



friends = ContactList([{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}])
work_buddies = ContactList([{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}])

friends.add_contact({'name':'Jack','number':'457-7845'})

friends.remove_contact('Alice')



