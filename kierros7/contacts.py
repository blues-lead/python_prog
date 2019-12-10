# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: contacts, program code template


def main():
    contacts = {"Tom": {"name": "Tom Techie",
                        "phone": "040 123546",
                        "email": "tom@tut.fi",
                        "skype": "tom_92_"},
                "Mike": {"name": "Mike Mechanic",
                         "phone": "050 123546",
                         "email": "mike@tut.fi",
                         "skype": "-Mike-M-"},
                "Archie": {"name": "Archie Architect",
                           "phone": "050 987654",
                           "email": "archie@tut.fi"}}

    #contact = input("Enter the name of the contact: ")
    # field = input("Enter the field name you're searching for: ")
    name = input("Enter the name of the contact: ").strip()
    field = input("Enter the field name you're searching for: ").strip()
    if name not in contacts:
        print("No contact information for", name)
        return
    contact_list = contacts[name]
    if field not in contact_list:
        print("No", field,  "for", contact_list["name"])
        return
    print(contact_list["name"],", ",field,": ",contact_list[field],sep = "")



main()
