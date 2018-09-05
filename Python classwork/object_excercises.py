#1- 
class Person: 
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name)) 

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@hotmail.com', '495-586-3956')
sonny.greet(jordan)
print(sonny.email, sonny.phone)
print(jordan.email, jordan.phone)

#2-
class Person: 
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.uniq_ppl = []


    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        if other_person not in self.uniq_ppl:
            self.uniq_ppl.append(other_person)

    def print_contact_info(self):
        print self.name + "\'s email: " + self.email + ", " + self.name + "\'s phone number: " + self.phone

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        return len(self.friends)
    
    def greeting_count(self):
        return self.greeting_count
        
    def __str__(self):
        return 'Who are you: {}, Can I have your number?: {}, Just send me an email man!: {}'.format(self.name, self.email, self.phone) 

    def num_unique_people_greeted(self):
        return len(self.uniq_ppl)

#test data
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@hotmail.com', '495-586-3956')
sonny.greet(jordan)
print(sonny.email, sonny.phone)
print(jordan.email, jordan.phone)
sonny.print_contact_info()
sonny.add_friend(jordan)
print sonny.num_friends()

print sonny.greeting_count
sonny.greet(jordan)
print sonny.greeting_count

sonny.greet(jordan)
print sonny.greeting_count

print (jordan)

sam = Person('sam', 'sam@gmail.com', '999-888-7777')
print sonny.num_unique_people_greeted()
sonny.greet(sam)
print sonny.num_unique_people_greeted()


