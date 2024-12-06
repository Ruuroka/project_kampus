import os
os.system('1cls')
print("---------------pameran Mobil----------------")
print("============================================")
print("")
pembeli = input("Masukkan Nama: ")
print("Nama Pembeli : ",pembeli)
print("Daftar Merk Mobil")
print("1.  Toyota")
print("2.  Suzuki")
print("3.  Honda")
print("4.  Daihatsu")
print("5.  Wuling")
print("6.  Mitsubishi")
print("7.  Hyundai")
print("8.  Subaru")
print("9. Lexus")
print("10. Mazda")
print("11. Mercedes-Benz")
print("12. Nissan")
print("13. BMW")
print("14. Lamborghini")
merk = int(input("Masukkan Merk Mobil : "))


if merk==1 :
  merk_mobil = "Toyota"
  print("--------Daftar Model Mobil Toyota---------")
  print("1. Avanza                  : Rp.239,7 - Rp.298,5 Jt/unit","Stock : 8 Unit")
  print("2. Kijang innova           : Rp.379   - Rp.471   Jt/unit","Stock : 7 Unit")
  print("3. Corolla Cross           : Rp.463   - Rp.608,4 Jt/Unit","stok : 5 unit")
  print("4. Calya                   : Rp.167   - Rp.190   Jt/Unit","stok : 7")
  print("5. Agya                    : Rp.170   - Rp.259,3 Jt/Unit","stok : 6")
  print("6. Rush                    : Rp.284   - Rp.310   Jt/Unit","stok : 5")
  print("7. Fortuner                : Rp.573   - Rp.761   Jt/Unit","stok : 3")
  print("8. Alphard                 : Rp.1,4   - Rp.1,71  M/Unit","stok : 2")
  print("9. Supra MK4               : Rp.2,2 M/Unit","stok : 2")
  nomor = int(input("Masukkan Nomor : "))

  if nomor==1 :
    print("---------Daftar Avanza-----------")
    print("1. Avanza 1.3E MT      : Rp.239,7 Jt/Unit","stok : 8 Unit")
    print("2. Avanza 1.5G MT      : Rp.262   Jt/Unit","stok : 8 Unit")
    print("3. Avanza 1.5G CVT TSS : Rp.298,5 Jt/Unit","stok : 8 unit")
    avanza = int(input("Avanza : "))

    if avanza==1 :
      model_mobil = "Avanza 1.3E MT"
      harga = 239700000
      stok = 8

    elif avanza==2 :
      model_mobil = "Avanza 1.5G MT"
      harga = 262000000
      stok = 8

    else :
      model_mobil = "Avanza 1.5G CVT TSS"
      harga = 298500000
      stok = 8
  
  elif nomor==2 :
    print("-----Daftar Kijang Innova----------")
    print("1. Kijang Innova 2.0 G MT        : Rp.379   Jt/Unit","stok : 7 Unit")
    print("2. kijang Innova 2.0 V AT        : Rp.442,7 Jt/Unit","stok : 7 Unit")
    print("3. Kijang Innova 2.4 V AT DIESEL : Rp.471,9 Jt/Unit","stok : 7 Unit")
    kijang = int(input("Kijang Innova : "))
    
    if kijang==1 :
      model_mobil = "Kijang Innova 2.0 G MT"
      harga = 379000000
      stok = 7
    
    elif kijang==2 :
      model_mobil = "Kijang Innova 2.0 V AT"
      harga = 442000000
      stok = 7

    else :
      model_mobil = "Kijang Innova 2.4 V AT DIESEL"
      harga = 471000000
      stok = 7

  elif nomor==3 :
    print("--------Daftar Corolla Cross---------")
    print("1. Corolla Cross 1.8 AT              : Rp.463,5 Jt/Unit","stok : 5 Unit")
    print("2. Corolla Cross 1.8 Hybrid AT       : Rp.568,2 Jt/Unit","stok : 5 Unit")
    print("3. Corolla Cross 1.8 Hybrid GR Sport : Rp.608,4 Jt/Unit","stok : 5 Unit")
    corolla = int(input("Corolla Cross : "))

    if corolla==1 :
      model_mobil = "Corolla Cross 1.8 AT"
      harga = 463500000
      stok = 5

    elif corolla==2 :
      model_mobil = "Corolla Cross 1.8 Hybrid AT"
      harga = 568200000
      stok = 5

    else :
      model_mobil = "Corolla Cross 1.8 Hybrid GR Sport"
      harga = 608400000
      stok = 5

  elif nomor==4 :
    print("-----------Daftar Calya----------")
    print("1. Calya 1.2 E MT : Rp.167,3 Jt/Unit","stok : 7 Unit")
    print("2. Calya G AT     : Rp.190   Jt/Unit","stok : 7 unit")
    calya = int(input("Calya : "))

    if calya==1 :
      model_mobil = "Calya 1.2 E MT"
      harga = 167000000
      stok = 7

    else :
      model_mobil = "Calya G AT"
      harga = 190000000
      stok = 7

  elif nomor==5 :
    print("-----------Daftar Agya-------------")
    print("1. Agya 1.2 E MT     : Rp.170,9 Jt/Unit","stok : 6 Unit")
    print("2. Agya 1.2 G CVT    : Rp.194,4 Jt/Unit","stok : 6 Unit")
    print("3. Agya 1.2 GR S CVT : Rp.259,3 Jt/Unit","stok : 6 Unit")
    agya = int(input("Agya : "))

    if agya==1 :
      model_mobil = "Agya 1.2 E MT"
      harga = 170900000
      stok = 6

    elif agya==2 :
      model_mobil = "Agya 1.2 G CVT"
      harga = 194400000
      stok = 6

    else :
      model_mobil = "Agya 1.2 GR S CVT"
      harga = 259300000
      stok = 6

  elif nomor==6 :
    print("--------Daftar Rush----------")
    print("1. Rush G MT              : Rp.284 Jt/Unit","stok : 5 Unit")
    print("2. Rush G AT              : Rp.295 Jt/Unit","stok : 5 Unit")
    print("3. Rush 1.5 S AT GR SPORT : Rp.310 Jt/Unit","stok : 5 Unit")
    rush = int(input("Rush : "))

    if rush==1 :
      model_mobil = "Rush G MT"
      harga = 284000000
      stok = 5

    elif rush==2 :
      model_mobil = "Rush G AT"
      harga = 295000000
      stok = 5

    else :
      model_mobil = "Rush 1.5 S AT GR SPORT"
      harga = 310000000
      stok = 5

  elif nomor==7 :
    print("---------Daftar Fortuner------------")
    print("1. Fortuner 4X2 2.4 G MT DSL : Rp.573,7 Jt/Unit","stok : 3 Unit")
    print("2. Fortuner VRZ 2.8 4X2      : Rp.640   Jt/Unit","stok : 3 Unit")
    print("3. Fortuner GR Sport 2.8 4X4 : Rp.761,7 Jt/Unit","stok : 3 Unit")
    fortuner = int(input("Fortuner : "))

    if fortuner==1 :
      model_mobil = "Fortuner 4X2 2.4 G MT DSL"
      harga = 573700000
      stok = 3

    elif fortuner==2 :
      model_mobil = "Fortuner VRZ 2.8 4X2"
      harga = 640000000
      stok = 3

    else :
      model_mobil = "Fortuner GR Sport 2.8 4X4"
      harga = 573700000
      stok = 3

  elif nomor==8 :
    print("--------Daftar Alpard----------")
    print("1. Alphard 2.5 X AT   : Rp.1,407M/Unit","stok : 2 Unit")
    print("2. Alphard 2.5 G AT   : Rp.1,626M/Unit","stok : 2 Unit")
    print("3. Alphard 2.5 HEV AT : Rp.1,714M/Unit","stok : 2 Unit")
    alphard = int(input("Alphard : "))

    if alphard==1 :
      model_mobil = "Alphard 2.5 X AT"
      harga = 1407000000
      stok = 2

    elif alphard==2 :
      model_mobil = "Alphard 2.5 G AT"
      harga = 1626000000
      stok = 2

    else : 
      model_mobil = "Alphard 2.5 HEV AT"
      harga = 1714000000
      stok = 2

  else :
    model_mobil = "Supra MK4"
    harga = 2237000000
    stok = 2

