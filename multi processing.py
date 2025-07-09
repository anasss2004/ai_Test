import multiprocessing
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
    with open(f'processed-output multi processing/{li}processed.txt',"w") as f:
        f.write(uppertext)

def multiprocess_file(text,num):
    read(text)
    for i in range(num):
        print(f"processing with {i+1} processes")
        start=time.perf_counter()
        # Create a pool of workers to handle the file download tasks
        with multiprocessing.Pool(processes=i+1) as pool:
        # Map the download tasks to the pool of worker processes
            pool.map(Capitale,list)
            print(f"this took{time.perf_counter()-start}")
        
            
            
if __name__=='__main__':
    multiprocess_file("text_1.txt",4)
        
