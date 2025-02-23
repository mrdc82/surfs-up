
'''
Here’s a breakdown of compass wind directions and their degree ranges:

North (N) → 0°
Northeast (NE) → 45° (range: 22.5° - 67.5°)
East (E) → 90°
Southeast (SE) → 135° (range: 112.5° - 157.5°)
South (S) → 180°
Southwest (SW) → 225° (range: 202.5° - 247.5°)
West (W) → 270°
Northwest (NW) → 315° (range: 292.5° - 337.5°)

'''

x=int(input("degrees: "))

if x in range(0,22):
    print("N")
elif x in range(22,67):
    print("NE")
elif x in range(67,112):
    print("E")
elif x in range(112,157):
    print("SE")
elif x in range(157,202):
    print("S")
elif x in range(202,247):
    print("SW")
elif x in range(247,292):
    print("W")
elif x in range(292, 337):
    print("NW")