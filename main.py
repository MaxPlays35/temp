class Clock:
    def __init__(self, *args) -> None:
        if len(args) == 3:
            self.time = args[0] * 60 * 60 + args[1] * 60 + args[2]
        elif len(args) == 2:
            self.time = args[0] * 60 * 60 + args[1] * 60
        elif len(args) == 1:
            self.time = args[0]
        else:
            self.time = 0

    def __add__(self, inst: object):
        return Clock((self.time + inst.time) % 86400)

    def __sub__(self, inst: object):
        if self.time < inst.time:
            raise ValueError("First time must be greater that second")
        return Clock(abs((self.time - inst.time) % 86400))

    def __eq__(self, inst: object) -> bool:
        return self.time == inst.time

    def __gt__(self, inst: object):
        return self.time > inst.time

    def __lt__(self, ints: object):
        return self.time < ints.time

    def __le__(self, inst: object):
        return self.time <= inst.time

    def __ge__(self, ints: object):
        return self.time >= ints.time

    def __str__(self) -> str:
        if self.time >= 43200:
            temp = self.time - 43200
            hours = temp // 60 // 60
            minutes = (temp - hours * 60 * 60) // 60
            seconds = (temp - hours * 60 * 60 - minutes * 60)
            return f'{hours}:{minutes}:{seconds} PM'
        hours = self.time // 60 // 60
        minutes = (self.time - hours * 60 * 60) // 60
        seconds = (self.time - hours * 60 * 60 - minutes * 60)
        return f'{hours}:{minutes}:{seconds} PM'


time_1 = Clock(3)
time_2 = Clock(121)
time_3 = time_1 + Clock(86400)
# time_4 = time_1 - time_2
print(time_2)
print(time_3)
