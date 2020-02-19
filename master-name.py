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


import os
import sys

from pyc import HumanName
from lib.tkinter import info
from lib.tkinter import tk
os.system('clear')


def main():

    a = sys.argv
    if (len(a) < 2):
       return

    n = HumanName(sys.argv[-1])
    chld = n.chalde()
    div = n.divin()
    r = n.pytha()
    jews = n.jewish()
    greek = n.greek()
    print('                       ')
    print('                       ')
    print('  === Your Real Numbers === ')
    print('  ----------------------------')
    print('  Pythagora Numerology: ==> {}'.format(r['sum']))
    print('  Chaldean Numerology: ==> {}'.format(chld['sum']))
    print('  Divine Numbers: ==> {}' .format(div['sum']))
    print('  Gematria Jewish: ==> {}'.format(jews['sum']))
    print('  Stoicheia Greek: ==> {}'.format(greek['sum']))
    print(' ===============================')
    print('                       ')
    print('                       ')
if __name__ == '__main__':
     main()

master = tk.Tk()
whatever_you_do = "Number 1 – Can be interpreted very literally as the first: an originating source of energy and a leader. Take these both together and you have a personality that stands strongest as an individual, one who creates plans, and the one who naturally takes charge." \
                  " All whole numbers can be created by addition of 1, so it has all encompassing qualities. However those that show such uniqueness do not necessarily form good bonds with others, so winning personal understanding is not as easily obtained" \
                  " as the many material achievements." \
                  "\n ----------------------------------------------------------------------" \
                  "\n Number 2 – Like 1 is an individual, 2 represents pairing and harmonious balance, and all the benefits of mutual collaboration and understanding. " \
                  "Also the active reaching out to people, helping others, resolving issues and learning from experience and feedback. However the openness and empathy can turn in a mess when it falls out of control, especially with the conflicting and" \
                  " self-serving demands of closest family and friends." \
                  "\n -----------------------------------------------------------------------" \
                  "\n Number 3 – The number 3 stands for the three key components that guide us along in life – mind, body and spirit. It in particular represents the birth of ideas in the spiritual and mental realms, and their conception into the physical. Those with this number " \
                  "in their charts experience high levels of creativity which they can channel into the disciplines of mind, body and spirit." \
                  " Number 3s are not always aware when it’s best to slow down, and need to self reflect at times where the demands of the mind exceed the capacity of the body." \
                  "\n -----------------------------------------------------------------------" \
                  "\n Number 4 – This number represents a certain stability and structure, such as the four directions on a compass or the sides of a square. Stern logic and groundedness are key here," \
                  " as are risk aversion and safety in decision making. Reliability and consistency are strong qualities, thanks to sticking to routine and the tried and tested. Very dependable qualities at " \
                  "times, but the room for growth is questionable, if a shifting in attitude " \
                  "or the promise of a surprise is ever on the cards." \
                  "\n -----------------------------------------------------------------------" \
                  "\n Number 5 – Corresponds with the five elements – earth, air, fire, water, ether – and the movement of energy between each of these. For that reason, those under the number 5 tend to be regarded " \
                  "as having a lot of strings to their bow and highly transformative, yet at the same time balanced with an ease to all that they do. Their main fuel is that of free will, they will work well as long " \
                  "as they are not tied down and can get what they want from the situation. As such, may be perceived as non-committal or deliberately hurting others," \
                  " when they are trying to put their right to freedom first." \
                  "\n -----------------------------------------------------------------------" \
                  "\n Number 6 – The number 6 gently loops around on itself, and focuses on promoting peace and harmony, with qualities of empathy and acceptance. This person puts people at ease and is seen as the go-to person " \
                  "where wise advice and counsel is required. The pros and cons of being a 6 are therefore fairly obvious, with the downside being that their own development is stalled by the amount of energy given to others, " \
                  "not least finding themselves having to absorb the emotional waste of others." \
                  "\n -----------------------------------------------------------------------" \
                  "\n Number 7 – The number 7 is almost like a question mark and people under the number 7 are the ones who tend to ask lots of questions, and as such learn, think and advance, often taking others with them. In some ways" \
                  " they blend the best qualities of 3 and 4, willing to be rational but test rationality to its limits. However questioning everything is not the purest mindset with which to enter relationships, and the negativity of " \
                  "scepticism can just as much sow seeds of doubt as opportunity." \
                  "\n -----------------------------------------------------------------------" \
                  "\n Number 8 – The number 8 is drawn as two circles looping together, representing the physical and the astral, or money and happiness, and so on. The circles do not overlap, merely touch, with one only barely knowing the other," \
                  " but somehow finding union. Those who are number 8 can find themselves disadvantaged into being too focused in excelling in one circle but not the other, much to their detriment. If they can fix this, then they will find far more" \
                  " windows of opportunity open to them. Some people say that the sign for infinity is an 8 lying on its side," \
                  " so is the symbol of 8 an infinity trying to stand upright?" \
                  "\n -----------------------------------------------------------------------" \
                  "\n Number 9 – Regarded as a particularly spiritual number. Here is where intuition presides over reasoning, creativity over stasis and chaos over order. For number 9 individuals, they live by the quest for transcendence, but there is " \
                  "often much turbulence in how this is reached. For every moment in their lives where they have displayed a sudden spark of true inspired genius and shown ascended qualities, there is another where they have hit rock bottom having pursued shadier" \
                  " pathways when seeking something more out of life." \
                  "\n -----------------------------------------------------------------------" \


msg = tk.Message(master, text = whatever_you_do)

msg.config(width='900',takefocus='true',bg='orange', font=('helvetica', 9, 'normal'))
msg.pack()
tk.mainloop()
root = info.Tk()
