#svecha1
open=10
high=15
low=9
close=12
volume=120
#proverka svechi1
if open>close :
    print('bullish')
else:
    print('bearish')
    
#rasschet mfi
mfi1=(high-low)/volume
print(mfi1)
#poiavilas novaia svecha
open1=12
high1=18
low1=8
close1=17
volume1=130
#proverka svechi2
if open1>close1:
    print('bullish')
else:
    print('bearish')
    
#mfi2
mfi2=(high1-low1)/volume1
print(mfi2)
#sravnenie 2 svechei viavlenie trenda
if high1>high and low1>low:
    print('uptrend')
elif high1>=high and low1<=low:
    print('uptrend-')
elif high1<high and low1<low:
    print('downtrend')
else:
    print('downtrend-')
#sravnenie mfi
print(f"delta={mfi2-mfi1}")
if mfi2>mfi1 and volume1>volume:
    print('greenbar')
elif mfi2<=mfi1 and volume1>volume:
    print('bluebar')
elif mfi2>mfi1 and volume1<volume:
    print('fakebar')
elif mfi2<=mfi1 and volume1<volume:
    print('prised')
#svecha3
open2,high2,low2,close2,volume2=17,25,10,12,150
print(open2,high2,low2,close2,volume2)
#появилась новая свеча объявлена как кортеж
OHLCV3=(12,24,12,15,120)#каждая свеча это кортеж
open3=OHLCV3[0]#октрытие свечи соответствует OHLCV[0]


    


