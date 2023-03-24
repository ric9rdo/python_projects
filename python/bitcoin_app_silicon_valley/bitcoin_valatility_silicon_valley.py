import requests
import pygame
import time

# Define the threshold price
threshold = 50000

# Initialize pygame mixer
pygame.mixer.init()

while True:
    # Fetch the current Bitcoin price from Coinbase API
    response = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/spot')
    price = float(response.json()['data']['amount'])

    # Check if the current price is below the threshold
    if price < threshold:
        # Load and play the sound file
        sound = pygame.mixer.Sound('/Users/ricardoribeiro/Dropbox/VisualStudioCode/VSCode/WEB3/Bitcoin app Silicon Valley/alert.mp3')
        sound.play()
        print('Bitcoin price has fallen below the threshold!')

    # Wait for 5 seconds before checking again
    time.sleep(5)
