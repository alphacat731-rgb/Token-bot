import os
import random
import requests

# Grabs the webhook URL from your GitHub repository secrets
WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")

# The list of messages the bot will randomly pick from
messages = [
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
    "ENDLESS ENERGY! NEVER STOPPING!"
]

def main():
    if not WEBHOOK_URL:
        print("Error: DISCORD_WEBHOOK_URL secret is not set.")
        return

    # Select a random message from the list
    chosen_message = random.choice(messages)

    # The payload now only contains the username, avatar, and the raw text message
    payload = {
        "username": "TOKEN",
        "content": chosen_message
    }

    print(f"Sending message: {chosen_message}")
    
    # Send the request to Discord
    response = requests.post(WEBHOOK_URL, json=payload)
    
    # Check if it was successful
    if response.status_code in [200, 204]:
        print("Successfully sent to Discord!")
    else:
        print(f"Failed to send. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    main()