elif merk==2 :
  merk_mobil = "Suzuki"
  print("------------Daftar Model Mobil Suzuki-------------")
  print("1. Ertiga           : Rp.232   - Rp.266,4 Jt/Unit","Stok : 7 Unit")
  print("2. APV Arena        : Rp.182,3 - Rp.264,3 Jt/Unit","stok : 7 Unit")
  print("3. Baleno           : Rp.265,5 - Rp.283,9 Jt/Unit","stok : 4 Unit")
  print("4. Grand Vitara     : Rp.362   - Rp.391,4 Jt/Unit","stok : 5 Unit")
  print("5. Ignis            : Rp.213,8 - Rp.223,8 Jt/Unit","stok : 6 Unit")
  print("6. Karimun Wagon R  : Rp.134,5 - Rp.155,2 Jt/Unit","stok : 6 Unit")
  print("7. XL7              : Rp.259,4 - Rp.297,2 Jt/Unit","stok : 4 Unit")
  nomor = int(input("Masukkan Nomor : "))

  if nomor==1 :
    print("------------Daftar Ertiga--------------")
    print("1. Ertiga GA MT : Rp.232   Jt/Unit","stok : 7 Unit")
    print("2. Ertiga GL MT : Rp.254,4 Jt/Unit","stok : 7 Unit")
    print("3. Ertiga GL AT : Rp.266,4 Jt/Unit","stok : 7 Unit")
    ertiga = int(input("Ertiga : "))

    if ertiga==1 :
      model_mobil = "Ertiga GA MT"
      harga = 232000000
      stok = 7

    elif ertiga==2 :
      model_mobil = "Ertiga GL MT"
      harga = 254400000
      stok = 7

    else :
      model_mobil = "Ertiga GA AT"
      harga = 232000000
      stok = 7

  elif nomor==2 :
    print("-----------Daftar APV Arena--------------")
    print("1. APV Blind Van 1.5 MT           : Rp.182,3 Jt/Unit","stok : 7 Unit")
    print("2. APV GL MT                      : Rp.230,2 Jt/Unit","stok : 7 Unit")
    print("3. APV New Luxury SGX LUX2 R17-MT : Rp.264,3 Jt/Unit","stok : 7 Unit")
    apv = int(input("APV : "))

    if apv==1 :
      model_mobil = "APV Blind Van 1.5 MT"
      harga = 182300000
      stok = 7

    elif apv==2 :
      model_mobil = "APV Blind Van 1.5 MT"
      harga = 230200000
      stok = 7

    else :
      model_mobil = "APV New Luxury SGX LUX2 R17-MT"
      harga = 264300000
      stok = 7

  elif nomor==3 :
    print("---------Daftar Baleno-----------")
    print("1. Baleno MT : Rp.265,5 Jt/Unit","stok : 4 Unit")
    print("2. Baleno AT : Rp.283,9 Jt/Unit","stok : 4 Unit")
    baleno = int(input("Baleno : "))

    if baleno==1 :
      model_mobil ="Baleno MT"
      harga = 265500000
      stok = 4

    else :
      model_mobil ="Baleno AT"
      harga = 283900000
      stok = 4

  elif nomor==4 :
    print("----------Daftar Grand Vitara--------")
    print("1. Grand Vitara GL          : Rp.362   Jt/Unit","stok : 5 Unit")
    print("2. Grand Vitara GX          : Rp.388,4 Jt/Unit","stok : 5 Unit")
    print("3. Grand Vitara GX Two Tone : Rp.391,4 Jt/Unit","stok : 5 Unit")
    grand = int(input("Grand Vitara : "))

    if grand==1 :
      model_mobil ="Grand Vitara GL"
      harga = 362000000
      stok = 5

    elif grand==2 :
      model_mobil ="Grand Vitara GX"
      harga = 388400000
      stok = 5

    else : 
      model_mobil ="Grand Vitara GX Two Tone"
      harga = 391400000
      stok = 5

  elif nomor==5 :
    print("----------Dafatr Ignis---------")
    print("1. Ignis GX MT : Rp.213,8 Jt/Unit","stok : 6 Unit")
    print("2. Ignis GX AGS : Rp.223,8 Jt/Unit","stok : 6 Unit")
    ignis = int(input("Ignis : "))

    if ignis==1 :
      model_mobil ="Ignis GX MT"
      harga = 213800000
      stok = 6

    else :
      model_mobil ="Ignis GX AGS"
      harga = 223800000
      stok = 6

  elif nomor==6 :
    print("---------Daftar Karimun Wagon R-----------")
    print("1. Karimun Wagon R Blind Van MT : Rp.134,5 Jt/Unit","stok : 6 Unit")
    print("2. Karimun Wagon R GL MT        : Rp.137,7 Jt/Unit","stok : 6 Unit")
    print("3. Karimun Wagon R GL AGS       : Rp.147   Jt/Unit","stok : 6 Unit")
    karimun = int(input("Karimun Wagon R : "))

    if karimun==1 :
      model_mobil ="Karimun Wagon R Blind Van MT"
      harga = 134500000
      stok = 6

    elif karimun==2 :
      model_mobil ="Karimun Wagon R Blind GL MT"
      harga = 137700000
      stok = 6

    else : 
      model_mobil ="Karimun Wagon R GL AGS"
      harga = 147000000
      stok = 6

  else :
    print("-----------Daftar XL7----------")
    print("1. XL7 Zeta MT         : Rp.259,4 Jt/Unit","stok : 4 Unit")
    print("2. XL7 Hybrid Beta MT  : Rp.287,2 Jt/Unit","stok : 4 Unit")
    print("3. XL7 Alpha FF MT     : Rp.294,2 Jt/Unit","stok : 4 Unit")
    print("4. XL7 Hybrid Alpha MT : Rp.297,2 Jt/Unit","stok : 4 Unit")
    xl7 = int(input("XL7 : "))

    if xl7==1 :
      model_mobil ="XL7 Zeta MT"
      harga = 259400000
      stok = 4

    elif xl7==2 :
      model_mobil ="XL7 Hybrid Beta MT"
      harga = 287200000
      stok = 4

    elif xl7==3 :
      model_mobil ="XL7 Alpha FF MT"
      harga = 294200000
      stok = 4

    else :
      model_mobil ="XL7 Hybrid Alpha MT"
      harga = 297200000
      stok = 4

