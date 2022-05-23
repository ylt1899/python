place = int(input())
maybe_place = []
for i in range(place):
    may = int(input())
    if may % 9 == 0 or may % 11 == 0:
        maybe_place.append(f"第{i+1}個點 {may}")
if len(maybe_place) == 0:
    print("0")
else:
    for i in maybe_place:
        print(i)