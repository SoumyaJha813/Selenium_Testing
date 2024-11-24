# class is an abstract idea of an object(bleprint of an object), and instance is an actual object, it could be any
# number of objects.
class Vehicle:
    is_engine_on = False  # properties
    is_headlight_on = False
    make = None
    model = None
    is_driving = True

    def __init__(self, make, model):  # initializer , don't need to call this method, it initializes the variable.
        # #whenever we
        # instantiate the class it is called on its own.
        self.make = make
        self.model = model

    def __repr__(self):  # represent the instance of class in string
        return (f'{self.make} {self.model} with engine '
                f'{"on" if self.is_engine_on else "off"}'
                f' and headlight {"on" if self.is_headlight_on else "off"}')

    def turn_engine_on(self):  # method:reference to class itself(self)
        self.is_engine_on = True

    def turn_engine_off(self):
        print("Turning engine off")
        if self.is_driving:
            print('You tried to turn the engine'
                  'off while driving, you crashed')
            return
        self.is_engine_on = False

    def turn_headlight_on(self):
        print('Turning headlight on')
        self.is_headlight_on = True

    def turn_headlight_off(self):
        print('Turning headlight off')
        self.is_headlight_on = False

    def start_driving(self):
        if not self.is_engine_on:
            print("You can't Drive without turning the engine on ")
            return
        print('Starting to drive')
        self.is_driving = True

    def stop_driving(self):
        print('Stop driving')
        self.is_driving = False


class Car(Vehicle):    #Inheritance
    def turn_steering_wheel(self, direction):
        print(f'Turning steering wheels {direction}')

    def turn(self, direction):
        if direction in ['left', 'right']:
            self.turn_steering_wheel(direction)
        else:
            print("Didn't understand the direction")


class Motorcycle(Vehicle):   #Inheritance
    def turn_handlebars(self, direction):
        print(f'Turning handlebars {direction}')

    def turn(self, direction):
        if direction == 'left':
            self.turn_handlebars('right')
            self.lean('left')
        elif direction == 'right':
            self.turn_handlebars('left')
            self.lean('right')
        else:
            print("Didn't understand that direction")

    def lean(self, direction):
        if not self.is_driving:
            print('You leaned while driving, and crashed!')
            return
        print(f'Leaning {direction}')

