from concurrent.futures import ThreadPoolExecutor
import time
import os

chunk_size=1024 * 1024
def read(text):
     #not error handling
     chunkz=[]
     with open(text, 'r') as file:
        while chunk:= file.read(chunk_size):
            chunkz.append(chunk)
     return chunkz
def capitale(args):
    index,text=args
    uppertext=text.upper()
    os.makedirs('processed-output multi threading', exist_ok=True)
    with open(f'processed-output multi threading/{index+1}processed.txt',"w") as f:
        f.write(uppertext)
def multithread_file(text,num):
    chunkz=read(text)
    for i in range(num):
        print(f"processing with {i+1} threads")
        start=time.perf_counter()
        with ThreadPoolExecutor(max_workers=i+1) as executor:
            executor.map(capitale,[(index, chunk) for index, chunk in enumerate(chunkz)])
        print(f'this took {time.perf_counter()-start:.2f}')
         
            
if __name__=='__main__':
    multithread_file("text_1.txt",4)
