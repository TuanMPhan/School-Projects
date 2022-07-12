import sys
import xml.dom.minidom
import mysql.connector


def getDate(document):
    count = 0
    tableElements = document.getElementsByTagName('table')
    for tr in tableElements[0].getElementsByTagName('tr'):
        count += 1
        data = []
        if count == len(tableElements[0].getElementsByTagName('tr')):
            for td in tr.getElementsByTagName('td'):
                for node in td.childNodes:
                    if node.nodeType == node.TEXT_NODE:
                        data.append(node.nodeValue)
    data = ' '.join(data)
    data = data[17:36]
    return data 


def getDayAndNight(document):
    div = document.getElementsByTagName('div')
    infor =[]
    for i in range(0, len(div)):
        if div[i].getAttribute('class') == "tombstone-container":
            data = []
            for p in div[i].getElementsByTagName('p'):
                if p.getAttribute('class') == "period-name":
                    for node in p.childNodes:
                        if node.nodeType == node.TEXT_NODE:
                            data.append(node.nodeValue)
                    data = ' '.join(data) 
                    infor.append(data)                      
    return infor

def getTemp(document):
    div = document.getElementsByTagName('div')
    infor =[]
    for i in range(0, len(div)):
        if div[i].getAttribute('class') == "tombstone-container":

            for p in div[i].getElementsByTagName('p'):
                if (p.getAttribute('class') == "temp temp-low") or (p.getAttribute('class') == "temp temp-high"):
                    for node in p.childNodes:
                        if node.nodeType == node.TEXT_NODE:
                            infor.append(node.nodeValue)           
    return infor
    

def getLong(document):
    img = document.getElementsByTagName('img')
    infor = []
    for i in range(0,len(img)):
        data =[]
        if img[i].getAttribute('class') == "forecast-icon":
            data.append(img[i].getAttribute('alt'))
            infor.append(img[i].getAttribute('alt'))
    return infor



def getShort(document):
    div = document.getElementsByTagName('div')
    infor = []
    for i in range(0,len(div)):
        if div[i].getAttribute('class') == "tombstone-container":
            data =[]
            for p in div[i].getElementsByTagName('p'):
                if p.getAttribute('class') == "short-desc":
                    for node in p.childNodes:
                        if node.nodeType == node.TEXT_NODE:
                            data.append(node.nodeValue)
                    data = ' '.join(data)
                    infor.append(data)
    return infor
                    

def finallize(dayAndNight, long_desc, short_desc, date, temp):
    vals = []
    for i in range(len(dayAndNight)):
        data = []
        data.append(date)
        data.append(dayAndNight[i]) 
        data.append(short_desc[i]) 
        data.append(temp[i]) 
        data.append(long_desc[i]) 
        tup = tuple((data))
        vals.append(tup)
    return vals

def insert(cursor,data,city):
    ct = city 
    query = 'INSERT INTO {}(date,dayOrNight,short_desc,temperature,long_desc) VALUES (%s,%s,%s,%s,%s)'.format(ct)
    values = data
    for value in values:
        cursor.execute(query, value)



def update(cursor,data,city):
    ct = city
    iD = 1
    query = 'UPDATE {} SET date= %s,dayOrNight= %s,short_desc= %s,temperature= %s,long_desc= %s WHERE id=%s'.format(ct)
    values = data
    for value in values:
        value = list(value)
        value.append(iD)
        cursor.execute(query,value)
        iD += 1




cities = ["newark","hackensack","hoboken","princeton","trenton"]
for city in cities:
    print(city)
    source = city + ".xhtml"
    document = xml.dom.minidom.parse(source)
    dayAndNight = getDayAndNight(document)
    long_desc = getLong(document)
    date = getDate(document)
    temp = getTemp(document)
    short_desc = getShort(document)
    vals = finallize(dayAndNight, long_desc, short_desc, date, temp)
    try:
        cnx = mysql.connector.connect(host='localhost', user='tp', password='bi646999', database='weather')
        cursor = cnx.cursor()

        # insert(cursor,vals,city)
        # cnx.commit()

        update(cursor,vals,city)
        cnx.commit()

        cursor.close()
    except mysql.connector.Error as err:
        print(err)
    finally:
        try:
            cnx
        except NameError:
            pass
        else:
            cnx.close()



    



