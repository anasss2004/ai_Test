import asyncio
import time
import aiofiles
import os
chunk_size=1024 * 1024
li=0
async def read(text):
     #not error handling
     global li
     os.makedirs('processed-output_asyncio', exist_ok=True)
     async with aiofiles.open(text, 'r') as file:
        while chunk:=await file.read(chunk_size):
            li+=1
            async with aiofiles.open(f'processed-output_asyncio/{li}processed.txt',"w") as f:
                await f.write(chunk.upper())
if __name__=='__main__':
     print("processing")
     start=time.perf_counter()
     asyncio.run(read('text_1.txt'))
     print(f"this took {time.perf_counter()-start:.2f}")
