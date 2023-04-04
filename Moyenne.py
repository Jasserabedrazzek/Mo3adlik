import streamlit as st
import datetime
import time
st.set_page_config(page_title="Moyennek",page_icon=":1234:",layout="centered")

st.title("Ehsib Moyennek")
st.write('---')
col1,col2,col3 = st.columns(3)

with col2:
    st.header("Math")
    def Math():
        c = (st.text_input("Control"))
        s = (st.text_input("Synthese"))
        try:    
            if c != " "and s !="" and c != "*" and s!="*":
                c = float(c)
                s = float(s)

                if c<=20 and c>=0 and s>=0 and s<=20:
                    math = (c + s*2)/3
                    if math<10:
                        st.error(str(math)[0:6])
                    elif math >10 and math<15:
                        st.warning((str(math)[0:6]))
                    else:
                        st.success((str(math)[0:6]))
                return math
            else:
                math = 0
                return math
        except :
            st.error('This is an error', icon="🚨")
            math = 0
            return math

        
    a =  Math()
    st.header("Physique")
    def Physique():
        c = (st.text_input("Control Physique"))
        tp = st.text_input("TP")
        s = (st.text_input("Synthese Physique"))
        try:
            if c!="" and s!="" and tp!="":
                c = float(c)
                tp = float(tp)
                s = float(s)
            
                if c<=20 and c>=0 and s>=0 and s<=20:
                    phy = (c +tp+ s*2)/4
                    if phy<10:
                        st.error(str(phy)[0:6])
                    elif phy >10 and phy<15:
                        st.warning((str(phy)[0:6]))
                    else:
                        st.success((str(phy)[0:6]))
                return phy
            else:
                phy = 0
                return phy
        except :
            st.error('This is an error', icon="🚨")
            phy = 0
            return phy

    b =  Physique()
    st.header("Arabia")
    def Arabia():
        c = (st.text_input("Control Arabia"))
        orla  = st.text_input("Oral Arabia")
        s = (st.text_input("Synthese Arabia"))
        try:
            if c!="" and s!=""and orla !="":
                c = float(c)
                ola = float(orla)
                s = float(s)
                if c<=20 and c>=0 and s>=0 and s<=20:
                    arabia = (c +ola+ s*2)/4
                    if arabia<10:
                        st.error(str(arabia)[0:6])
                    elif arabia >10 and arabia<15:
                        st.warning((str(arabia)[0:6]))
                    else:
                        st.success((str(arabia)[0:6]))
                return arabia
            else:
                arabia = 0
                return arabia
        except:
                st.error('This is an error', icon="🚨")
                arabia = 0
                return arabia
        
    c =  Arabia()
    st.header("Français")
    def Français(): 
        c = (st.text_input("Control Français"))
        orlf = st.text_input("Orla Français")
        s = (st.text_input("Synthese Français"))
        
        try:
            if c !="" and s !="" and orlf !="":
                c = float(c)
                orlf = float(orlf)
                s = float(s)
                if c<=20 and c>0 and s>0 and s<=20:
                    fra = (c +orlf+ s*2)/4
                    if fra<10:
                        st.error(str(fra)[0:6])
                    elif fra >10 and fra<15:
                        st.warning((str(fra)[0:6]))
                    else:
                        st.success((str(fra)[0:6]))
                return fra
            else:
                fra =0
                return fra
        except:
            st.error('This is an error', icon="🚨")
            fra = 0
            return fra
    d =  Français()
    st.header("English")
    def English():  
        c = (st.text_input("Control En"))
        orle = st.text_input("Oral En")
        s = (st.text_input("Synthese En"))
        
        try:
            if c !="" and s !="" and orle !="":
                c = float(c)
                orle = float(orle)
                s = float(s)
                if c<=20 and c>=0 and s>=0 and s<=20:
                    en = (c +orle+ s*2)/4
                    if en<10:
                        st.error(str(en)[0:6])
                    elif en >=10 and en<=15:
                        st.warning((str(en)[0:6]))
                    else:
                        st.success((str(en)[0:6]))
                return en
            else:
                en = 0
                return en
        except:
            st.error('This is an error', icon="🚨")
            en  = 0
            return en
    e =  English()
    st.header("Tarikh")
    def Tarikh():   
        c = (st.text_input("Control Tarikh"))
        orlt = st.text_input("Oral Tarikh")
        s = (st.text_input("Synthese Tarikh"))
        
        try:
            if c != "" and s != "" and orlt !=" ":
                c = float(c)
                orlt = float(orlt)
                s = float(s)
                if c<=20 and c>=0 and s>=0 and s<=20:
                    tr = (c +orlt+ s*2)/4
                    if tr<10:
                        st.error(str(tr)[0:6])
                    elif tr >10 and tr<15:
                        st.warning((str(tr)[0:6]))
                    else:
                        st.success((str(tr)[0:6]))
                return tr
            else:
                tr = 0
                return tr
        except:
            st.error('This is an error', icon="🚨")
            tr = 0
            return tr
    f =  Tarikh()
    st.header("Geoghraphiya")
    def Geogr():
        c = (st.text_input("Control Geo"))
        orlg = st.text_input("orl Geo")
        s = (st.text_input("Synthese Geo"))
        try:
            if c!='' and s!='' and orlg !='':
                c = float(c)
                orlg = float(orlg)
                s = float(s)
                if c<=20 and c>=0 and s>=0 and s<=20:
                    geo = (c +orlg+ s*2)/4
                    if geo<10:
                        st.error(str(geo)[0:6])
                    elif geo >10 and geo<15:
                        st.warning((str(geo)[0:6]))
                    else:
                        st.success((str(geo)[0:6]))
                return geo
            else:
                geo =0  
                return geo
        except:
            st.error('This is an error', icon="🚨")
    g =  Geogr()
    st.header("Informatique")
    def info():
        c = (st.text_input("Control Info"))
        s = (st.text_input("Synthese Info"))
        try:
            if c!='' and s!= '':
                c = float(c)
                s = float(s)
                if c<=20 and c>=0 and s>=0 and s<=20:
                    infor = (c +orlo+ s*2)/3
                    if infor<10:
                        st.error(str(infor)[0:6])
                    elif infor >10 and infor<15:
                        st.warning((str(infor)[0:6]))
                    else:
                        st.success((str(infor)[0:6]))
                return infor
            else:
                infor = 0
                return infor
        
        except:
            st.error('This is an error', icon="🚨")
            infor = 0
            return infor
    h =  info()
    st.header("Sport")
    def Sport():
        c = (st.text_input("Control Sport"))
        s = (st.text_input("Synthese Sport"))
        try:
            if c != '' and s != '':
                c = float(c)
                s = float(s)
                if c<=20 and c>=0 and s>=0 and s<=20:
                    sports = (c + s*2)/3
                    if sports<10:
                        st.error(str(sports)[0:6])
                    elif sports >=10 and sports<=15:
                        st.warning((str(sports)[0:6]))
                    else:
                        st.success((str(sports)[0:6]))
                return sports
            else:
                sports = 0
                return sports
        except:
            st.error('This is an error', icon="🚨")
            sports = 0
            return sports
    i =  Sport()
    st.header("Philosophie")
    def fals():
        s = (st.text_input("Synthese Philo"))
        
        try:
            if s!="":
                s = float(s)
                if s>=0 and s<=20:
                    philo = s
                    if philo<10:
                        st.error(str(philo)[0:6])
                    elif philo >10 and philo<15:
                        st.warning((str(philo)[0:6]))
                    else:
                        st.success((str(philo)[0:6]))
            else:
                philo = 0
            return philo
            
        except:
            st.error('This is an error', icon="🚨")
            philo = 0
            return philo
    j =  fals()
    st.header("Science")
    def Science():
        c = (st.text_input("Control SC"))
        TPs = st.text_input("TP SC")
        s = (st.text_input("Synthese SC"))
        try:
            if c != '' and TPs != '' and s !='':
                c = float(c)
                TPs = float(TPs)
                s = float(s)
                if c<=20 and c>=0 and s>=0 and s<21 and TPs <=20:
                    sc = (c +TPs+ s*2)/4
                    if sc<10:
                        st.error(str(sc)[0:6])
                    elif sc >10 and sc<15:
                        st.warning((str(sc)[0:6]))
                    else:
                        st.success((str(sc)[0:6]))
                return sc
            else:
                sc = 00
                return sc
        except:
            st.error('This is an error', icon="🚨")
            sc = 0
            return sc
    k =  Science()
    st.header("Islamiya")
    def Isl():
        c = (st.text_input("Control Islamiya"))
        orls = st.text_input("Oral Islamiya")
        s = (st.text_input("Synthese islamiya"))
        try:
            if c!=""and orls != '' and s !='' :
                c = float(c)
                orls = float(orls)
                s = float(s)
                if c<21 and c>=0 and s>=0 and s<=20:
                    isl = (c +orls+ s*2)/4
                    if isl<10:
                        st.error(str(isl)[0:6])
                    elif isl >10 and isl<15:
                        st.warning((str(isl)[0:6]))
                    else:
                        st.success((str(isl)[0:6]))
                return isl
            else:
                isl = 0
                return isl
        except:
            st.error('This is an error', icon="🚨")
            isl = 0
            return isl
    l =  Isl()
    st.header("Option")
    def Option():
        c = (st.text_input("Control Option"))
        orlo = st.text_input("Oral Option")
        s = (st.text_input("Synthese Option"))
        
        try:
            if c != "" and orlo != "" and s != "":
                c = float(c)
                orlo =float(orlo)
                s = float(s)
                if c<=20 and c>=0 and s>=0 and s<=20:
                    op = (c + s*2)/4
                    if op<10:
                        st.error(str(op)[0:6])
                    elif op >=10 and op<=15:
                        st.warning((str(op)[0:6]))
                    else:
                        st.success((str(op)[0:6]))
                return op
            else:
                op = 0
                return op
        except:
            st.error('This is an error', icon="🚨")
            op = 0
            return op
    m =  Option()
    res = a*4+b*4+c*2+d*2+e*2+f+g+h*1.5+i+j+k*1.5+l+m

    btn = st.button("Calculer votre  Moyennek")
    if btn:
        resultat = res/23
        st.header("Moyennek")
        if resultat < 10:
            st.error(str(resultat)[0:5])
        elif resultat >= 10 and resultat < 15:
            st.warning(str(resultat)[0:5])
        else:
            st.success(str(resultat)[0:5])
st.write('---')
col10,col11 = st.columns(2)
with col10:
    st.write("Crédits:","[Jasser ben abed razzek](https://www.facebook.com/jasser.razzek.3/)")
with col11:
    st.write("Copyright :copyright: 2023, Streamlit Inc")
col13,col14 = st.columns(2)
with col14:
    current_time = st.empty()
    current_time.text(datetime.datetime.now().strftime("%H:%M:%S"))

# Update the time every second
    while True:
        current_time.text(datetime.datetime.now().strftime("%H:%M:%S"))
        time.sleep(1)
