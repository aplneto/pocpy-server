import signal
import time
import os
import threading

def deal_with_signal(signum, stack):
    print("This is", signum, stack)
    os._exit(0)

def deal_with_signal_usr(signum, stack):
    print("Signal Usr", signum, stack)

def alarm_sending_thread():
    time.sleep(5)
    os.kill(os.getpid(), signal.SIGUSR1)

signal.signal(signal.SIGALRM, deal_with_signal)
signal.signal(signal.SIGUSR1, deal_with_signal_usr)
signal.alarm(20)

threading.Thread(target=alarm_sending_thread).start()

while True:
    print("nothing yet...")
    time.sleep(3)