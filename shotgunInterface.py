__author__ = 'andrew.willis'

from shotgun_api3 import Shotgun

sg = Shotgun("http://andrewwillish.shotgunstudio.com", "scriptTest", "8b7db88321b7c296541580d1659872d2e63527c040b37b4a2ca0eb47f9da04cb")
proj = sg.find_one("Project",[['name','is','KIKO']])
print sg.create("shot",{'code':'SEQ01','project':proj})
#sg.update('Shot',shot['id'],{"sg_status_list":"ip"})
#sg.delete("Shot", 1160)