def caps(s):
    s = s[0].upper() + s[1:].lower()
    return s


st = input()
if st == st.upper() or st[0] == st[0].lower() and st[1:] == st[1:].upper():
    print(caps(st))
else:
    if len(st) == 1:
        print(st.upper())
    print(st)
