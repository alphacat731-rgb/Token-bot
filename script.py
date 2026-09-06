import os
import random
import string
import requests

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")

if not WEBHOOK_URL:
    print("Error: DISCORD_WEBHOOK secret is missing.")
    exit(1)

# Femtanyl / Token mascot avatar & color theme
TOKEN_AVATAR = "https://i.scdn.co/image/ab6761610000e5eb2a265691383ed1cf226b528b"
EMBED_COLOR = 16711765  # Vibrant pink/red (#FF0055)

# Chaotic Femtanyl lyrics and quotes
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

# Randomly select a quote or chaotic string
is_quote = random.choice([True, False])
message_body = random.choice(FEMTANYL_QUOTES) if is_quote else f"||{generate_noise(20)}||"

payload = {
    "username": "TOKEN",
    "avatar_url": TOKEN_AVATAR,
    "embeds": [
        {
            "title": "FEMTANYL / TOKEN BROADCAST",
            "description": message_body,
            "color": EMBED_COLOR,
            "footer": {
                "text": f"BPM: {random.randint(170, 240)} | Noise: {generate_noise(8)}"
            }
        }
    ]
}

response = requests.post(WEBHOOK_URL, json=payload)

if response.status_code == 204:
    print(f"Token broadcast sent: {message_body}")
else:
    print(f"Failed to send broadcast. Status: {response.status_code}, Response: {response.text}")
