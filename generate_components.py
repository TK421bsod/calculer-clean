def get_input(message, help=None):
    ret = input(message).strip()
    if help:
        if ret.lower() == "h":
            print("\nHelp:")
            print(help+"\n")
            ret = get_input(message, help)
    return ret

try:
    TYPES = {"1":"number", "2":"checkbox"}
    CLASSES = {"number":"number", "checkbox":"check"}
    with open("components.json", "x") as components:
        components.write("[")
        while True:
            try:
                name = get_input("Enter a component name (enter 'h' for help): ", "A component is one form field on the final page.\nThis name will be used to identify the component both to the user and in code.")
                id = "".join([i.capitalize() for i in name.lower().replace('/','').replace('.','').replace('(','').replace(')','').split(' ')[:3]])
                print(f"Automatically generated id '{id}'.")
                while True:
                    for key, value in list(TYPES.items()):
                        print(f"{key}) {value}")
                    type = get_input("Select a component type from the above list: (enter 'h' for help) ", "Component types are the type of input to show to the user.\n'number' is a text box that allows number input.\n'checkbox' is a box that has two states: checked and not checked.\nEnter the number that matches the component type you want.")
                    try:
                        type = TYPES[type]
                        cls = CLASSES[type]
                        print(f"Alright, set component type to '{type}'.\n")
                        break
                    except KeyError:
                        print("Sorry, that type is invalid. Try again.")
                desc = get_input("Enter a description for this component (enter 'h' for help): ", "A component's description is what shows in between the name and input field on the final page.\nIt's usually a point value.")
                points = get_input("Enter a point value for this component (enter 'h' for help): ", "Point values are not shown to the user but are instead used internally to keep track of totals.\nYou must enter a number here.")
                extra = " "
                streak = ""
                if type == "number":
                    extra = " min=\\\"0\\\" "
                elif type == "checkbox":
                    if input("Should point values for this component increase by 25pts/year? Y/N ").strip().lower().startswith("y"):
                        print("Ok, enabling that.")
                        streak = f"<div class=\\\"row justify-content-center streak-wrapper\\\" id=\\\"{id}-streak-wrapper\\\"><div class=\\\"col-md-2\\\"><p>How many years? +25 pts/yr</p></div><div class=\\\"col-md-2\\\"><input data-streakpoints=25 type=\\\"number\\\" id=\\\"{id}-streak\\\" class=\\\"form-number-input\\\" min=\\\"1\\\" max=\\\"4\\\"></input></div></div>"
                        extra = "data-streakenabled=\\\"true\\\""
                    else:
                        print("Not enabling that.")
                components.write(f"\"<div class=\\\"row justify-content-center\\\"><div class=\\\"col-md-2\\\"><label for=\\\"{id}\\\">{name}</label></div><div class=\\\"col-md-2\\\"><p>{desc}</p></div><div class=\\\"col-md-2\\\"><input type=\\\"{type}\\\" class=\\\"form-{cls}-input\\\" id=\\\"{id}\\\"{extra}data-points=\\\"{points}\\\"></div>{streak}</div><hr>\",")
                print("Done with that component.\n")
            except KeyboardInterrupt:
                print("Interrupted, exiting")
                components.write("]")
                quit()
except FileExistsError:
    print("File already exists")
