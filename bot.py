import socket
import time
import json

# Set variables to connect
HOST = 'irc.twitch.tv'
PORT = 6667
NICK = 'ENTER NICK HERE'
PASS = 'ENTER PASS HERE'

# Connect to specific channel
CHANNEL = input('What channel are you connecting to? ')
s = socket.socket()
s.connect((HOST, PORT))
s.send(str.encode('PASS ' + PASS + '\r\n'))
s.send(str.encode('NICK ' + NICK + '\r\n'))
s.send(str.encode('JOIN #' + CHANNEL + '\r\n'))

# Remove fluff from start of chat
while True:
    line = str(s.recv(1024))
    if 'End of /NAMES list' in line:
        break

# Initialize counter and timer
pog_counter = []
lul_counter = []
kappa_counter = []
sleep_counter = []
cry_counter = []
wut_counter = []

pog_count = 0
lul_count = 0
kappa_count = 0
sleep_count = 0
cry_count = 0
wut_count = 0

start = time.time()
t = 0
minutes = int(input('How many minutes? '))

# Main loop
while True:
    for line in str(s.recv(1024)).split('\\r\\n'):
        if 'PING' in line:
            s.send(bytes('PONG :tmi.twitch.tv\r\n', 'UTF-8'))

        parts = line.split(':')

        if len(parts) < 3:
            continue

        if 'QUIT' not in parts[1] and 'JOIN' not in parts[1] and 'PART' not in parts[1]:
            message = parts[2][:len(parts[2])]

        username = parts[1].split('!')[0]
        #print(username, ': ', message)

        if 'PogChamp' in message:
            pog_count += 1
        if 'LUL' in message:
            lul_count += 1
        if 'Kappa' in message:
            kappa_count += 1
        if 'ResidentSleeper' in message:
            sleep_count += 1
        if 'BibleThump' in message:
            cry_count += 1
        if 'WutFace' in message:
            wut_count = 0
            
    elapsed = time.time() - start

    # Reset counters every minute
    if (elapsed >= 60):
        pog_counter.append(pog_count)
        lul_counter.append(lul_count)
        kappa_counter.append(kappa_count)
        sleep_counter.append(sleep_count)
        cry_counter.append(cry_count)
        wut_counter.append(wut_count)

        pog_count = 0
        lul_count = 0
        kappa_count = 0
        sleep_count = 0
        cry_count = 0
        wut_count = 0

        print(pog_counter)

        t = t + 1
        start = time.time()
        elapsed = 0

    # After n minutes write and stop program
    if t >= minutes:
        l = [pog_counter, lul_counter, kappa_counter, sleep_counter, cry_counter, wut_counter]
        with open('data.json', 'w') as f:
            json.dump(l, f)
        break

