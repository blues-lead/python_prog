def main():
    times = [630, 1015, 1415, 1620, 1720, 2000]
    haku = int(input("Enter the time (as an integer): "))
    i = 0
    while i < len(times):
        if times[i] >= haku:
          break
        i += 1
    new_times = times[i:]
    if len(new_times) < 3:
        sz = 3 - len(new_times)
        new_times = new_times + times[0:sz]
    else:
        new_times = times[i:i+3]
    print("The next buses leave:")
    for el in new_times:
        print(el)



main()