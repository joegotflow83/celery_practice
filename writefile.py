
import tasks


for _ in range(15):
    print("Queing up task")
    tasks.write_file.delay()

print("Rest of the program")
