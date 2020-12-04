from util import *
from emulator import Emulator
import os
import shutil


class NoCash(Emulator):
    def __init__(self):
        super().__init__("No$gmb", startup_time=1.6)
        self.speed = 1.0

    def setup(self):
        download("https://problemkaputt.de/no$gmb.zip", "downloads/no$gmb.zip")
        extract("downloads/no$gmb.zip", "emu/no$gmb")
        setDPIScaling("emu/no$gmb/no$gmb.exe")
        shutil.copyfile(os.path.join(os.path.dirname(__file__), "nocash.ini"), "emu/no$gmb/NO$GMB.INI")
    
    def startProcess(self, rom, *, gbc=False):
        return subprocess.Popen(["emu/no$gmb/no$gmb.exe", os.path.abspath(rom)], cwd="emu/no$gmb")

    def getScreenshot(self):
        screenshot = getScreenshot(self.title_check)
        return screenshot.crop((80, 34, 80 + 160, 34 + 144))
