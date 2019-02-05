string= str(input("Enter the string: "))
if string>='a' and string<='z' or string>='A' and string<='Z':
    if string=='a' or string=='e' or string=='i' or string=='o' or string=='u' or string=='A' or string=='E' or string=='I' or string=='O' or string=='U':
        print("vowel")
    else:
        print("consonant")
else:
    print("invalid")
