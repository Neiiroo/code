import time
import sys 

def somebody_pleasure():
    lyric = [
        ("\n""Soul try to figure it out", 0.10),
        ("From where I've been escapin", 0.10),
        ("Running to end all the sin", 0.11),
        ("Get away from the pressure", 0.10),
        ("\n""Wondering to get a love that is so pure", 0.10),
        ("Gotta have to always make sure", 0.10),
        ("That I'm not just somebody's pleasure", 0.10),
    ]
    delay = [1.0, 1.8, 1.3, 1.6, 4.0, 1.5, 1.0]
    print("\n""Somebody Pleasure - Aziz Hendra")
    time.sleep(0.2)
    for i, (baris_lagu, delay_karakter) in enumerate(lyric):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    print("\n""Code by - Neiro Skibidi")

if __name__ == "__main__":
    somebody_pleasure()