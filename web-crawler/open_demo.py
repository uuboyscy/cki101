from pathlib import Path

demo_file = Path("test.txt")

# Write something to a file
with demo_file.open("w", encoding="utf-8") as f:
    f.write("fyudisouidhjvkfdjkvfdjsgfdkl")

with demo_file.open("a", encoding="utf-8") as f:
    f.write("123123123")
    f.write("\n45456456456456")

with demo_file.open("r", encoding="utf-8") as f:
    read_str = f.read()

print(read_str)
