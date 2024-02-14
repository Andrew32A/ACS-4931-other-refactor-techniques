# by Kami Bigdely
# Extract class

class SteakCooking:
    WELL_DONE = 3000
    MEDIUM = 2500
    COOKED_CONSTANT = 0.05

    def __init__(self, time, temperature, pressure, desired_state):
        self.time = time
        self.temperature = temperature
        self.pressure = pressure
        self.desired_state = desired_state

    def is_cookeding_criteria_satisfied(self):
        return self.is_well_done() or self.is_medium()

    def is_well_done(self):    
        return self.desired_state == 'well-done' and \
               self.get_cooking_progress() >= self.WELL_DONE

    def is_medium(self):
        return self.desired_state == 'medium' and \
               self.get_cooking_progress() >= self.MEDIUM

    def get_cooking_progress(self):
        return self.time * self.temperature * self.pressure * self.COOKED_CONSTANT


time = 30 # [min]
temp = 103 # [celcius]
pressure = 20 # [psi]
desired_state = 'well-done'

steak_cooking = SteakCooking(time, temp, pressure, desired_state)

if steak_cooking.is_cookeding_criteria_satisfied():
    print('cooking is done.')
else:
    print('ongoing cooking.')
