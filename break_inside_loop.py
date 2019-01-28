# Program to print out all the names(and its ordinal number) in a list
# until the iteration gets to "Joseph027". When the iteration reaches "Joseph",
# the for loop will break and go to the code outside it.

name_ls = ["Abe001", "Ada002", "Apa003", "Bet004", "Ben005", "Cat006", "Joseph007", "John008", "Lisa009", "Lee010",
           "Abe011", "Ada012", "Apa013", "Bet014", "Ben015", "Cat016", "Joseph017", "John018", "Lisa019", "Lee020",
           "Abe021", "Ada022", "Apa023", "Bet024", "Ben025", "Cat026", "Joseph027", "John028", "Lisa029", "Lee030",
           "Abe031", "Ada032", "Apa033", "Bet034", "Ben035", "Cat036", "Joseph037", "John038", "Lisa039", "Lee040",
           "Abe041", "Ada042", "Apa043", "Bet044", "Ben045", "Cat046", "Joseph047", "John048", "Lisa049", "Lee050",
           "Abe051", "Ada052", "Apa053", "Bet054", "Ben055", "Cat056", "Joseph057", "John058", "Lisa059", "Lee060",
           "Abe061", "Ada062", "Apa063", "Bet064", "Ben065", "Cat066", "Joseph067", "John068", "Lisa069", "Lee070",
           "Abe071", "Ada072", "Apa073", "Bet074", "Ben075", "Cat076", "Joseph077", "John078", "Lisa079", "Lee080",
           "Abe081", "Ada092", "Apa083", "Bet084", "Ben085", "Cat086", "Joseph087", "John088", "Lisa089", "Lee090",
           "Abe091", "Ada092", "Apa093", "Bet094", "Ben095", "Cat096", "Joseph097", "John098", "Lisa099", "Lee100"]
for name in name_ls:
    ord_num = str(name_ls.index(name) + 1)
    if name == "Joseph027":
        break
    if ord_num[-1] == "1" or ord_num[-1] == "2" or ord_num[-1] == "3":
        if ord_num[-2:] == "11":
            print(f"The {ord_num}th name is {name}.")
        elif ord_num[-2:] == "12":
            print(f"The {ord_num}th name is {name}.")
        elif ord_num[-2:] == "13":
            print(f"The {ord_num}th name is {name}.")
        else:
            if ord_num[-1] == "1":
                print(f"The {ord_num}st name is {name}.")
            elif ord_num[-1] == "2":
                print(f"The {ord_num}nd name is {name}.")
            else:
                print(f"The {ord_num}rd name is {name}.")
    else:
        print(f"The {ord_num}th name is {name}.")
print(f"When we got the {ord_num}th name \"{name}\", the loop reaches the end.")



