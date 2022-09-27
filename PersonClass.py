class Person:
    def __init__(self,name,address,telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

        def get_name(self):
            return self.__name
        
        def get_address(self):
            return self.__address

        def get_telephone(self):
            return self.__telephone
        
        def print_person(self):
            print('Name:', self.__name)
            print('Address:', self.__address)
            print('Telephone:', self.__telephone)

class Customer(Person):

    def __init__(self,name,address,telephone,custNumber, mail):

        Person.__init__(self,name,address,telephone)

        self.__custNumber = custNumber
        self.__mail = mail


    def get_custNumber(self):
        return self.__custNumber

    def get_mail(self):
        return self.__mail

  
        print('Customer Number:', self.__custNumber)
        print('On the mailing list:', self.__mail)