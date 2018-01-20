## class restaurant for in class exercise

class Restaurant:
    
    def __init__(self, name = 'Jack in Box', c_type = 'Fast food'):
        self._restaurant_name = name
        self._cuisine_type = c_type
        
    def decribe_restaurant(self):
        print('The name of restautant is %s' %self._restaurant_name)
        print('The food serving is %s' %self._cuisine_type)
    
    def open_restaurant(self):
        print('Welcome to %s' %self._restaurant_name)
    
    