elif merk==3 :
  merk_mobil = "Honda"
  print("----------Daftar Moodel Mobil Honda-----------")
  print("1. Brio           : Rp.167,9 - Rp.253,1 Jt/Unit","stok : 9 Unit")
  print("2. City Hatchback : Rp.352,5 - Rp.382,5 Jt/Unit","stok : 6 Unit")
  print("3. BR-V           : Rp.292,9 - Rp.362,4 Jt/Unit","stok : 6 Unit")
  print("4. WR-V           : Rp.274,9 - Rp.324,1 Jt/Unit","stok : 5 unit")
  print("5. HR-V           : Rp.383,9 - Rp.540,3 Jt/Unit","stok : 7 Unit")
  print("6. CR-V           : Rp.749,1 - Rp.814,4 Jt/Unit","stok : 5 Unit")
  print("7. Civic          : Rp.512,8Jt - Rp.1,4 M/Unit","stok : 8 Unit")
  nomor = int(input("Masukkan Nomor : "))

  if nomor==1 :
    print("-------Daftar Brio--------")
    print("1. Brio Satya S MT              : Rp.167,9 Jt/Unit","stok : 9 Unit")
    print("2. Brio Satya E CVT             : Rp.198,3 Jt/Unit","stok : 9 Unit")
    print("3. Brio RS MT Urbanite Edition  : Rp.233,9 Jt/Unit","stok : 9 Unit")
    print("4. Brio RS CVT Urbanite Edition : Rp.243,9 Jt/Unit","stok : 9 Unit")
    brio = int(input("Brio : "))

    if brio==1 :
      model_mobil ="Brio Satya S MT"
      harga = 167900000
      stok = 9

    elif brio==2 :
      model_mobil ="Brio Satya E CVT"
      harga = 198300000
      stok = 9

    elif brio==3 :
      model_mobil ="Brio RS MT Urbanite Edition"
      harga = 233900000
      stok = 9

    else :
      model_mobil ="Brio RS CVT MT Urbanite Edition"
      harga = 243900000
      stok = 9

  if nomor==2 :
    print("----------Daftar City Hatchback---------")
    print("1. City Hatchback RS MT                     : Rp.352,5 Jt/Unit","stok : 6 Unit")
    print("2. City Hatchback RS CVT                    : Rp.362,5 Jt/Unit","stok : 6 Unit")
    print("3. City Hatchback RS CVT with Honda Sensing : Rp.382,5 Jt/Unit","stok : 6 Unit")
    city = int(input("City Hatchback : "))

    if city==1 : 
      model_mobil ="City Hatchback RS MT"
      harga = 352500000
      stok = 6

    elif city==2 : 
      model_mobil ="City Hatchback RS CVT"
      harga = 362500000
      stok = 6

    else :
      model_mobil ="City Hatchback RS CVT with Honda Sensing"
      harga = 382500000
      stok = 6

  elif nomor==3 :
    print("---------Daftar BR-V------------")
    print("1. BR-V S MT                            : Rp.292,9 Jt/Unit","stok : 6 Unit")
    print("2. BR-V E CVT                           : Rp.318,4 Jt/Unit","stok : 6 Unit")
    print("3. BR-V Prestige CVT                    : Rp.342,4 Jt/Unit","stok : 6 Unit")
    print("4. BR-V Prestige CVT with Honda Sensing : Rp.362,4 Jt/Unit","stok : 6 Unit")
    brv = int(input("BR-V : "))

    if brv==1 :
      model_mobil ="BR-V S MT"
      harga = 292900000
      stok = 6

    elif brv==2 :
      model_mobil ="BR-V E CVT"
      harga = 318400000
      stok = 6

    elif brv==2 :
      model_mobil ="BR-V Prestige CVT"
      harga = 342400000
      stok = 6

    else : 
      model_mobil ="BR-V Prestigeb CVT with Honda Sensing"
      harga = 362400000
      stok = 6

  elif nomor==4 :
    print("---------Daftar WR-V---------")
    print("1. WR-V 1.5L E MT                  : Rp.274,9 Jt/Unit","stok : 5 Unit")
    print("2. WR-V 1.5L RS                    : Rp.304,1 Jt/Unit","stok : 5 Unit")
    print("3. WR-V 1.5L RS with Honda Sensing : Rp.324,1 Jt/Unit","stok : 5 Unit")
    wrv = int(input("WR-V : "))

    if wrv==1 :
      model_mobil ="WR-V 1.5L E MT"
      harga = 274900000
      stok = 5

    elif wrv==2 :
      model_mobil ="WR-V 1.5L RS"
      harga = 304100000
      stok = 5

    else :
      model_mobil ="WR-V 1.5L RS with Honda Sensing"
      harga = 324100000
      stok = 5

  elif nomor==5 :
    print("-----------Daftar HR-V-----------")
    print("1. HR-V S CVT    : Rp.383,9 Jt/Unit","stok : 7 Unit")
    print("2. HR-V E CVT    : Rp.404,2 Jt/Unit","stok : 7 Unit")
    print("3. HR-V SE CVT   : Rp.424,6 Jt/Unit","stok : 7 Unit")
    print("4. HR-V Turbo RS : Rp.540,3 Jt/Unit","stok : 7 Unit")
    hrv = int(input("HR-V : "))

    if hrv==1 :
      model_mobil ="HR-V S CVT"
      harga = 383900000
      stok = 7

    elif hrv==2 :
      model_mobil ="HR-V E CVT"
      harga = 404200000
      stok = 7

    elif hrv==3 :
      model_mobil ="HR-V SE CVT"
      harga = 424600000
      stok = 7

    else : 
      model_mobil ="HR-V Turbo RS"
      harga = 540300000
      stok = 7

  elif nomor==6 : 
    print("------------Daftar CR-V-------------")
    print("1. CR-V 15L DOHC VTEC Turbo : Rp.749,1 Jt/Unit","stok : 5 Unit")
    print("2. CR-V 20L RS eHEV         : Rp.814,4 Jt/Unit","stok : 5 Unit")
    crv = int(input("CR-V : "))

    if crv==1 :
      model_mobil ="CR-V 15L DOHC VTEC Turbo"
      harga = 749100000
      stok = 5

    else :
      model_mobil ="CR-V 20L RS eHEV"
      harga = 814400000
      stok = 5

  else :
    print("--------Daftar Civic----------")
    print("1. Civic Hatchback RS      : Rp.512,8 Jt/Unit","stok : 8 Unit")
    print("2. Civic RS                : Rp.616,8 Jt/Unit","stok : 8 Unit")
    print("3. Civic Type R 6 Speed MT : Rp.1,427 M/Unit","stok : 8 Unit")
    civic = int(input("Civic : "))

    if civic==1 :
      model_mobil ="Civic Hatchback RS"
      harga = 512800000
      stok = 8

    elif civic==2 :
      model_mobil ="Civic RS"
      harga = 616800000
      stok = 8

    else :
      model_mobil ="Civic Type R 6 Speed MT"
      harga = 1427000000
      stok = 8

