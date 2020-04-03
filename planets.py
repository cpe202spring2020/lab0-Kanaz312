def weight_on_planets():
   # write your code here
   weight = int(input("What do you weigh on earth? "))
   Mars_weight = weight * 0.38
   Jupiter_weight = weight * 2.34
   print("\nOn Mars you would weigh {0:2f} pounds.\nOn Jupiter you would weigh {1:2f} pounds.".format(
      Mars_weight, Jupiter_weight)
   
   
if __name__ == '__main__':
   weight_on_planets()
