def details():
    Name = str(input("Enter your name:"))
    Source = str(input("Enter the Starting point:"))
    Destination = str(input("Enter the destination:"))
def Luxury_Type():    
    Luxury_Type = str(input("Enter the luxury type:"))
        if Luxury_Type = Seadan :
            calculate_fare()
        if Luxury_Type = Premium:
            calculate_fare()
        if Luxury_Type = Prime:
            calculate_fare1()
def calculate_fare():
  distance = float(input("Enter the distance: "))
  distance = distance * 1000
  fare = 4.00 + ((distance / 140) * 5.00)
  
  return fare
 def calculate_fare1():
  distance = float(input("Enter the distance: "))
  distance = distance * 1000
  fare = 4.00 + ((distance / 140) * 0.70)
  
  return fare 
def print_fare(fare):
  print("%0s%.2f" % ("Fare is: Rs:", fare))
  
def main():
  fare = calculate_fare()
  print_fare(fare)
  
main()
