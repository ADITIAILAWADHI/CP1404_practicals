NAME_TO_CODE = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "ANTIQUEWHITE1" : "#ffefdb", "ANTIQUEWHITE2" : "#eedfcc", "ANTIQUEWHITE3": "#cdc0b0", "ANTIQUEWHITE4": "#8b8378", "AQUAMARINE1": "#7fffd4", "AQUAMARINE2": "#76eec6", "AQUAMARINE4": "#458b74", "DARKGREEN": "#006400"}
print(NAME_TO_CODE)

color_name = input("Enter color name: ").upper()
while color_name != "":
    if color_name in NAME_TO_CODE:
        print(color_name, "is", NAME_TO_CODE[color_name])
    else:
        print("Invalid short name")
    color_name = input("Enter color name: ").upper()