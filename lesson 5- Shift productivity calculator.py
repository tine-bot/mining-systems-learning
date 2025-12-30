pit_name= input("Enter pit Name:")
tonnes= float(input("Enter of tonnes  mined:"))
hours= float(input("Enter hours worked:"))
target_tph= float(input("Target TPH:"))
tph= tonnes/hours

print("\n---SHIFT PERFOMANCE REPORT---")
print(f"Pit:{pit_name}")
print(f"Productivity:{tph:2f}tonnes/hour")

if tph >= target_tph: 
 print("Status: Target met")
elif tph >= target_tph* 0.9:
 print("Status: Slightly below target")
else: print("Status: Poor perfomance")

