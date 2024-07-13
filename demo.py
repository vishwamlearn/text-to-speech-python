from components.get_accent import get_accent_tld,get_accent_message

accent_list=get_accent_message()

print(accent_list)

accent=accent_list[3]
tld=get_accent_tld(accent)
print(tld)