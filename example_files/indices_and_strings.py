#WORKING WITH INDICES AND STRINGS
device_id = "A1B2C3D4E5F6"

#ACCESSING INDIVIDUAL CHARACTERS USING INDICES
print("Device ID:", device_id[0])
print("A1B2C3D4E5F6"[0])

#STRING FUNCTIONS AND METHODS
device_id_length = len(device_id)
if device_id_length == 12:
    print("Device ID has:", device_id_length, "characters.")

#FINDING SUBSTRINGS WITH .index() METHOD
tshah_index = "tsnow, tshah, bmoreno - updated".index("tshah")
print(tshah_index)

