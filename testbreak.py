
for i in range(4):
    print("start")
    if i == 3:
        cleanup()
        print("break")
        break
    print(i)
    def cleanup():
        print("in cleanup")
    cleanup()
    print("end")

