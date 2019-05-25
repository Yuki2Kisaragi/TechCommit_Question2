def input_time():
    while(1):
        time=float(input("初期微動継続時間を入力してください(正の整数のみ)"))
        time=int(time)
        if time <=0:
            print("正数を入力してください")
            continue
        else:   
            return time

def Distance_measure(time):
    Diff_time=S_wave-P_wave
    return Diff_time*time
    
P_wave=3.5
S_wave=7
Init_tremo_time=input_time()
print("Primary Wave="+str(P_wave))
print("Secondary Wave="+str(S_wave))
print("初期微動継続時間は"+str(Init_tremo_time))
print("震源から現在地までの距離(km)は"+str(Distance_measure(Init_tremo_time))+"[km]です。")