elif merk==4 :
  merk_mobil = "Daihatsu"
  print("--------------Daftar Model Mobil Daihatsu----------")
  print("1. Ayla       : Rp.136    - Rp..191,9 Jt/Unit","stok : 9 Unit")
  print("2. Sigra      : Rp.139    - Rp.182,6  Jt/Unit","stok : 7 Unit")
  print("3. Sirion     : Rp.230,35 - Rp.239,55 Jt/Unit","stok : 6 Unit")
  print("4. Xenia      : Rp.222,65 - Rp.279,85 Jt/Unit","stok : 9 Unit")
  print("5. Terios     : Rp.241,55 - Rp.307,55 Jt/Unit","stok : 7 Unit")
  print("6. Grand Max  : Rp.205,25 - Rp.225,85 Jt/Unit","stok : 4 Unit")
  nomor = int(input("Masukkan Nomor : "))

  if nomor==1 : 
    print("------Daftar Mobil Ayla-------")
    print("1. Ayla 1.0 M : Rp.136 Jt/Unit","stok : 9 Unit")
    print("2. Ayla 1.2 R MT : Rp.166 Jt/Unit","stok : 9 Unit")
    print("3. Ayla X CVT ADS : Rp.174,8 Jt/Unit","stok : 9 Unit")
    print("4. Ayla 1.2 R CVT ADS : Rp.191,9 Jt/Unit","stok : 9 Unit")
    ayla = int(input("Ayla : "))

    if ayla==1 :
      model_mobil ="Ayla 1.0 M"
      harga = 136000000
      stok = 9

    elif ayla==2 :
      model_mobil ="Ayla 1.2 R MT"
      harga = 166000000
      stok = 9

    elif ayla==3 :
      model_mobil ="Ayla X CVT ADS"
      harga = 174800000
      stok = 9

    else :
      model_mobil ="Ayla 1.2 R CVT ADS"
      harga = 191900000
      stok = 9

  if nomor==2 :
    print("-----------Daftar Sigra-------")
    print("1. Sigra 1.0 D MT : Rp.139 Jt/Unit","stok : 7 Unit")
    print("2. Sigra 1.2 X MT : Rp.157,3 Jt/Unit","stok : 7 Unit")
    print("3. Sigra 1.2 X AT DLX : Rp.176,1 Jt/Unit","stok : 7 Unit")
    print("4. Sigra 1.2 R AT DLX : Rp.182,6 Jt/Unit","stok : 7 Unit")
    sigra = int(input("Sigra : "))

    if sigra==1 :
      model_mobil ="Sigra 1.0 D MT"
      harga = 139000000
      stok = 7

    elif sigra==2 :
      model_mobil ="Sigra 1.2 X MT"
      harga = 157300000
      stok = 7

    elif sigra==3 :
      model_mobil ="Sigra 1.2 X AT DLX"
      harga = 176100000
      stok = 7

    else :
      model_mobil ="Sigra 1.2 R AT DLX"
      harga = 182600000
      stok = 7

  elif nomor==3 :
    print("-----------Daftar Sirion--------")
    print("1. Sirion X CVT : Rp.230,35 Jt/Unit","stok : 6 Unit")
    print("2. Sirion R CVT : Rp.239,55 Jt/Unit","stok : 6 Unit")
    sirion = int(input("Sirion : "))

    if sirion==1 :
      model_mobil ="Sirion X CVT"
      harga = 230350000
      stok = 6

    else :
      model_mobil ="Sirion R CVT"
      harga = 239550000
      stok = 6

  elif nomor==4 :
    print("----------Daftar Xenia----------")
    print("1. Xenia 1.3 M MT : Rp.222,65 Jt/Unit","stok : 9 Unit")
    print("2. Xenia 1.5 R MT SC : Rp.255,05 Jt/Unit","stok : 9 Unit")
    print("3. Xenia 1.5 R CVT : Rp.268,45 Jt/unit","stok : 9 Unit")
    print("4. Xenia 1.5 R CVT ASA SC : Rp.279,85 Jt/Unit","stok : 9 Unit")
    xenia = int(input("Xenia : "))

    if xenia==1 :
      model_mobil ="Xenia 1.3 M MT"
      harga = 222650000
      stok = 9

    elif xenia==2 :
      model_mobil ="Xenia 1.5 R MT"
      harga = 255050000
      stok = 9

    elif xenia==3 :
      model_mobil ="Xenia 1.5 R CVT"
      harga = 268450000
      stok = 9

    else :
      model_mobil ="Xenia 1.5 R CVT ASA SC"
      harga = 279850000
      stok = 9

  elif nomor==5 :
    print("--------Daftar Terios---------")
    print("1. Terios X MT        : Rp.241,55 Jt/Unit","stok : 7 Unit")
    print("2. Terios R AT        : Rp.284,95 Jt/Unit","stok : 7 Unit")
    print("3. Terios R Custom MT : Rp.297,25 Jt/Unit","stok : 7 Unit")
    print("4. Terios R Custom AT : Rp.307,75 Jt/Unit","stok : 7 Unit")
    terios = int(input("Terios : "))

    if terios==1 :
      model_mobil ="Terios X MT"
      harga = 241550000
      stok = 7

    elif terios==2 :
      model_mobil ="Terios R AT"
      harga = 284950000
      stok = 7

    elif terios==3 :
      model_mobil ="Terios R Custom MT"
      harga = 297250000
      stok = 7

    else : 
      model_mobil ="Terios R Custom AT"
      harga = 307750000
      stok = 7

  else :
    print("-------Daftar Gran Max----------")
    print("1. Gran Max MB 1.3 D FH    : Rp.205,25 Jt/Unit","stok : 4 Unit")
    print("2. Gran Max MB 1.3 D FF FH : Rp.212,05 Jt/Unit","stok : 4 Unit")
    print("3. Gran Max MB 1.5 D PS FH : Rp.225,85 Jt/Unit","stok : 4 Unit")
    gran = int(input("Gran Max : "))

    if gran==1 : 
      model_mobil ="Gran Max MB 1.3 D FH "
      harga = 205250000
      stok = 4

    elif gran==2 : 
      model_mobil ="Gran Max MB 1.3 D FF FH"
      harga = 212050000
      stok = 4

    else :
      model_mobil ="Gran Max MB 1.3 D PS FH "
      harga = 225850000
      stok = 4

elif merk==5 :
  merk_mobil = "Wuling"
  print("--------Daftar Model Mobil Wuling----------")
  print("1. Air EV    : Rp.179,1 - Rp.275    Jt/Unit","stok : 9 Unit")
  print("2. Formo     : Rp.152,7 - Rp.169,6  Jt/Unit","stok : 6 Unit")
  print("3. Cortez    : Rp.263,5 - Rp.342,65 Jt/Unit","stok : 6 Unit")
  print("4. Alvez     : Rp.214   - Rp.300    Jt/Unit","stok : 7 Unit")
  print("5. BinguoEV  : Rp.326   - Rp.372    Jt/Unit","stok : 6 Unit")
  print("6. Almaz     : Rp.303,5 - Rp.438    Jt/Unit","stok : 7 Unit")
  nomor = int(input("Masukkan Nomor : "))

  if nomor==1 :
    print("---------Daftar Air EV---------")
    print("1. Air EV Lite Standart Range : Rp.179,1 Jt/Unit","stok : 9 Unit")
    print("2. Air Ev Lite Long Range     : Rp.190   Jt/Unit","stok : 9 Unit")
    print("3. Air EV Standart Range      : Rp.224   Jt/Unit","stok : 9 Unit")
    print("4. Air EV Long Range          : Rp.275   Jt/Unit","stok : 9 Unit")
    air = int(input("Air EV : "))

    if air==1 :
      model_mobil ="Air EV Lite Standart Range"
      harga = 179100000
      stok = 9

    elif air==2 :
      model_mobil ="Air EV Lite Long Range"
      harga = 190000000
      stok = 9

    elif air==3 :
      model_mobil ="Air EV Standart Range"
      harga = 224000000
      stok = 9

    else :
      model_mobil ="Air EV Long Range"
      harga = 275000000
      stok = 9

  elif nomor==2 :
    print("---------Daftar Formo----------")
    print("1. Formo 1.2 BV MT  : Rp.152,7 Jt/Unit","stok : 6 Unit")
    print("2. Formo S 5-Seater : Rp.164,8 Jt/Unit","stok : 6 Unit")
    print("3. Formo S 8-Seater : Rp.169,6 Jt/Unit","stok : 6 Unit")
    formo = int(input("Formo : "))

    if formo==1 :
      model_mobil ="Formo 1.2 BV MT"
      harga = 152700000
      stok = 6

    elif formo==2 :
      model_mobil ="Formo S 5-Seater"
      harga = 164800000
      stok = 6

    else :
      model_mobil ="Formo 1.2 BV MT"
      harga = 152700000
      stok = 6

  elif nomor==3 :
    print("----------Daftar Cortez-----------")
    print("1. Cortez S 1.5T MT Lux Plus   : Rp.263,5  Jt/Unit","stok : 6 Unit")
    print("2. Cortez 1.5S Plus T CVT      : Rp.285,2  Jt/Unit","stok : 6 Unit")
    print("3. Cortez EX 1.5T Lux Plus CVT : Rp.342,65 Jt/Unit","stok : 6 Unit")
    cortez = int("Cortez : ")

    if cortez==1 :
      model_mobil ="Cortez S 1.5T MT Lux Plus"
      harga = 263500000
      stok = 6

    elif cortez==2 :
      model_mobil ="Cortez 1.5S Plus T CVT"
      harga = 285200000
      stok = 6

    else : 
      model_mobil ="Cortez EX 1.5T Lux Plus CVT"
      harga = 342650000
      stok = 6

  elif nomor==4 :
    print("----------Daftar Alvez-------------")
    print("1. Alvez SE  : Rp.214 Jt/Unit","stok : 7 Unit")
    print("2. Alvez CE  : Rp.260 Jt/Unit","stok : 7 Unit")
    print("3. Alvez EX  : Rp.300 Jt/Unit","stok : 7 Unit")
    alvez = int(input("Alvez : "))

    if alvez==1 :
      model_mobil ="Alvez SE"
      harga = 214000000
      stok = 7

    elif alvez==2 :
      model_mobil ="Alvez CE"
      harga = 260000000
      stok = 7

    else :
      model_mobil ="Alvez EX"
      harga = 300000000
      stok = 7

  elif nomor==5 :
    print("----------Daftar BinguoEV--------------")
    print("1. BinguoEV Long Range 333km    : Rp.326 Jt/Unit","stok : 6 Unit")
    print("2. BinguoEV Premium Range 410km : Rp.372 Jt/Unit","stok : 6 Unit")
    binguo = int(input("BinguoEV : "))

    if binguo==1 :
      model_mobil ="Binguo Long Range 333km"
      harga = 326000000
      stok = 6

    else :
      model_mobil ="Binguo Premium Range 410km"
      harga = 372000000
      stok = 6

  else :
    print("-------------Daftar Almaz-----------")
    print("1. Almaz Smart Enjoy 6 MT 7 Sealer    : Rp.303,5 Jt/Unit","stok : 7 Unit")
    print("2. Almaz Smart Exclusive CVT 7 Seater : Rp.385,8 Jt/Unit","stok : 7 Unit")
    print("3. Almaz RS Pro                       : Rp.402   Jt/Unit","stok : 7 Unit")
    print("4. Almaz RS Pro Hybrid                : Rp.442   Jt/Unit","stok : 7 Unit")
    almaz = int(input("Almaz : "))

    if almaz==1 :
      model_mobil ="Almaz Smart Enjoy 6 MT 7 Seater"
      harga = 303500000
      stok = 7

    elif almaz==2 :
      model_mobil ="Almaz Smart EXclusive CVT 7 Seater"
      harga = 385800000
      stok = 7

    elif almaz==3 :
      model_mobil ="Almaz RS Pro"
      harga = 402000000
      stok = 7

    else : 
      model_mobil ="Almaz RS Pro Hybrid"
      harga = 442000000
      stok = 7

