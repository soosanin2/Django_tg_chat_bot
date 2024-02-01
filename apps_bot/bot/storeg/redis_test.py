# import asyncio
#
# from aiogram.fsm.storage.redis import RedisStorage
#
# storage = RedisStorage.from_url('redis://localhost:6379/0')
#
# async def start():
#
#
#     await storage.redis.set(name='1234', value=1, ex=10)
#
#     for i in range(15):
#         value = await storage.redis.get(name='1234')
#
#         if value:
#             print(f'ok {value.decode()}')
#         else:
#             print('not ok')
#             break
#         await asyncio.sleep(1)
#
#
# asyncio.run(start())
