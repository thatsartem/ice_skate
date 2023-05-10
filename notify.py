import subprocess

CMD = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv) sound name "Blow"
end run
'''

def notify(title, text):
  subprocess.call(['osascript', '-e', CMD, title, text])
