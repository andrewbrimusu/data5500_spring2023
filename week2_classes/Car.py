class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        
    def calc_value(self, current_year):
        return self.price * 0.9 ** (current_year - self.year)
        
    
     
        
class AntiqueCar(Car):
    def calc_value(self, current_year):
        return self.price * 1.04 ** (current_year - self.year)
    
    def __str__(self):
        return "amazing car! " + self.make + " " + self.model
       
        




andy_car = Car("toyota", "sequoia", 2001, 40000)
print(andy_car.calc_value(2023))

chelsea_car = Car("honda", "accord", 1993, 12000)
print(chelsea_car.calc_value(2022))

davis_car = Car("toyota", "corolla", 2013, 21000)
print(davis_car.calc_value(2023))

andys_back_again = AntiqueCar("toyota", "sequoia", 2001, 40000)
print(andys_back_again.calc_value(2023))

greg_car = AntiqueCar("Cadillac", "DeVille", 1976, 8000)
print(greg_car.calc_value(2023))

sam_car = AntiqueCar("Ford", "Mustang", 1967, 6000)
print(sam_car.calc_value(2023))

bryan_car = AntiqueCar("toyota", "celica", 2003, 18000)
print(bryan_car.calc_value(2023))


bruces_car_lot = [andy_car, chelsea_car, davis_car, andys_back_again, greg_car, sam_car, bryan_car]





tot_value = sum([my_car.calc_value(2022) for my_car in bruces_car_lot])
print("total value of bruce's cars: ", tot_value)

for car in bruces_car_lot:
    print(car)
    

    


