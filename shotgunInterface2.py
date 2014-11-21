__author__ = 'andrew.willis'

from shotgun_api3 import Shotgun

sg = Shotgun("http://andrewwillish.shotgunstudio.com", "scriptTest", "8b7db88321b7c296541580d1659872d2e63527c040b37b4a2ca0eb47f9da04cb")
proj = sg.find_one("Project",[['name','is','KIKO']])

idLis = [1166, 1167, 1168]

for id in idLis: sg.update('Shot', id, {"sg_status_list":"wtg"})