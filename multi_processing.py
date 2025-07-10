import multiprocessing
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
    os.makedirs('processed-output multi_processing', exist_ok=True)
    with open(f'processed-output multi_processing/{index+1}processed.txt',"w") as f:
        f.write(uppertext)

def multiprocess_file(text,num):
    chunkz=read(text)
    for i in range(num):
        print(f"processing with {i+1} processes")
        start=time.perf_counter()
        # Create a pool of workers to handle the file download tasks
        with multiprocessing.Pool(processes=i+1) as pool:
        # Map the download tasks to the pool of worker processes
            pool.map(capitale,[(index, chunk) for index, chunk in enumerate(chunkz)])
            print(f"this took{time.perf_counter()-start:.2f}")
if __name__=='__main__':
    multiprocess_file("text_1.txt",4)
        
