import subprocess

print("Data Preprocessing ...")
subprocess.run(["python" , "./scripts/preprocessing.py"] , check=True)

print("Joining Tables ...")
subprocess.run(["python" , "./scripts/join.py"] , check=True)

print("Data Analysis ...")
subprocess.run(["python" , "./scripts/analysis.py"] , check=True)

print("Finished!")