elif merk==6 :
  merk_mobil = "Mitsubishi"
  print("----------Daftar Model Mobil Mitshubishi------------")
  print("1. Xpander       : Rp.263    - Rp.322,9 Jt/Unit","stok : 9 Unit")
  print("2. XForce        : Rp.381,9  - Rp.414,9 Jt/Unit","stok : 7 Unit")
  print("3. Pajero Sport  : Rp.567,1  - Rp.764,2 Jt/Unit","stok : 7 Unit")
  nomor = int(input("Masukkan Nomor : "))

  if nomor==1 :
    print("--------Daftar Xpander---------")
    print("1. Xpander GLS MT       : Rp.263,2  Jt/Unit","stok : 9 Unit")
    print("2. Xpander Exceed CVT   : Rp.285,7  Jt/Unit","stok : 9 Unit")
    print("3. Xpander Sport MT     : Rp.299,85 Jt/Unit","stok : 9 Unit")
    print("4. Xpander Ultimate CVT : Rp.322,9  Jt/Unit","stok : 9 Unit")
    xpander = int(input("Xpander : "))

    if xpander==1 :
      model_mobil ="Xpander GLS MT"
      harga = 263200000
      stok = 9

    elif xpander==2 :
      model_mobil ="Xpander Exceed CVT"
      harga = 285700000
      stok = 9

    elif xpander==1 :
      model_mobil ="Xpander Sport MT"
      harga = 299850000
      stok = 9

    else :
      model_mobil ="Xpander Ultimate CVT"
      harga = 322900000
      stok = 9

  elif nomor==2 :
    print("-----------Daftar XForce------------")
    print("1. XForce Exceed CVT : Rp.381,9 Jt/Unit","stok : 7 Unit")
    print("2. XForce Ultimate CVT : Rp.414,9 Jt/Unit","stok : 7 Unit")
    xforce = int(input("XForce : "))

    if xforce==1 :
      model_mobil ="XForce Exceed CVT"
      harga = 381900000
      stok = 7

    else :
      model_mobil ="XForce Ultimate CVT"
      harga = 414900000
      stok = 7

  else :
    print("---------Daftar Pajero Sport--------")
    print("1. Pajero Sport GLX 4x4 MT : Rp.593,1 Jt/Unit","stok : 7 Unit")
    print("2. Pajero Sport Dakar 4x2 AT : Rp.650,7 Jt/Unit","stok : 7 Unit")
    print("3. Pajero Sport Dakar Ultimate 4x2 AT : Rp.703,1 Jt/Unit","stok : 7 Unit")
    print("4. Pajero Sport Daka Ultimate 4x4 AT : Rp.764,2 Jt/Unit","stok : 7 Unit")
    pajero = int(input("Pajero Sport : "))

    if pajero==1 :
      model_mobil ="Pajero Sport GLX 4x4 MT"
      harga = 593100000
      stok = 7

    elif pajero==2 :
      model_mobil ="Pajero Sport Dakar 4x2 AT"
      harga = 650700000
      stok = 7

    elif pajero==3 :
      model_mobil ="Pajero Sport Dakar Ultimate 4x2 AT"
      harga = 703100000
      stok = 7

    else :
      model_mobil ="Pajero Sport Dakar Ultimate 4x4 AT"
      harga = 764200000
      stok = 7

