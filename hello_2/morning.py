import datetime
hour = datetime.datetime.now().hour
name = input("Bonvolu diru min nomon vian: ")
if hour < 12:
    print("Bonan matenon ", name)
elif hour < 18:
    print("Bonan vesperon ", name)
else:
    print("Bonan nokton ", name)

print("Vi estas mirinda")
# mian adici
timeEx = datetime.datetime.now(tz=None)
print(timeEx)
