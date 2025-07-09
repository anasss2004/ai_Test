import asyncio
import time
import aiofiles
chunksize=1024 * 1024
li=0
async def READ(text):
     #not error handling
     global li
     async with aiofiles.open(text, 'r') as file:
        while chunk:=await file.read(chunksize):
            li+=1
            async with aiofiles.open(f'processed-output asyncio/{li}processed.txt',"w") as f:
                await f.write(chunk.upper())
print("processing")
start=time.perf_counter()
asyncio.run(READ('text_1.txt'))
print(f"this took {time.perf_counter()-start}")
