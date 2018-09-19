


# print('Enter a case number and a name of a client')
#
# client=input('Name of client')
# num= int(input('client number'))

def enter_client(client_dict):
    print('Enter a case number and a name of a client')

    client=input('Name of client ')
    num= int(input('Client Number '))
    client_dict.update({client: num})

    return client_dict


def return_client(client_dict):

    print(' Enter a client(s) name')
    client = client_dict['name']









    return client_dict


def main():
    print("Welcome to case number entry program woo hoo")
    client_dict={}
    status = "yes"
    print("Would you like to enter a new client? Yes to enter no to quit")
    while status != "no":


        enter_client(client_dict)
        print('would you like to enter another? or type no to quit.')
        status = input()
    print(client_dict)


    return_client(client_dict)

    print (client_dict)








main()
