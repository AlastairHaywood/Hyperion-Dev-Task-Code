
#variables store user input
city_flight = input("Enter the city you want to travel to \nLondon \nParis \nBerlin \nMadrid \n")
num_nights = int(input("Enter the number of nights you will be staying in a hotel. \n"))
rental_days = int(input("Enter the number of days you will be hiring a car for. \n"))


#function that multiplies the user input(number of days in hotel) by the cost of the hotel per day(50)
def hotel_cost(num_nights):
    return num_nights * 50


#function that returns the correct price(as an integer) for the city input by the user
def plane_cost(city_flight):
    if city_flight == "London":
        return 50
    elif city_flight == "Paris":
        return 65
    elif city_flight == "Berlin":
        return 75
    elif city_flight == "Madrid":
        return 100
    else:
        print("Invalid input")
        return 0

#function that multiplies the user input (number of days a car is rented) by the cost of renting the car per day (35)
def car_rental(rental_days):
    return rental_days * 35


#function that assigns the result of the previous functions to a new variable and adds these together then returns this figure
def holiday_cost(city_flight, num_nights, rental_days):
    total_hotel_cost = hotel_cost(num_nights)
    total_plane_cost = plane_cost(city_flight)
    total_car_cost = car_rental(rental_days)
    return total_hotel_cost + total_plane_cost + total_car_cost


#displays the total cost added together then the seperate costs
print(f"The total cost for your holiday is £{holiday_cost(city_flight, num_nights, rental_days)}!")
print(f"The hotel cost is £{hotel_cost(num_nights)}!")
print(f"The plane ticket cost is £{plane_cost(city_flight)}!")
print(f"The car rental cost is £{car_rental(rental_days)}!")