elif merk==7 :
  merk_mobil = "Hyundai"
  print("-----------Daftar Model Mobil Hyundai---------")
  print("1. Creta         : Rp.297,3 - Rp.421,8 Jt/Unit","stok : 9 Unit")
  print("2. Stargazer X   : Rp.335,8 - Rp.346,4 Jt/Unit","stok : 7 Unit")
  print("3. Tucson        : Rp.471   - Rp.523   Jt/Unit","stok : 6 Unit")
  print("4. Kona Electric : Rp.499   - Rp.590   Jt/Unit","stok : 6 Unit")
  print("5. Ioniq 5       : Rp.713   - Rp.902,4 Jt/Unit","stok : 5 Unit")
  print("6. Staria        : Rp.924Jt - Rp.1,06  M/Unit","stok : 4 Unit")
  print("7. Palisade      : Rp.910Jt - Rp.1,215 M/Unit","stok : 3 Unit")
  nomor = int(input("Masukkan Nomor : "))

  if nomor==1 :
    print("-------------Daftar Creta----------")
    print("1. Creta Active 6-Speed MT     : Rp.297,3 Jt/Unit","stok : 9 Unit")
    print("2. Creta Dynamic Black Edition : Rp.350 Jt/Unit","stok : 9 Unit")
    print("3. Creta Alpha                 : Rp.421,8 Jt/Unit","stok : 9 Unit")
    creta = int(input("Creta : "))

    if creta==1 :
      model_mobil ="Creta Active 6-Speed MT"
      harga = 297300000
      stok = 9

    elif creta==2 :
      model_mobil ="Creta Dynamic Black Edition"
      harga = 350000000
      stok = 9

    else :
      model_mobil ="Creta Alpha"
      harga = 421800000
      stok = 9

  elif nomor==2 :
    print("----------Daftar Stargazer X-------------")
    print("1. Stargazer X Style IVT : Rp.335,8 Jt/Unit","stok : 7 Unit")
    print("2. Stargazer X Prime IVT : Rp.346,4 Jt/Unit","stok : 7 Unit")
    stargazer = int(input("Stargazer X : "))

    if stargazer==1 :
      model_mobil ="Stargazer X Style IVT"
      harga = 335800000
      stok = 7

    else :
      model_mobil ="Stargazer X Prime IVT"
      harga = 346400000
      stok = 7

  elif nomor==3 :
    print("----------Daftar Tucson---------")
    print("1. Tucson GLS 2.0 Gasoline : Rp.471 Jt/Unit","stok : 6 Unit")
    print("2. Tucson CRDi GLS         : Rp.523 Jt/Unit","stok : 6 Unit")
    tucson = int(input("Tucson : "))

    if tucson==1 :
      model_mobil ="Tucson GLS 2.0 Gasoline"
      harga = 471000000
      stok = 6

    else :
      model_mobil ="Tucson CRDi GLS"
      harga = 523000000
      stok = 6

  elif nomor==4 :
    print("---------Daftar Kona Electric------------")
    print("1. Kona Style Standard Range     : Rp.499 Jt/Unit","stok : 6 Unit")
    print("2. Kona Prime Long Range         : Rp.560 Jt/Unit","stok : 6 Unit")
    print("3. Kona Signature Standard Range : Rp.575 Jt/Unit","stok : 6 Unit")
    print("4. Kona Signature Long Range     : Rp.590 Jt/Unit","stok : 6 Unit")
    kona = int(input("Kona Electric : "))

    if kona==1 :
      model_mobil ="Kona Style Standard Range"
      harga = 499000000
      stok = 6

    elif kona==2 :
      model_mobil ="Kona Prime Long Range"
      harga = 560000000
      stok = 6

    elif kona==3 :
      model_mobil ="Kona Signature Standard Range"
      harga = 575000000
      stok = 6

    else :
      model_mobil ="Kona Signature Long Range"
      harga = 590000000
      stok = 6

  elif nomor==5 :
    print("--------Daftar Ioniq 5-------------")
    print("1. Ioniq 5 Prime Standard Range : Rp.713   Jt/Unit","stok : 5 Unit")
    print("2. Ioniq 5 Prime Long Range     : Rp.750,4 Jt/Unit","stok : 5 Unit")
    print("3. Ioniq 5 Batik                : Rp.902,4 Jt/Unit","stok : 5 Unit")
    ioniq = int(input("Ioniq 5 : "))

    if ioniq==1 :
      model_mobil ="Ioniq 5 Prime Standard Range"
      harga = 713000000
      stok = 5

    elif ioniq==2 :
      model_mobil ="Ioniq 5 Prime Long Range"
      harga = 750400000
      stok = 5

    else :
      model_mobil ="Ioniq 5 Batik"
      harga = 902400000
      stok = 5

  elif nomor==6 : 
    print("-------------Daftar Staria----------")
    print("1. Staria Signature 9 : Rp.924 Jt/Unit","stok : 4 Unit")
    print("2. Staria Signature 7 : Rp.1,06 M/Unit","stok : 4 Unit")
    staria = int(input("Staria : "))

    if staria==1 :
      model_mobil ="Staria Signature 9"
      harga = 924000000
      stok = 4

    else :
      model_mobil ="Staria Signature 7"
      harga = 1060000000
      stok = 4

  else :
    print("-----------Daftar Palisade----------")
    print("1. Palisade Prime             : Rp.910 Jt/Unit","stok : 3 Unit")
    print("2. Palisade Signature 4WD     : Rp.1,187 M/Unit","stok : 3 Unit")
    print("3. Palisade Signature 4WD XRT : Rp.1,215 M/Unit","stok : 3 Unit")
    palisade = int(input("Palisade : "))

    if palisade==1 :
      model_mobil ="Palisade Prime"
      harga = 910000000
      stok = 3

    elif palisade==2 :
      model_mobil ="Palisade Signature 4WD"
      harga = 1187000000
      stok = 3

    else :
      model_mobil ="Palisade Signature 4WD XRT"
      harga = 1215000000
      stok = 3

elif merk==8 :
  merk_mobil = "Subaru"
  print("-------Daftar Model Mobil Subaru-------")
  print("1. Forester  : Rp.579,5   - Rp.659,5 Jt/Unit","stok : 7 Unit")
  print("2. WRX       : Rp.874,5   - Rp.959,5 Jt/Unit","stok : 5 Unit")
  print("3. BR-Z      : Rp.885     - Rp.895   Jt/Unit","stok : 5 Unit")
  print("4. WRX Wagon : Rp.975,5Jt - Rp.1,029 M/Unit","stok : 4 Unit")
  nomor = int(input("Masukkan Nomor : "))

  if nomor==1 : 
    print("----------Daftar Forester----------")
    print("1. Forester 2.0i L : Rp.579,5 Jt/Unit","stok : 7 Unit")
    print("2. Forester 2.0i S-Eyesight : Rp.659,5 Jt/Unit","stok : 7 Unit")
    forester = int(input("Forester : "))

    if forester==1 :
      model_mobil ="Forester 2.0i L"
      harga = 579500000
      stok = 7

    else : 
      model_mobil ="Forester 2.0i S-Eyesight"
      harga = 659500000
      stok = 7

  elif nomor==2 :
    print("----------Daftar WRX------------")
    print("1. WRX MT          : Rp.874,5 Jt/Unit","stok : 5 Unit")
    print("2. WRX TS Eyesight : Rp.959,5 Jt/Unit","stok : 5 Unit")
    wrx = int(input("WRX : "))

    if wrx==1 :
      model_mobil ="WRX MT"
      harga = 874500000
      stok = 5

    else : 
      model_mobil ="WRX TS Eyesight"
      harga = 959500000
      stok = 5

  elif nomor==3 :
    print("---------Daftar BR-Z-----------")
    print("1. BR-Z MT : Rp.885 Jt/Unit","stok : 5 Unit")
    print("2. BR-Z AT : Rp.895 Jt/Unit","stok : 5 Unit")
    brz = int(input("BR-Z : "))

    if brz==1 :
      model_mobil ="BR-Z MT"
      harga = 885000000
      stok = 5

    else :
      model_mobil ="BR-Z AT"
      harga = 895000000
      stok = 5

  else : 
    print("--------Daftar WRX Wagon-------------")
    print("1. WRX Wagon GT-S EyeSight : Rp.975,5 Jt/Unit","stok : 4 Unit")
    print("2. WRX Wagon TS EyeSight   : Rp.1,025 M/Unit","stok : 4 Unit")
    wrxwagon = int(input("WRX Wagon : "))

    if wrxwagon==1 :
      model_mobil ="WRX Wagon GT-S EyeSight"
      harga = 975500000
      stok = 4

    else :
      model_mobil ="WRX Wagon TS EyeSight"
      harga = 1025000000
      stok = 4

elif merk==9 :
  merk_mobil = "Lexus"
  print("-------Daftar Model Model Mobil Lexus------------")
  print("1. ES 300h         : Rp.1,205 M/Unit","stok : 3 Unit")
  print("2. NX 350h F Sport : Rp.1,454 M/Unit","stok : 3 Unit")
  print("3. RX 450h Luxury  : Rp.1,87  M/Unit","stok : 3 Unit")
  print("4. UX 300e         : Rp.1,464 M/Unit","stok : 3 Unit")
  print("5. LX 600 VIP      : Rp.3,598 M/Unit","stok : 2 Unit")
  nomor = int(input("Masukkan Nomor : "))

  if nomor==1 :
    model_mobil ="ES 300h"
    harga = 1205000000
    stok = 3

  elif nomor==2 :
    model_mobil ="NX 350h F Sport"
    harga = 1454000000
    stok = 3

  elif nomor==3 :
    model_mobil ="RX 450h Luxury"
    harga = 1870000000
    stok = 3

  elif nomor==4 :
    model_mobil ="UX 300e"
    harga = 1464000000
    stok = 3

  else :
    model_mobil ="LX 600 VIP"
    harga = 3598000000
    stok = 2

