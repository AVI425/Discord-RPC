import time, rpc
from time import mktime

print("Starting Discord RPC.")
client_id = 'Your Client ID'
RPC_Discord = rpc.DiscordIpcClient.for_platform(client_id)
print("RPC connection successful.")

time.sleep(5)
start_time = mktime(time.localtime())
while True:
    activity = {
            "state": "Your state",
            "details": "Your details",
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "large_text": "Your Text",
                "large_image": "Your Image on Discord Developer portal"
                "small_text": "Your Text",
                "small_image": "Your Image on Discord Developer portal"
            }
        }
    RPC_Discord.set_activity(activity)
    time.sleep(900)
