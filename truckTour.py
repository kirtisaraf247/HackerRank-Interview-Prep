def truckTour(petrolpumps):
 # Write your code here
 first = fuel = 0
 for i, pump in enumerate(petrolpumps):
 fuel += pump[0] - pump[1]
 if fuel < 0:
 first, fuel = i+1, 0
 return first