elif merk==10 :
  merk_mobil = "Mazda"
  print("--------Daftar Model Mobil Mazda-------------")
  print("1. CX-3 : Rp.399,9   - Rp.495,5 Jt/Unit","stok : 7 Unit")
  print("2. CX-5 : Rp.647,7   - Rp.689,9 Jt/Unit","stok : 5 Unit")
  print("3. CX-9 : Rp.955,5Jt - Rp.1,035 M/Unit","stok : 4 Unit")
  print("4. CX-60 : Rp.799Jt  - Rp.1,188 M/Unit","stok : 4 Unit")
  nomor = int(input("Masukkan Nomer : "))

  if nomor==1 :
    print("--------Daftar CX-3------------")
    print("1. CX-3 1.5L Sport : Rp.399,9 Jt/Unit","stok : 7 Unit")
    print("2. CX-3 2.0L PRO   : Rp.495,5 Jt/Unit","stok : 7 Unit")
    cx3 = int(input("CX-3 : "))

    if cx3==1 :
      model_mobil ="CX-3 1.5L Sport"
      harga = 399900000
      stok = 7

    else :
      model_mobil ="CX-3 2.0L PRO"
      harga = 495500000
      stok = 7

  elif nomor==2 :
    print("----------Daftar CX-5----------")
    print("1. CX-5 Kuro AWD                : Rp.689,9 Jt/Unit","stok : 5 Unit")
    print("2. CX-5 AWD Anniversary Edition : Rp.705,5 Jt/Unit","stok : 5 Unit")
    cx5 = int(input("CX-5 : "))

    if cx5==1 :
      model_mobil ="CX-5 Kuro AWD"
      harga = 689900000
      stok = 5

    else : 
      model_mobil ="CX-5 AWD Anniversary Edition"
      harga = 705500000
      stok = 5

  elif nomor==3 :
    print("----------Daftar CX-9----------")
    print("1. CX-9 2WD : Rp.955,5 Jt/Unit","stok : 4 Unit")
    print("2. CX-9 AWD : Rp.1,035 M/Unit","stok : 4 unit")
    cx9 = int(input("CX-9 : "))

    if cx9==1 :
      model_mobil ="CX-9 2WD"
      harga = 955500000
      stok = 4

    else :
      model_mobil ="CX-9 AWD"
      harga = 1035000000
      stok = 4

  else :
    print("---------Daftar CX-60------------")
    print("1. CX-60 Pro    : Rp.799   Jt/Unit","stok : 4 Unit")
    print("2. CX-60 Ellite : Rp.1,188 M/Unit","stok : 4 Unit")
    cx60 = int(input("CX-60 : "))

    if cx60==1 :
      model_mobil ="CX-60 Pro"
      harga = 799000000
      stok = 4

    else :
      model_mobil ="CX-60 Ellite"
      harga = 1188000000
      stok = 4

elif merk==11 :
  merk_mobil = "Mercedez-Benz"
  print("-----------Daftar Model Mobil Mercedez-Benz-----------")
  print("1. V-Class        : Rp.977Jt - Rp.1,599 M/Unit","stok : 4 Unit")
  print("2. C 300          : Rp.1,255 - Rp.1,365 M/Unit","stok : 3 Unit")
  print("3. EQS 450        : Rp.2,984 - 3,41     M/Unit","stok : 3 Unit")
  print("4. Maybach S      : Rp.6,735 - Rp.7,1   M/Unit","stok : 2 unit")
  print("5. AMG GT R Coupe : Rp.7,165 M/Unit","stok : 2 Unit")
  nomor = int(input("Masukkan Nomor : "))

  if nomor==1 : 
    print("--------Daftar V-Class----------")
    print("1. Vito Select : Rp.977 Jt/Unit","stok : 4 Unit")
    print("2. V 260 LWB : Rp.1,599 M/Unit","stok : 4 Unit")
    v = int(input("V-Class : "))

    if v==1 :
      model_mobil ="Vito Select"
      harga = 977000000
      stok = 4

    else :
      model_mobil ="V 260 LWB"
      harga = 1599000000
      stok = 4

  elif nomor==2 :
    print("---------Daftar C 300----------")
    print("1. C 300 Coupe AMG Line : Rp.1,365 M/Unit","stok : 3 Unit")
    print("2. C 300 AMG Line : Rp.1,255 M/Unit","stok : 3 Unit")
    c300 = int(input("C 300 : "))

    if c300==1 :
      model_mobil ="C 300 Coupe AMG Line"
      harga = 1365000000
      stok = 3

    else :
      model_mobil ="C 300 AMG Line"
      harga = 1255000000
      stok = 3

  elif nomor==3 :
    print("-------Daftar EQS 450-----------")
    print("1. EQS 450 Plus Electric Art Line : Rp.2,984 M/Unit","stok : 3 Unit")
    print("2. EQS 450 Plus AMG Line          : Rp.3,41  M/Unit","stok : 3 Unit")
    eqs = int(input("EQS 450 : "))

    if eqs==1 :
      model_mobil ="EQS 450 Plus Electric Art Line"
      harga = 2984000000
      stok = 3

    else :
      model_mobil ="EQS 450 Plus Electric Art Line"
      harga = 3410000000
      stok = 3

  elif nomor==4 :
    print("------------Daftar Maybach S-----------")
    print("1. Maybach S 560 FL : Rp.6,735 M/Unit","stok : 2")
    print("2. Maybach S 650 FL : Rp.7,1 M/Unit","stok : 2 Unit")
    maybach = int(input("Maybach S : "))

    if maybach==1:
      model_mobil ="Maybach S 560 FL"
      harga = 6735000000
      stok = 2

    else :
      model_mobil ="Maybach S 650 FL"
      harga = 7100000000
      stok = 2

  else :
    model_mobil ="AMG GT R Coupe"
    harga = 7165000000
    stok = 2

elif merk==12 :
  merk_mobil = "Nissan"
  print("--------Daftar Model Mobil Nissan-----------")
  print("2. Livina  : Rp.292,5  - Rp.327   Jt/Unit","stok : 7 Unit")
  print("3. Serena  : Rp.465,15 - Rp.560,8 Jt/Unit","stok : 5 Unit")
  nomor = int(input("Masukkan Nomor : "))

  if nomor==1 :
    print("-------Daftar Livina---------")
    print("1. Livina 1.5 EL MT : Rp.292,5 Jt/Unit")
    print("2. Livina 1.5 VE AT : Rp.316,5 Jt/Unit")
    print("3. Livina 1.5 VL AT : Rp.327 Jt/Unit")
    livina = int(input("Livina : "))

    if livina==1 :
      model_mobil ="Livina 1.5 EL MT"
      harga = 292500000
      stok = 7

    elif livina==2 :
      model_mobil ="Livina 1.5 VE AT"
      harga = 316500000
      stok = 7

    else : 
      model_mobil ="Livina 1.5 VL MT"
      harga = 327000000
      stok = 7

  else :
    print("-------Daftar Serena----------")
    print("1. Serena 2.0 X            : Rp.465,15 Jt/Unit")
    print("2. Serena 2.0 Highway Star : Rp.560,8  Jt/Unit")
    serena = int(input("Serena : "))

    if serena==1 :
      model_mobil ="Serena 2.0 X"
      harga = 465150000
      stok = 5

    else :
      model_mobil ="Serena 2.0 Highay Star"
      harga = 560800000
      stok = 5

