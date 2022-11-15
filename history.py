import datetime
new_log=str(datetime.datetime.now())
def write_history():
    with open('log.txt','a') as f:
         f.write(new_log+'\n')
def read_history():
     with open('log.txt','r') as f:
         index=f.readlines()
         last=index[-1][:-8]
         return last
#print(read_history())
 
