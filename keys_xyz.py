import pigpio
import curses
from PigpioStepperMotor import StepperMotor, halfStepSequence
import sys

pi = pigpio.pi()
stdscr = curses.initscr()
stdscr.keypad(True)
curses.cbreak()
curses.noecho()

try:
  delay = 0.0025
  seq = halfStepSequence
  X=Y=Z=0
  if len(sys.argv) == 4:
    X = int(sys.argv[1])
    Y = int(sys.argv[2])
    Z = int(sys.argv[3])
  z = StepperMotor(pi, 21, 20, 16, 12, seq, delay, Z )
  y = StepperMotor(pi, 26, 19, 13, 6, seq, delay, Y)
  x = StepperMotor(pi, 5, 11, 10, 9, seq, delay, X)
  stdscr.addstr(str(X)+" "+str(Y)+" "+str(Z)+"\n")
  while True:
    key = stdscr.getkey()
    if key == "KEY_LEFT":
      x.doClockwiseStep()
      X+=1
    elif key == "KEY_RIGHT":
      x.doCounterclockwiseStep()
      X-=1
    elif key == "KEY_UP":
      y.doCounterclockwiseStep()
      Y-=1
    elif key == "KEY_DOWN":
      y.doClockwiseStep()
      Y+=1
    elif key == "KEY_PPAGE":
      z.doCounterclockwiseStep()
      Z-=1
    elif key == "KEY_NPAGE":
      z.doClockwiseStep()
      Z+=1
    elif key == "KEY_END":
      break
    print X,Y,Z,"\r"
except Exception as e:
  print(e)
finally:
  curses.endwin()
  pi.stop()
