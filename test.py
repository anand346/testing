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
        if(options.branch == None) :
            subprocess.call('git add .',shell=True)    
            subprocess.call('git commit -m "automated" ',shell=True)    
            subprocess.call(f'git push -u origin master',shell=True)    
        else :
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
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")


        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            
            if(options.branch == None) :
                subprocess.call('git add .',shell=True)    
                subprocess.call('git commit -m "automated" ',shell=True)    
                subprocess.call(f'git push -u origin master',shell=True)    
            else :
                subprocess.call('git init',shell=True)
                subprocess.call('git add .',shell=True)
                subprocess.call('git commit -m "automated" ',shell=True)
                subprocess.call(f'git remote add origin {options.source}',shell=True)
                subprocess.call(f'git push -u origin {options.branch}',shell=True)


        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            if(options.branch == None) :
                subprocess.call('git add .',shell=True)    
                subprocess.call('git commit -m "automated" ',shell=True)    
                subprocess.call(f'git push -u origin master',shell=True)    
            else :
                subprocess.call('git init',shell=True)
                subprocess.call('git add .',shell=True)
                subprocess.call('git commit -m "automated" ',shell=True)
                subprocess.call(f'git remote add origin {options.source}',shell=True)
                subprocess.call(f'git push -u origin {options.branch}',shell=True)



if __name__ == '__main__':
    w = Watcher()
    w.run()