import time
import numpy as np

# Import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, Data, RequestError

# Set to your Adafruit IO key.
ADAFRUIT_IO_KEY = 'aio_FCop625tIn10NPSfYiSuV1E2mx6E'

# Set to your Adafruit IO username.
ADAFRUIT_IO_USERNAME = 'alexGt8z'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Assign a feed, if one exists already
try:
    sinusoidal_feed = aio.feeds('sinusoidal')
except RequestError: # Doesn't exist, create a new feed
    feed_sinusoidal = Feed(name="sinusoidal")
    sinusoidal_feed = aio.create_feed(feed_sinusoidal)
    
# Assign a feed, if one exists already
try:
    cosinusoidal_feed = aio.feeds('cosinusoidal')
except RequestError: # Doesn't exist, create a new feed
    feed_cosinusoidal = Feed(name="cosinusoidal")
    cosinusoidal_feed = aio.create_feed(feed_cosinusoidal)


#Data analytics
i=0
t = np.linspace(0,10,500) #tiempo
f = 2 #frecuencia
w = 2 * np.pi * f #2*pi*frecuencia
A = 10 #Amplitud
sinusoidal_sgn = A * np.sin(w * t)
cosinusoidal_sgn = A * np.cos(w * t)

#Send information for a period of time to Adafruit IO
while i < 1000:
    # Send data to Adafruit IO
    aio.send(sinusoidal_feed.key,str(sinusoidal_sgn[i]))
    aio.send(cosinusoidal_feed.key,str(cosinusoidal_sgn[i]))
    print(sinusoidal_sgn[i])
    print(cosinusoidal_sgn[i])
    i += 1

    # Timeout to avoid flooding Adafruit IO in seconds
    time.sleep(4)