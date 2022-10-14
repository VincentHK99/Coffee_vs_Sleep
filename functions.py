def caffine_in_bloodstream(shots):
  hours_in_bloodstream = range(1,24)
  caffine_per_hour = []
  initial_caffine_mg = shots*63
  for hour in hours_in_bloodstream:
    caffine_per_hour.append(initial_caffine_mg*(1/2)**(hour/6))
  caffine_per_hour.insert(0,initial_caffine_mg)
  return caffine_per_hour

def coffee_calculator(cups_of_coffee):
  coffee_dict = {}
  coffee_dict["shots"] = list()
  coffee_dict["time"] = list()
  for i in range(cups_of_coffee):
    coffee_dict["shots"].extend([int(input("How many shots of coffee in cup " + str(i+1) + " "))])
    coffee_dict["time"].extend([int(input("Time cup" + str(i+1) + " was drank "))])
  return coffee_dict


def coffee_graph(cups_of_coffee):
  coffee_data = coffee_calculator(cups_of_coffee)
  coffee_graph = {}

  for shot in coffee_data["shots"]:
    coffee_graph[f"{shot} shots"] = caffine_in_bloodstream(shot)

  for time in coffee_data["time"]:
    coffee_graph[f"Coffee at {time}"] = list(range(time,25))
  
  return coffee_graph
