#Class for Heigh will take separate attributed for feet and inches
class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
    def __str__(self):
        output = str(self.feet) + " Feet " + str(self.inches) + " Inches"
        return output
    
    def __add__(self, other):
        total_self_inches = self.feet * 12 + self.inches
        total_other_inches = other.feet * 12 + other.inches

        diff_inches = total_self_inches - total_other_inches

        output_feet = diff_inches // 12
        output_inches = diff_inches % 12
        #return the final output as a new height object
        return Height(output_feet, output_inches)
    
    def __lt__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A < height_inches_B



    def __le__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A <= height_inches_B



    def __eq__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A == height_inches_B

Height(4, 6) > Height(4, 5)
Height(4, 5) >= Height(4, 5)
Height(5, 9) != Height(5, 10)
#Height objects
person_A_height = Height(5, 8)
person_B_height = Height(4, 11)
height_sum = person_A_height + person_B_height

print(Height(4, 6) > Height(4, 5))  # Should print: True
print(Height(4, 5) >= Height(4, 5))  # Should print: True
print(Height(5, 9) != Height(5, 10))  # Should print: True