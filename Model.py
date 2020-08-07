from Sketch_model import Sketch

for i in range(8,12):
    Neeraj = Sketch("images/{}.jpg".format(i),"Samples","Neeraj{}.jpg".format(i))
    Neeraj.sketchit()