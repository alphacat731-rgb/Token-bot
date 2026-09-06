import os
import random
import string
import requests

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")

if not WEBHOOK_URL:
    print("Error: DISCORD_WEBHOOK secret is missing.")
    exit(1)

TOKEN_AVATAR = "https://i.scdn.co/image/ab6761610000e5eb2a265691383ed1cf226b528b"
EMBED_COLOR = 16711765  # Vibrant pink (#FF0055)

# Femtanyl track list with direct clickable links
FEMTANYL_TRACKS = [
    {"title": "PUSH UR TEMPER", "url": "https://femtanyl.bandcamp.com/track/push-ur-temper"},
    {"title": "KATAMARI", "url": "https://femtanyl.bandcamp.com/track/katamari"},
    {"title": "LOVESICK, CANNIBAL!", "url": "https://femtanyl.bandcamp.com/track/lovesick-cannibal"},
    {"title": "CHASER", "url": "https://femtanyl.bandcamp.com/track/chaser"},
    {"title": "ACT RIGHT", "url": "https://femtanyl.bandcamp.com/track/act-right"},
    {"title": "DINNER!", "url": "https://femtanyl.bandcamp.com/track/dinner"},
    {"title": "DOGMATICA", "url": "https://femtanyl.bandcamp.com/track/dogmatica"},
    {"title": "WEIGHTLESS!", "url": "https://femtanyl.bandcamp.com/track/weightless"},
]

FEMTANYL_QUOTES = [
    "PUSH UR TEMPER!",
    "LOVESICK, CANNIBAL!",
    "KATAMARI!",
    "CHASER!",
    "ACT RIGHT!",
    "PICK UP THE PACE!",
    "DINNER!",
    "EVERY TIME I TRY TO THINK MY HEAD GOES BLANK!",
    "SPEEDRUN!",
    "DOGMATICA!",
    "WEIGHTLESS!",
]

def generate_noise(length=12):
    """Generates random webcore/breakcore noise strings."""
    chars = string.ascii_lowercase + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# Randomly select a quote or noise
is_quote = random.choice([True, False])
quote_text = random.choice(FEMTANYL_QUOTES) if is_quote else f"||{generate_noise(20)}||"

# Select a random featured track
track = random.choice(FEMTANYL_TRACKS)

# Construct embed description with Markdown hyperlinks
description_text = (
    f"{quote_text}\n\n"
    f"🎧 **Featured Track:** [{track['title']}]({track['url']})\n"
    f"🔗 **Listen:** [Bandcamp](https://femtanyl.bandcamp.com/) | "
    f"[Spotify](https://open.spotify.com/artist/7M2R1j8M8PjR6nN2vN6pG3) | "
    f"[YouTube](https://www.youtube.com/@femtanyl)"
)

payload = {
    "username": "TOKEN",
    "avatar_url": TOKEN_AVATAR,
    "embeds": [
        {
            "title": "FEMTANYL / TOKEN BROADCAST",
            "url": track['url'],  # Clicking the title opens the track URL directly
            "description": description_text,
            "color": EMBED_COLOR,
            "footer": {
                "text": f"BPM: {random.randint(170, 240)} | Noise: {generate_noise(8)}"
            }
        }
    ]
}

response = requests.post(WEBHOOK_URL, json=payload)

if response.status_code == 204:
    print(f"Token broadcast sent with track: {track['title']}")
else:
    print(f"Failed to send broadcast. Status: {response.status_code}, Response: {response.text}")
