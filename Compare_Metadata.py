import os

import codecs

import time

def loading():
    # List of loading animation frames
    frames = ["|", "/", "-", "\\"]
    for frame in frames:
        print(f"Loading... {frame}", end="\r")
        # Wait for 500ms
        time.sleep(0.2)
    print("Loading complete!")

if __name__ == "__main__":
    loading()


print("""
   .=-.-.                   _,.---._      .-._            .=-.-.    ,---.      
  /==/_ /   .-.,.---.     ,-.' , -  `.   /==/ \  .-._    /==/_ /  .--.'  \     
 |==|, |   /==/  `   \   /==/_,  ,  - \  |==|, \/ /, /  |==|, |   \==\-/\ \    
 |==|  |  |==|-, .=., | |==|   .=.     | |==|-  \|  |   |==|  |   /==/-|_\ |   
 |==|- |  |==|   '='  / |==|_ : ;=:  - | |==| ,  | -|   |==|- |   \==\,   - \  
 |==| ,|  |==|- ,   .'  |==| , '='     | |==| -   _ |   |==| ,|   /==/ -   ,|  
 |==|- |  |==|_  . ,'.   \==\ -    ,_ /  |==|  /\ , |   |==|- |  /==/-  /\ - \ 
 /==/. /  /==/  /\ ,  )   '.='. -   .'   /==/, | |- |   /==/. /  \==\ _.\=\.-' 
 `--`-`   `--`-`--`--'      `--`--''     `--`./  `--`   `--`-`    `--`         
""")

def compare_files(file1, file2):
    with open(file1, "rb") as f1, open(file2, "rb") as f2:
        # Only Compare first 10 bytes of each file
        bytes_to_compare = 10
        f1_bytes = f1.read(bytes_to_compare)
        f2_bytes = f2.read(bytes_to_compare)

        different_bytes = [i+1 for i in range(bytes_to_compare) if f1_bytes[i] != f2_bytes[i]]
        if different_bytes:
            print(f"Bytes {different_bytes} are different between {file1} and {file2}, maybe {different_bytes} is protected")
        else:
            print(f"The first {bytes_to_compare} bytes of {file1} and {file2} are the same")

if __name__ == "__main__":
    file1 = "global-metadata.dat"
    file2 = "2global-metadata.dat"
    if not (os.path.isfile(file1) and os.path.isfile(file2)):
        print("One or both files do not exist.")
    else:
        compare_files(file1, file2)


file1 = open("global-metadata.dat", "rb")
file2 = open("2global-metadata.dat", "rb")

data1 = file1.read(10)
data2 = file2.read(10)

if data1 == data2:
    print("The first 10 bytes of the files are the same.")
else:
    print("The first 10 bytes of the files are different.")

print("Bytes from global-metadata.dat:" + " ".join("{:02x}".format(c) for c in data1))

print("Bytes from 2global-metadata.dat:" + " ".join("{:02x}".format(c) for c in data2))

file1.close()
file2.close()

