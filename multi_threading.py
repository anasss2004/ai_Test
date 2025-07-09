from concurrent.futures import ThreadPoolExecutor
import time
li=0
list=[]
chunk_size=1024 * 1024
def read(text):
     #not error handling
     with open(text, 'r') as file:
        while chunk:= file.read(chunk_size):
            list.append(chunk)
def capitale(text):
    global li
    li+=1
    uppertext=text.upper()
    with open(f'processed-output multi threading/{li}processed.txt',"w") as f:
        f.write(uppertext)
def multithread_file(text,num):
    read(text)
    for i in range(num):
        print(f"processing with {i+1} threads")
        start=time.perf_counter()
        with ThreadPoolExecutor(max_workers=i+1) as executor:
            executor.map(Capitale, list)
        print(f'this took {time.perf_counter()-start}')
         
            
if __name__=='__main__':
    multithread_file("text_1.txt",4)
