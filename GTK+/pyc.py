###################################################################
# Python
# Project Name: HUMAN NUMBER NAME
# ver  1.0
# Developer: ROB GIULIANO  -a.k.a- PG
# Etherium:       0x14996EE0113C46A34b14e4F30197768b174c9486
# Bitcoin:        1HN7eNRiJFWR1JXQdMx2hwVCaANmbhnUrb
# Bitcoin Cash:   qz7h44sqpn8ud2hv04tw2kgr9ayqu94gngm2tedvrt
# Tipeeestream:   https://www.tipeeestream.com/rob-giuliano/donation
#####################################################################


class HumanName:
    def __init__(self, s):
        self._s = s
        self._l = list(self._s.replace(' ', '').strip().lower())
        self._chalde = {
            'chalde': {
                "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "u": 6, "o": 7, "f": 8,
                "i": 1, "k": 2, "g": 3, "m": 4, "h": 5, "v": 6, "z": 7, "p": 8,
                "j": 1, "r": 2, "l": 3, "t": 4, "n": 5, "w": 6, "q": 1, "s": 3,
                "x": 5, "y": 1
            }
        }
        self._pytha = {
            'pytha': {
                "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8,
                "i": 9, "j": 1, "k": 2, "l": 3, "m": 4, "n": 5, "o": 6, "p": 7,
                "q": 8, "r": 9, "s": 1, "t": 2, "u": 3, "v": 4, "w": 5, "x": 6,
                "y": 7, "z": 8
            }
        }
        self._divin = {
            'divin': {
                "a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1, "g": 1, "h": 1,
                "i": 1, "j": 1, "k": 1, "l": 1, "m": 1, "n": 1, "o": 1, "p": 1,
                "q": 1, "r": 1, "s": 1, "t": 1, "u": 1, "v": 1, "w": 1, "x": 1,
                "y": 1, "z": 1
            }
        }
        self._jewish = {
            'jewish': {
                "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8,
                "i": 9, "j": 600, "k": 10, "l": 20, "m": 30, "n": 40, "o": 50, "p": 60,
                "q": 70, "r": 80, "s": 90, "t": 100, "u": 200, "v": 700, "w": 900, "x": 300,
                "y": 400, "z": 500
            }
        }

        self._greek = {
            'greek': {
                "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 90, "g": 3, "h": 8,
                "i": 10, "j": 100, "k": 20, "l": 30, "m": 40, "n": 50, "o": 70, "p": 80,
                "q": 1, "r": 100, "s": 200, "t": 300, "u": 400, "v": 700, "w": 800, "x": 60,
                "y": 400, "z": 7, "th": 9, "ph": 500, "kh": 600, "ps": 700
            }
        }

    def chalde(self):
        d = self._chalde['chalde']
        s = ''
        k = 0
        for c in self._l:
            i = d[c]
            s += str(i)
            k += i
        return {
            'sum': k,
            'string': s
        }

    def pytha(self):
        d = self._pytha['pytha']
        s = ''
        k = 0
        for c in self._l:
            i = d[c]
            s += str(i)
            k += i
        return {
            'sum': k,
            'string': s
        }

    def divin(self):
        d = self._divin['divin']
        s = ''
        k = 0
        for c in self._l:
            i = d[c]
            s += str(i)
            k += i
        return {
            'sum': k,
            'string': s
        }

    def jewish(self):
        d = self._jewish['jewish']
        s = ''
        k = 0
        for c in self._l:
            i = d[c]
            s += str(i)
            k += i
        return {
            'sum': k,
            'string': s
        }

    def greek(self):
        d = self._greek['greek']
        s = ''
        k = 0
        for c in self._l:
            i = d[c]
            s += str(i)
            k += i
        return {
            'sum': k,
            'string': s
        }
