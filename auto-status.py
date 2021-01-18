import vk_api
import time
import settings
from vk_api.longpoll import VkLongPoll, VkEventType
import datetime

vk = vk_api.VkApi(token=settings.TOKEN)

while True:
    now = datetime.datetime.now()
    if now.minute <= 9:
        minute = '0'+f'{now.minute}'
    else:
        minute = now.minute
    if now.hour <= 5:
        now_icon = '🌛'
    elif now.hour >= 6 and now.hour <= 11:
        now_icon = '🌄'
    elif now.hour >= 12 and now.hour <= 17:
        now_icon = '☀️'
    elif now.hour >= 18 and now.hour <= 23:
        now_icon = '🌆'
    vk.method('status.set',{'text':f'{now_icon}{now.hour}:{minute}'})
    time.sleep(30)
    print(f"Логи: {now.hour}:{minute}")