elif merk==13 :
  merk_mobil = "BMW"
  print("-----Daftar Model Mobil BMW---------")
  print("1. X      : Rp.985Jt - Rp.2,774 M/Unit","stok : 4 Unit")
  print("2. I      : Rp.1,319 - Rp.3,33  M/Unit","stok : 4 unit")
  print("3. Series : Rp.1,864 - Rp.3,033 M/Unit","stok : 4 Unit")
  print("4. M      : Rp.2,2   - Rp.6,857 M/unit","stok : 2 Unit")
  nomor = int(input("Masukkan Nomor : "))

  if nomor==1 :
    print("---------Daftar X----------")
    print("1. X1 sDrive 18i XLine   : Rp.985   Jt/Unit")
    print("2. X3 M Competition      : Rp.2,583 M/Unit")
    print("3. X6 xDrive 40i M Sport : Rp.2,357 M/Unit")
    print("4. X7 xDrive 40i M Sport : Rp.2,774 M/Unit")
    xbmw = int(input("X : "))

    if xbmw==1 :
      model_mobil ="X1 sDrive 18i XLine"
      harga = 985000000
      stok = 4

    elif xbmw==2 :
      model_mobil ="X3 M Competition"
      harga = 2583000000
      stok = 4

    elif xbmw==3 :
      model_mobil ="X6 xDrive 40i M Sport"
      harga = 2357000000
      stok = 4

    else :
      model_mobil ="X7 xDrive 40i M Sport"
      harga = 2774000000
      stok = 4

  elif nomor==2 :
    print("----------Daftar I----------")
    print("1. I3s          : Rp.1,319 M/Unit")
    print("2. I4 eDrive 40 : Rp.2,108 M/Unit")
    print("3. I7           : Rp.3,33  M/Unit")
    print("4. I8 Roadster  : Rp.3,989 M/Unit")
    ibmw = int(input("I : "))

    if ibmw==1 :
      model_mobil ="I3s"
      harga = 1319000000
      stok = 4

    elif ibmw==2 :
      model_mobil ="I3 eDrive 40"
      harga = 2108000000
      stok = 4

    elif ibmw==3 :
      model_mobil ="I7"
      harga = 3330000000
      stok = 4

    else :
      model_mobil ="I8 Roadster"
      harga = 3989000000
      stok = 4

  elif nomor==3 :
    print("----------Daftar Series----------")
    print("1. 430i Convortible M Sport  : Rp.1,864 M/Unit")
    print("2. 630i Gran Turismo M Sport : Rp.1,599 M/Unit")
    print("3. 735i M Sport              : Rp.2,594 M/Unit")
    print("4. 840i Coupe M Technic      : Rp.3,033 M/Unit")
    series = int(input("Series : "))

    if series==1 :
      model_mobil ="430i Convortible M Sport "
      harga = 1864000000
      stok = 4

    elif series==2 :
      model_mobil ="630i Turismo M Sport "
      harga = 1599000000
      stok = 4

    elif series==3 :
      model_mobil ="735i M Sport "
      harga = 2594000000
      stok = 4

    else :
      model_mobil ="840i Coupe M Technic "
      harga = 3033000000
      stok = 4

  else :
    print("-----------Daftar M-----------")
    print("1. M2 Coupe Competition M DCT : Rp.2,2   M/Unit")
    print("2. M4 Coupe Competition       : Rp.2,919 M/Unit")
    print("3. M5 Competition             : Rp.4,747 M/Unit")
    print("4. M8 Coupe Competition       : Rp.6,857 M/Unit")
    mbmw = int(input("M : "))

    if mbmw==1 :
      model_mobil ="M2 Coupe Competition M DCT"
      harga = 2200000000
      stok = 2

    elif mbmw==2 :
      model_mobil ="M4 Coupe Competition"
      harga = 2919000000
      stok = 2

    elif mbmw==3 :
      model_mobil ="M5 Competition"
      harga = 4747000000
      stok = 2

    else :
      model_mobil ="M8 Coupe Competition"
      harga = 6857000000
      stok = 2

else :
  merk_mobil = "Lamborghini"
  print("---------Daftar Model Mobil Lamborghini----------")
  print("1. Lamborghini Aventador : Rp.6,4 - Rp.8,7 M/Unit")
  print("2. Lamborghini Urus : Rp.8,3 - Rp.9,25 M/Unit")
  print("3. Lamborghini Huracan : Rp.8,9 - Rp.9,5 M/Unit")
  nomor = int(input("Masukkan Nomor : "))

  if nomor==1 :
    print("------Daftar Lamborghini Aventador---------")
    print("1. Lamborghini Aventador LP 750-4 Superveloce : Rp.6,4 M/Unit")
    print("2. Lamborghini Aventador LP 700-4             : Rp.8,7 M/Unit")
    aven = int(input("Lamborghini Aventador : "))

    if aven==1 : 
      model_mobil ="Lamborghini Aventador LP 750-4 Superveloce"
      harga = 6400000000
      stok = 2

    else :
      model_mobil ="Lamborghini Aventador LP 700-4"
      harga = 8700000000
      stok = 2

  elif nomor==2 :
    print("--------Daftar Lamborghini Urus-------")
    print("1. Lamborghini Urus 4.0L                        : Rp.8,5  M/Unit")
    print("2. Lamborghini Urus 4.0 Urban Kit Edition Wagon : Rp.9,5 M/Unit")
    urus = int(input("Lamborghini Urus : "))

    if urus==1 :
      model_mobil ="Lamborghini Urus 4.0L"
      harga = 8500000000
      stok = 2

    else :
      model_mobil ="Lamborghini Urus 4.0 Urban Kit Edition Wagon"
      harga = 9250000000
      stok = 2

  else :
    print("-------Daftar Lamborghini Huracan---------")
    print("1. Lamborghini Huracan LP 610-4               : Rp.8,9 M/Unit")
    print("2. Lamborghini Huracan 5.2 Technica V10 Coupe : Rp.9,5 M/Unit")
    huracan = int(input("Lamborghini Huracan : "))

    if huracan==1 :
      model_mobil ="Lamborghini Huracan LP 610-4"
      harga = 8900000000
      stok = 2

    else :
      model_mobil ="Lamborghini Huracan 5.2 Technica V10 Coupe"
      harga = 9500000000
      stok = 2


jumlah = int(input("Banyak Beli : "))
print("")
print("------------Daftar Warna Mobil---------")
print("1. Hitam")
print("2. Putih")
print("3. Silver")
print("4. Merah")
print("5. Kuning")
print("6. Hijau")
print("7. Biru")
print("8. Orange")
warna = int(input("Masukkan Warna : "))

if warna==1 :
  warna_mobil = "Hitam"

elif warna==2 :
  warna_mobil = "Putih"

elif warna==3 :
  warna_mobil = "Silver"

elif warna==4 :
  warna_mobil = "Merah"

elif warna==5 :
  warna_mobil = "Kuning"

elif warna==6 :
  warna_mobil = "Hijau"

elif warna==7 :
  warna_mobil = "Biru"

else :
  warna_mobil = "Orange"

if jumlah>=3 :
  potongan = (harga*jumlah)*0.1


else : 
  potongan = 0


total = (harga*jumlah) - potongan
print("Total Harga : Rp.",total)
uang = int(input("Masukkan Uang Pembeli : "))
print("Uang Pembeli : ",uang)
kembalian = uang - total
stok_mobil = stok - jumlah

print("=========================================")
print("=========Struk Beli======================")
print("=========================================")
print("Nama         : ",pembeli)
print("Merk Mobil   : ",merk_mobil)
print("Model Mobil  : ",model_mobil)
print("Harga Mobil  : Rp. ",harga)
print("Banyak Beli  : ",jumlah)
print("               ____________+")
print("Total Harga  : Rp.",total)
print("Uang Pembeli : Rp.",uang)
print("               ____________-")
print("Kembali      : Rp.",kembalian)
print("")
print("==============Terima Kasih===============")
print("")
print("")
print("")