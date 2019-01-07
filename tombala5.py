
n=0
s=1
r=0
oyuncu_kartı=[]
oyun_gurubu=[]
sozluk={}
oyuncu_sayısı=int(input("Oyuncu sayısını giriniz\t:"))
yeni_liste=[]
import random
liste=[]
i=1    
for i in range(90):
    liste.append(i+1)
    i+=1
    if len(liste)==90:
        print(liste)
while n<oyuncu_sayısı:
    oyuncu_ismi=input("Bir isim giriniz\t:")
    oyun_gurubu.append(oyuncu_ismi)
    print(oyun_gurubu)    
    print("{} için kart oluşturunuz.".format(oyun_gurubu[n]))
    p=0   
    while p<3:
        kart=random.sample(liste,5)       
        p+=1
        oyuncu_kartı.append(kart)
        if len(oyuncu_kartı)==3:            
            sozluk[n]=oyuncu_kartı
    print("sozluk=",sozluk)    
    n+=1        
    p=0
    oyuncu_kartı=[]
while i>0 and liste!=[]:
    global cekilen_sayı
    cekilen_sayı=random.choice(liste)
    i=i-1
    print("torbada kalan taş sayıası=\t",i)    
    liste.remove(cekilen_sayı)    
    print(*"cekilen_sayı=",cekilen_sayı)    
    m=0   
    for anahtar,deger in sozluk.items():        
        while m<oyuncu_sayısı:
            print("-"*30)
            print(sozluk[m][0])     #bu bir listedir
            print(sozluk[m][1])        
            print(sozluk[m][2])
            m+=1            
            print("-"*30)
    m=0  
    #karar_liste=[(sozluk[m][0]),(sozluk[m][1]),(sozluk[m][2])]    
    while m<oyuncu_sayısı:
        
        sozluk1=[]        
        for x in ((sozluk[m][0])):           
            if x==cekilen_sayı:                
                (sozluk[m][0]).remove(cekilen_sayı)
                if len(sozluk[m][0])==0: #sozluk listesinin uzunluğu sıfır ise. boştur       
                   #print("ÇİNKO")
                   print(m)
                   print(oyun_gurubu[m])
                   yeni_liste.append(m)
                   #s+=1
        for x in ((sozluk[m][1])):            
            if x==cekilen_sayı:                
                (sozluk[m][1]).remove(cekilen_sayı)
                if len(sozluk[m][1])==0:                   
                    #print("ÇİNKO")
                    print(m)
                    print(oyun_gurubu[m])
                    yeni_liste.append(m)
                    #s+=1                                     
        for x in ((sozluk[m][2])):           
            if x==cekilen_sayı:               
                (sozluk[m][2]).remove(cekilen_sayı)
                if len(sozluk[m][2])==0:                    
                    #print("ÇİNKO")
                    print(m)
                    print(oyun_gurubu[m])
                    yeni_liste.append(m)
                    #+=1
        #print(yeni_liste)
        if yeni_liste.count(m)==3:
            print("T O M B A L A\t\\t*T O M B A L A")
            s+=1
        elif yeni_liste.count(m)==2 and s==2:
            print("2.Ç İ N K O\t\t\t2.Ç İ N K O")
            s+=1
        elif yeni_liste.count(m)==1 and s==1 :
            print("1.Ç İ N K O \t\t\t1. Ç İ N K O")
            s+=1
        m+=1        
        #print("s=",s)       
    cek=input(" Numara cekmek için 'enter' a basınız\t:")
