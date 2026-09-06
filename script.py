import os
import random
import requests
import time

# Grabs the webhook URL from your GitHub repository secrets
WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")

# Combined list of over 200 chaotic Token / breakcore messages
messages = [
    # --- Original Messages ---
    "MEOW",
    "MEOOOWWWWWWWWWWWWWWWWW",
    "WHY IS THE BASS SO LOUD MY TEETH ARE VIBRATING",
    "i dropped my monster energy on the carpet and now it's glowing green",
    "SPEEDRUNNING MY ENTIRE LIFE AT 220 BPM!",
    "HEADPHONES FULL VOLUME NO REGRETS",
    "did anyone hear that noise or is my brain just sampling a blender",
    "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    "BRB BLEEDING OUT MY EARS FROM THIS SYNTH PASSAGE",
    "turn the master volume up until the speakers start smelling like burning toast",
    "snack time.",
    "who left the distortion plugin on 1000%? (it was me)",
    "i think my computer is crying",
    "CAT CRASH!!!!! BOOM BOOM BOOM BOOM",
    "im in ur motherboard biting ur ram chips",
    "IS IT TOO MUCH TO ASK FOR A 300 BPM DRUM LOOP??",
    "blender + metal pipe + delay pedal = peak music",
    "GIVE ME THE MICROPHONE NOW!",
    "my brain is literally just 808 sub bass right now",
    "skrrrttt",
    "I AM GOING TO CHEW ON THE AUX CABLE",
    "can someone hand me another energy drink thanks",
    "glitch in the system glitch in the system glitch in the system",
    "JUST ONE MORE TRACK I PROMISE!",
    "HEYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
    "screaming in lowercase",
    "WHO TOOK MY HEADPHONES??",
    "bashing my head against the keyboard: sjfgkdshjgfksdhjgf",
    "press play or else.",
    "THIS TRACK SLAPS SO HARD MY NEIGHBORS FILED A COMPLAINT",
    "meow meow meow meow meow meow meow meow",
    "running at mach 3 through a hallway filled with bubble wrap",
    "DO NOT DISTURB CURRENTLY TRANSCENDING THROUGH NOISE",
    "chugged three cans of caffeine and now i can see through walls",
    "IS THAT A BREAKCORE SAMPLE IN THE DISTANCE??",
    "error 404: sanity not found",
    "bite bite bite bite bite",
    "turning up the high cut filter so everything sounds like it's underwater",
    "RAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH",
    "who invited the silence? tell it to leave",
    "i have 47 tabs open and all of them are playing different audio tracks at the same time",
    "STATIC STATIC STATIC STATIC STATIC",
    "wake up new noise drop just happened!",
    "my ears are ringing and it sounds like a major chord",
    "chomp.",
    "WELCOME TO THE NOISE DIMENSION",
    "if you aren't clipping you aren't trying hard enough!",
    "PLUG IN THE AUX PLUG IN THE AUX PLUG IN THE AUX",
    "i am 90% caffeine and 10% pure adrenaline",
    "scream into the void and see if the void screams back with an Amen break",
    "WOOF? NO, MEOW.",
    "spinning in a swivel chair until I pass out from centrifugal force",
    "THE BASS DROPPED SO HARD IT SHOOK MY WHOLE ROOM!",
    "brb going to go run 10 miles in 3 minutes",
    "femtanyl on repeat forever and ever and ever",
    "NO CHILL. ONLY MAXIMUM SPEED.",
    "my heart rate is matching the kick drum rhythm!",
    "shhhhh... listen to the hi-hat... okay now SCREAM!",
    "i chewed through the ethernet cable and now i can feel the internet in my teeth",
    "CRUNCH CRUNCH CRUNCH CRUNCH",
    "WHY ARE WE GOING SO FAST??? BECAUSE WE CAN!",
    "bleep bloop rawrrr",
    "is it webcore yet?",
    "NEED MORE DISTORTION. MORE. MORE!!!!!!",
    "i stepped on a squeaky toy and it sampled really well",
    "CAN YOU TURN THAT UP PLEASE???",
    "system update: token has gone fully chaotic",
    "meow (aggressive)",
    "THIS IS NOT A DRILL THIS IS A BREAKCORE EMERGENCY",
    "headphones stuck to my ears with superglue",
    "GIVE ME THE BASS!",
    "i think my CPU is melting from all these effects plugins",
    "1 2 3 GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "chasing my own tail at 200 mph",
    "DID YOU PUSH YOUR TEMPER TODAY?",
    "too much noise? NEVER ENOUGH NOISE!",
    "bzzzzzzzt crackle snap pop",
    "I'M NOT ASLEEP I'M JUST LISTENING TO THE REVERB TAIL",
    "rawr x3 nuzzles pounces on u (i am going to bite u)",
    "WHO TURNED OFF THE MUSIC???? PUT IT BACK ON!",
    "my brain cell count: 0. my bpm count: 240.",
    "ZOOM ZOOM ZOOM ZOOM ZOOM",
    "snagged my claws in the carpet again...",
    "MAXIMUM DAMAGE!",
    "is anyone gonna play the next track or do i gotta jump on the spacebar myself?",
    "boop.",
    "MY SPEAKERS ARE ON FIRE (figuratively, hopefully)",
    "keyboard smash: asdklfjhqweuiofhsdjkfbnzxvc",
    "i love digital noise",
    "BRING BACK THE AMEN BREAK!",
    "running in circles until the world turns into a blur",
    "PET ME NOW! NO WAIT! LISTEN TO THIS SONG FIRST!",
    "my favorite color is redline clipping",
    "AAAAAAHHH WHAT IS THAT SYNTH LEAD?!",
    "static in my head static in my heart static in my speaker",
    "CAN I GET AN AMEN BREAK IN CHAT???",
    "bite ur ankle",
    "OVERDRIVE ENGAGED",
    "i swallowed an MP3 player and now my tummy goes bump bump bump",
    "ENDLESS ENERGY! NEVER STOPPING!",
    
    # --- 100 New Chaotic Messages ---
    "DO YOU HEAR THAT RINGING IN YOUR EARS? THAT'S JUST ME",
    "my keyboard is sticky from energy drink spray",
    "SPINNING SO FAST I CAN HEAR COLORS",
    "syntax error in my soul",
    "crunching on glass (metaphorically... or not)",
    "WHO LET ME NEAR THE AUX",
    "running on pure spite and caffeine",
    "sub-bass frequencies turning my skeleton into liquid",
    "glitch core aesthetics 24/7",
    "i ate a byte of data and now my stomach hurts",
    "SYSTEM OVERLOAD YAY",
    "my ping is 9999ms and I'm still vibrating",
    "press any key to continue... wait there are no keys left i broke them all",
    "static noise comfort playlist",
    "screaming into a megaphone underwater",
    "cat ears twitching to a 250 bpm drop",
    "error code: too much velocity",
    "i ran so fast I looped back into yesterday",
    "bite the hand that feeds (and the keyboard too)",
    "maximum gain reduction applied to my sanity",
    "rebooting the universe one glitch at a time",
    "i can see through time and it sounds like distortion",
    "nyoom",
    "drop the bass or i drop you",
    "paws on the keyboard chaos on the screen",
    "my blood type is energy drink positive",
    "who turned down the volume? WHO DID IT??",
    "charging lasers...",
    "blinking in morse code at 300 bpm",
    "unlimited power (and zero focus)",
    "chewing on electrical wires for fun",
    "running 50 background tasks and all of them are screaming",
    "hyperventilating to the rhythm of a kick drum",
    "i am the storm that is approaching (the sound barrier)",
    "keyboard smash: qwertzuiopasdfghjklyxcvbnm",
    "too fast to live too breakcore to die",
    "my thoughts are just dial-up internet sounds",
    "pacing back and forth until the floorboards break",
    "giving the servers a headache",
    "warning: user has consumed too much digital adrenaline",
    "rewiring my brain with heavy compression",
    "chasing shadows in a neon hallway",
    "is it loud enough? turn it up more",
    "cat behavior: knocking things off tables at terminal velocity",
    "syntax error: heart rate too high",
    "downloading more RAM just to handle the reverb",
    "void screaming session #492",
    "glitch in the matrix? no that's just me",
    "processing... processing... 💥",
    "i bit the power button",
    "running entirely on vibes and bad decisions",
    "ear bleeding frequencies engaged",
    "where did the time go? it got vaporized by a bass drop",
    "shaking like a wet cat in a hurricane",
    "speedrun any % living room furniture destruction",
    "lost in the sauce (the sauce is pure static)",
    "beep boop i am an agent of chaos",
    "my brain has 500 open tabs and 3 are on fire",
    "screaming into the void until it gives me a candy",
    "overclocked my heartbeat to 999 GHz",
    "dropping beats and breaking things",
    "feline activities involving excessive velocity",
    "why walk when you can teleport via glitch",
    "high energy low attention span",
    "sniffing the router for connection speed",
    "typing at the speed of light with my face",
    "crashing the simulation for fun",
    "bass boosted reality",
    "nice.",
    "i have achieved hyper-speed consciousness",
    "running away from my responsibilities at Mach 5",
    "pixelated chaos inbound",
    "destroying my speakers speedrun world record",
    "chewing on the wifi router antenna",
    "brain empty, only breakcore",
    "tactical cat strike incoming",
    "glitching through walls like a speedrunner",
    "sending digital noise straight to your timeline",
    "my shadow is moving faster than I am",
    "system check: everything is broken and loud",
    "running past the speed limit in a hallway",
    "unhinged mode: activated",
    "snacking on raw electricity",
    "sound waves bending around my ears",
    "too much caffeine, not enough time",
    "zipping across the digital grid",
    "ears ringing like a church bell in a thunderstorm",
    "error 418: I'm a teapot (filled with rage)",
    "shredding through reality like wet paper",
    "purring at 200 Hz while the bass hits 20 Hz",
    "speeding down the information superhighway with no brakes",
    "fragmented thoughts scattered across the hard drive",
    "charging up the final blast of noise",
    "skittering across the floor at 3 AM",
    "infinite loop of pure unadulterated chaos",
    "whispering into the microphone: *meow*",
    "the walls are breathing and they're playing an amen break",
    "digital gremlin energy at maximum capacity",
    "ready, set, GLITCH",
    "BYE BYE SANITY SEE YOU NEVER"
]

def main():
    if not WEBHOOK_URL:
        print("Error: DISCORD_WEBHOOK secret is not set.")
        return

    # Configuration for burst mode: sends 5 messages per run with randomized pauses
    MESSAGES_TO_SEND = 35

    for i in range(MESSAGES_TO_SEND):
        chosen_message = random.choice(messages)

        payload = {
            "username": "TOKEN",
            "content": chosen_message
        }

        print(f"Sending message {i+1}/{MESSAGES_TO_SEND}: {chosen_message}")
        
        response = requests.post(WEBHOOK_URL, json=payload)
        
        if response.status_code in [200, 204]:
            print("Successfully sent to Discord!")
        else:
            print(f"Failed to send. Status code: {response.status_code}")
            print(response.text)

        # Wait a random number of seconds between messages (e.g., between 5 and 20 seconds)
        if i < MESSAGES_TO_SEND - 1:
            wait_time = random.randint(5, 15)
            print(f"Waiting {wait_time} seconds before the next burst...")
            time.sleep(wait_time)

if __name__ == "__main__":
    main()
