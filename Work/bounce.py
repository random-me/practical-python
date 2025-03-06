# bounce.py
#
# Exercise 1.5
height = 100 # Meters
bounce = 0 # Bounces done

while bounce < 10:
    bounce = bounce + 1
    height = height * (3/5)
    print(bounce, round(height, 4))
