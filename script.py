import os
import random
import time

import requests

# Grabs the webhook URL from your GitHub repository secrets.
WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")

# Token-themed original messages. Kept playful, chaotic, and mascot-focused.
messages = [
    "MEOW",
    "MEOOOWWWWWWWWWWWWWWWWW",
    "TOKEN HAS ENTERED THE CHAT",
    "tiny cat, enormous volume",
    "POINTY EARS ONLINE",
    "white cat detected. chaos immediately follows.",
    "TOKEN.exe has stopped pretending to be normal",
    "*aggressive Token staring*",
    "the ears have achieved maximum signal strength",
    "TOKEN SAYS HELLO!!!!!!",
    "meow meow meow meow meow",
    "who gave Token the aux again",
    "Token found the loud button",
    "cat.exe is running perfectly fine (probably)",
    "TOKEN HAS TOO MANY TABS OPEN",
    "the little creature yearns for more bass",
    "Token is approximately 90% ears",
    "emergency Token meeting: bring snacks",
    "Token has discovered the keyboard",
    "one paw on the keyboard = complete chaos",
    "TOKEN ZOOM",
    "TOKEN NYOOOOOM",
    "POINTY EAR DETECTED. HELLO.",
    "Token is buffering... please wait for more meowing",
    "meow but in 240 BPM",
    "Token just pressed every button at once",
    "the cat has opinions about the mix",
    "Token demands another weird sound",
    "white cat, black screen, zero thoughts",
    "Token has become one with the glitch",
    "the mascot has arrived",
    "TOKEN CHECK: ears? pointy. vibes? immaculate.",
    "Token is staring directly at the waveform",
    "the waveform belongs to Token now",
    "TOKEN HAS ACQUIRED A USB CABLE",
    "do not give Token admin permissions",
    "Token found a mysterious button and pressed it",
    "system message: TOKEN IS LOUD",
    "Token is currently operating on pure silly",
    "meow.dll loaded successfully",
    "Token has 47 browser tabs and no regrets",
    "cat detected in the server room",
    "Token has entered goblin mode",
    "small paws. giant chaos.",
    "Token would like everyone to know that the bass is acceptable",
    "the ears are twitching to the beat",
    "Token is now the moderator",
    "everyone say hi to Token",
    "TOKEN!!!!! TOKEN!!!!! TOKEN!!!!!",
    "Token has spawned directly next to the aux cord",
    "the creature is pleased",
    "Token heard one weird sound and needs to investigate",
    "meow.exe has been upgraded",
    "Token has selected: MAXIMUM SILLY",
    "the server has been blessed by pointy ears",
    "Token is doing important mascot business",
    "Token just discovered caps lock",
    "TOKEN CAPS LOCK ACTIVATED",
    "Token is rapidly approaching maximum meow",
    "tiny creature detected at high velocity",
    "Token has become a professional button presser",
    "the cat is judging your playlist",
    "Token would like to speak to whoever lowered the volume",
    "meow meow. that is all.",
    "Token's ears are functioning at 100% efficiency",
    "the mascot demands another track",
    "Token has successfully achieved silly",
    "loading more Token...",
    "Token has been upgraded to Version MEOW",
    "the white cat has breached the sound barrier of silliness",
    "Token is somewhere nearby. probably behind the monitor.",
    "do NOT feed Token after midnight (they get too silly)",
    "Token has located the snack drawer",
    "server status: cat-shaped",
    "Token is now 4 pixels closer to your screen",
    "the pointy ears have opinions",
    "Token is inspecting your code",
    "Token found the bug. it was the cat.",
    "debugging complete: add more meow",
    "Token has opened the secret menu",
    "secret menu item: one extremely loud cat",
    "Token is speedrunning the settings menu",
    "the mascot has selected CHAOS MODE",
    "Token is currently spinning in a metaphorical loading icon",
    "cat firmware update: MORE EARS",
    "Token has become a desktop notification",
    "important announcement from Token: meow",
    "Token has acquired moderator energy",
    "the server belongs to the cat now",
    "Token says: keep the silly going",
    "meow meow meow meow MEOW",
    "Token has entered maximum gremlin settings",
    "the cat has a PhD in pressing random buttons",
    "Token has found the loudest possible notification sound",
    "white cat jumpscare, but friendly",
    "Token is approximately one billion pixels of silly",
    "Token has requested a snack break",
    "the mascot is watching the chat",
    "Token's ears can hear the internet",
    "Token just connected to the Wi-Fi telepathically",
    "the cat has achieved perfect reception",
    "TOKEN SIGNAL: STRONG",
    "Token is communicating exclusively in meows",
    "today's weather forecast: 100% chance of Token",
    "Token has been spotted near the waveform again",
    "the waveform made a funny shape and Token approved",
    "Token has declared this server a silly zone",
    "no thoughts, just Token",
    "Token has located the forbidden keyboard key",
    "the forbidden key has been booped",
    "Token is now a very important little creature",
    "the mascot committee has approved this message",
    "Token says hello from somewhere in the wires",
    "there is a cat in the computer",
    "Token has absolutely not rearranged your desktop icons",
    "Token has done nothing wrong. probably.",
    "the cat's ears are basically antennae",
    "Token is receiving transmissions from the silly dimension",
    "silly dimension connection established",
    "TOKEN STATUS: MEOWING",
    "TOKEN STATUS: ZOOMING",
    "TOKEN STATUS: BEING A CAT",
    "Token has achieved peak mascot",
    "another perfectly normal day with Token",
]


def send_message(message: str) -> bool:
    """Send one message through the configured Discord webhook."""
    payload = {
        "username": "TOKEN",
        "content": message,
    }

    try:
        response = requests.post(WEBHOOK_URL, json=payload, timeout=15)
    except requests.RequestException as exc:
        print(f"Webhook request failed: {exc}")
        return False

    if response.status_code in (200, 204):
        print("Successfully sent to Discord!")
        return True

    # Discord may tell us to wait when a webhook is rate-limited.
    if response.status_code == 429:
        try:
            retry_after = float(response.json().get("retry_after", 5))
        except (ValueError, TypeError):
            retry_after = 5.0
        retry_after = max(1.0, min(retry_after, 60.0))
        print(f"Rate limited. Waiting {retry_after:.1f}s...")
        time.sleep(retry_after)
        return False

    print(f"Failed to send. Status code: {response.status_code}")
    print(response.text[:500])
    return False


def main() -> None:
    if not WEBHOOK_URL:
        print("Error: DISCORD_WEBHOOK secret is not set.")
        return

    # Configure these from GitHub Actions secrets/env vars when desired.
    # Defaults keep the bot reasonably quiet and avoid accidental message storms.
    try:
        messages_to_send = max(1, min(int(os.environ.get("MESSAGES_TO_SEND", "10")), 35))
    except ValueError:
        messages_to_send = 10

    try:
        min_wait = max(1, int(os.environ.get("MIN_WAIT_SECONDS", "5")))
        max_wait = max(min_wait, int(os.environ.get("MAX_WAIT_SECONDS", "15")))
    except ValueError:
        min_wait, max_wait = 5, 15

    for i in range(messages_to_send):
        chosen_message = random.choice(messages)
        print(f"Sending message {i + 1}/{messages_to_send}: {chosen_message}")
        send_message(chosen_message)

        if i < messages_to_send - 1:
            wait_time = random.randint(min_wait, max_wait)
            print(f"Waiting {wait_time}s before the next message...")
            time.sleep(wait_time)


if __name__ == "__main__":
    main()
