import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-s", "--source", dest="source",
                  help="Give your repo url")
parser.add_option("-b", "--branch",dest="branch",
                  help="give your branch name here")

(options, args) = parser.parse_args()

class Watcher:
    DIRECTORY_TO_WATCH = "./"

    def __init__(self):
        self.observer = Observer()

        val = subprocess.check_output('git remote -v',shell=True)
        if('https://' in val.decode('utf-8').split()[1]) :

            branchName = subprocess.check_output('git rev-parse --abbrev-ref HEAD',shell=True)
            branchName = branchName.decode()

            if(options.source != "none") :
                print("https:// block source",options.source)
                subprocess.call(f'git remote set-url origin {options.source}',shell=True)     

            if(options.branch != "none") :
                print("https:// block branch")
                branchName = options.branch
                subprocess.call(f'git checkout -b {branchName}',shell=True)

            subprocess.call('git add .',shell=True)     
            subprocess.call('git commit -m "automated" ',shell=True)    
            subprocess.call(f'git push -u origin {branchName}',shell=True)  

        else :
            print("https else block")
            if(options.source != "none" and options.branch != "none") :
                subprocess.call('git init',shell=True)
                subprocess.call('git add .',shell=True)
                subprocess.call('git commit -m "automated" ',shell=True)
                subprocess.call(f'git remote add origin {options.source}',shell=True)
                subprocess.call(f'git push -u origin {options.branch}',shell=True)
            

    def run(self):
        event_handler = Handler()

        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
            print("exit")


        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if(".git" in event.src_path) : 
            return None

        elif event.is_directory:
            return None

        elif (event.event_type == 'created' or event.event_type == 'modified'):
            val = subprocess.check_output('git remote -v',shell=True)
            if('https://' in val.decode('utf-8').split()[1]) :
                print("event is : ",event.event_type)
                branchName = subprocess.check_output('git rev-parse --abbrev-ref HEAD',shell=True)
                branchName = branchName.decode()
                subprocess.call(f'git push -u origin {branchName}',shell=True)  
                subprocess.call('git add .',shell=True)    
                subprocess.call('git commit -m "automated" ',shell=True)    
                subprocess.call(f'git push -u origin {branchName}',shell=True)    

if __name__ == '__main__':
    w = Watcher()
    w.run()