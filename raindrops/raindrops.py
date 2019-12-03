import functools

foldl = lambda func, acc, xs: functools.reduce(func, xs, acc)

def convert(number):
    sound_map_list = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    def add_sound_if_factor(accumulated_sound, sound_map):
        sound_number, sound = sound_map
        return accumulated_sound + sound if number % sound_number == 0 else accumulated_sound
    sound = foldl(add_sound_if_factor, "", sound_map_list)
    return f"{number}" if sound == "" else sound
