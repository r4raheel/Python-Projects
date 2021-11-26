import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title="**Please Drink Water Now!!",
            message=" It is good for health",
            app_icon="D:\python\python project\Water.ico",
            timeout=12
        )
        #	time.sleep(10)
        time.sleep(60*60)
