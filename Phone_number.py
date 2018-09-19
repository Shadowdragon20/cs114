
print('what is your phone number? all digits')

def get_phone():
    phone=input()
#'phone'.split
    return phone

def check_length(phone):
    phone_len = len(phone)
    if phone_len == 7:
        has_area_code = False
    else:
        has_area_code = True
    return has_area_code

def build_output(phone, has_area_code):
    if has_area_code == True:
        area_code = phone[0:3]
        part_one = phone[3:6]
        part_two = phone[6:]
        print(phone[0:3],'-',phone[3:6],'-', phone[6:])
        print('(',phone[0:3],')', phone[3:6], '-', phone[6:])
    else:
        print(phone[0:3] + '-' + phone[3:])

def main():
    phone = get_phone()
    has_area_code = check_length(phone)
    # print(phone, has_area_code)
    build_output(phone, has_area_code)

main()
