import os
import requests
import datetime

base_dir = "C:/Users/Rafist0/Documents/adventOfCode2022/programs/"

session_id = open(base_dir + "data/session.id", encoding="utf-8").read()
print(session_id)

d = int(datetime.datetime.now().strftime("%d"))
print(f"https://adventofcode.com/2022/day/{str(d)}/input")

input = requests.get(f"https://adventofcode.com/2022/day/{str(d)}/input", cookies={"session": session_id})

with open(f"{base_dir}data/{str(d)}.12.input.txt", "w") as file:
    file.write(input.content.decode("utf-8"))

if not os.path.exists(f"{base_dir}rw.{str(d)}.12.py"):
    with open(f"{base_dir}rw.{str(d)}.12.py", "w") as file:
        file.write(f"""file = open("{base_dir}data/{str(d)}.12.input.txt").read().split('\n')""")
