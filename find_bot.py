# Author: Luis Serrano
# Python verison: 3.0
import reg_funcs

file = open('log.log')

date_list = []
action_list = []
equal_dates = []
user_list = []
ip_address_list = []
first_row = True
i = 0
print('==========================================================================')
print('                           Bot Detection System')
print('                     Bots do multiple actions in 1 sec')
print('==========================================================================')
print("")
for line in file:
    text = str(line)

    # Load variables extracting the data with Regular Expressions
    date = reg_funcs.find_text(
        '[A-Z]\w+[,\/]\s\d\d\s[A-Z]\w+\s\d{4}\s\d\d[:\/]\d\d[:\/]\d\d', text)
    user = reg_funcs.find_text('[|[A-Z]\w+[|\/]', text)
    action = reg_funcs.find_text('\w*user\w*\s[a-z]\w+\s[a-z]\w+', text)
    # not used for now
    ip_address = reg_funcs.find_text('(\d+[.\/]\d+[.\/]\d+[.\/]\d+)', text)

    # Fill the arrays
    if first_row:
        date_list.append(date)
        action_list.append(action)
        user_list.append(user)
        first_row = False
    else:
        # Validate than the actions occurs in the same second
        if date_list[0] == date:
            date_list.append(date)
            action_list.append(action)
            user_list.append(user)
        else:
            date_list = [date]
            user_list = [user]
            action_list = [action]

    if(len(date_list)) >= 3:
        user_final = reg_funcs.equal_elements(user_list)
        final_actions = len(set(action_list))
        user_name = user_list[0].replace("|", "")
        if user_final[user] >= 3 and final_actions == 3:
            i = i + 1
            print('Bot detected {}: {} - Actions: {}'.format(i, user_name, action_list))
print("")
print("============================================================")
print('Actions: Login, Change Password, Log off, change Profile')
print("============================================================")
