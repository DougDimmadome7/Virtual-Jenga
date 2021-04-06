from jenga import Tower, Layer
from bots import StatBot

def layer_suite():
    subjects = {Layer(): (3, (1, 1.0)),
                Layer(False, False): (1, (1, 0.0))}
    for subject in subjects:
        if subject.get_mass() != subjects[subject][0]:
            print("Failed: Expected {}".format(subjects[subject][0]))
        if subject.get_COM() != subjects[subject][1]:
            print("Failed: Expected {}".format(subjects[subject][1]))



t1 = Tower(15)
stats = StatBot()
t1.move_piece(4,1)
t1.display()
print(stats.all_valid(t1))


