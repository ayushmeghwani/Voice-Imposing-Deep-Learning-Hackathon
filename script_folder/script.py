import os
import paramiko

path_input = os.path.dirname(os.path.realpath(__file__))+'/input/'
path_output = os.path.dirname(os.path.realpath(__file__))+'/output/'

path_remote = "/home/akul/Desktop/sem6/deep_learning/hackathon/"

# Connect to remote host
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.8.20.66', username='akul', password='qwerty')

# Setup sftp connection and transmit this script

sftp = client.open_sftp()
sftp.put(path_input+'test.wav', path_remote+'input/test.wav')
# # sftp.get(path_remote+'input/test.wav','./test.wav')
# sftp.close()
print("audio file copied")
# Run the transmitted script remotely without args and show its output.
# SSHClient.exec_command() returns the tuple (stdin,stdout,stderr)
cmnd = "cd /home/akul/Desktop/sem6/deep_learning/hackathon/ && python client2.py"
stdout = client.exec_command(cmnd)[1]
data = ""
for line in stdout:
    # Process each line in the remote output
    data = line
    print(line)

print("audio-to-text done")

file = open("a.txt","w")
file.write("\n")
file.write("1. "+data[:-1]+".")
file.close()
sftp.put('./a.txt', path_remote+'DLHack/harvard_sentences.txt')

print("audio-to-text file copied")


cmnd = "cd /home/akul/Desktop/sem6/deep_learning/hackathon/DLHack/ && python synthesize.py"
stdout = client.exec_command(cmnd)[1]
for line in stdout:
    # Process each line in the remote output
    print(line)

print("audio-to-audio done")


sftp.get(path_remote+'/DLHack/samples/1.wav',path_output+'test.wav')

print("audio-to-audio file copied")


client.close()