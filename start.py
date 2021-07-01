import time, rpc
from time import mktime

print("Starting Discord RPC.")
client_id = '732437600622739538'
RPC_Discord = rpc.DiscordIpcClient.for_platform(client_id)
print("RPC connection successful.")

time.sleep(5)
start_time = mktime(time.localtime())
while True:
    activity = {
            "state": "Dream-Animation",
            "details": "Developing React-APP ",
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "large_text": "Dream-Animation",
                "large_image": "untitled-1"
            }
        }
    RPC_Discord.set_activity(activity)
    time.sleep(900)