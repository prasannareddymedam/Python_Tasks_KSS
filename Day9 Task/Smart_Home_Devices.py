""" A smart home device may have both WiFi connectivity and Voice control features. 
Create classes WiFiDevice and VoiceAssistant, and a class SmartSpeaker that 
inherits from both using multiple inheritance.
"""

class WifiDevice:
    def wifi(self):
        print("Wifi Connected")

class VoiceAssistant:
    def voice(self):
        print("Voice Control On")

class SmartSpeaker(WifiDevice,VoiceAssistant):
    def play(self):
        print("Playing Music")

s1 = SmartSpeaker()
s1.wifi()
s1.voice()
s1.play()
