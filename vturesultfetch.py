from selenium import webdriver
from tkinter import *
import cv2
from  PIL import Image
import pytesseract
import time

dictn = {}
lst=[0,0]
import pandas
usns=input('Enter the starting usn from which u want result (ex/1jb16ec***):')
usne=input('Enter the ending usn:')

usns=int(usns[7:10])
usne=int(usne[7:10])
df2=pandas.DataFrame(columns=['15ES51','15EC562','15EC52','15EC553','15EC53','15EC54','15ECL57','15ECL58','15EC561','SGPA'],index=['usn'])
browser = webdriver.Chrome('C:\\Users\\Admin\\Downloads\\chromedriver.exe')
df1=pandas.DataFrame(columns=['15ES51','15EC562','15EC52','15EC553','15EC53','15ec54','15ECL57','15ECL58','15EC561','SGPA'])
try:
    browser.get('http://results.vtu.ac.in/resultsvitavicbcs_19/index.php')
except:
    print('NO INTERNET CONECTION!!')
def test(usn):
    global df1
    global dictn
    def captcha():
        browser.save_screenshot('screenshot.png')
        image = cv2.imread('screenshot.png')
        x = 730
        y = 477
        h = 20
        w = 75
        cp = image[y:y + h, x:x + w]
        cv2.imwrite('temp3.png', cp)
        cp = Image.open("temp3.png")
        nx, ny = cp.size
        cp1 = cp.resize((int(nx * 5), int(ny * 5)), Image.BICUBIC)
        cp1.save('temp4.png')
        cp2 = Image.open('temp4.png')
        a = (pytesseract.image_to_string(cp2, config='--psm 9')) 
        if(len(a) == 5):
            browser.find_element_by_name('lns').send_keys(usn)
            browser.find_element_by_name('captchacode').send_keys(a)
            browser.find_element_by_id('submit').click()
        else:
            captcha()
        try:
            alert=browser.switch_to.alert
            txt=alert.text
            print(txt)
            if (txt == 'Invalid captcha code !!!'):
                alert.accept()
                captcha()
            elif (txt == 'University Seat Number is not available or Invalid..!'):
                alert.accept()
                pass
        except:
            pass

    try:
        captcha()
    except:
        time.sleep(2)
        captcha()
    try:
        for n in range(2, 10):
            f_fath = '//*[@id="dataPrint"]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[' + str(
                n) + ']/div[5]'
            m_fath = '//*[@id="dataPrint"]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[' + str(
                n) + ']/div[1]'
            key = browser.find_element_by_xpath(m_fath).text
            value = browser.find_element_by_xpath(f_fath).text
            dictn[key] = value
        #browser.find_element_by_id("ಹಿಂದೆ / BACK").click()
        #print(browser.page_source)
        #browser.find_element_by_css_selector('input.form-control.btn.btn-info').click()
        #browser.switch_to.window(window_before)
        browser.back()
        time.sleep(3)
        dictn1 = {}
        def credit(key, value, x):
            value = int(value)
            if value >= 90:
                dictn1[key] = 10 * x
            if value in range(80, 90):
                dictn1[key] = 9 * x
            if value in range(70, 80):
                dictn1[key] = 8 * x
            if value in range(60, 70):
                dictn1[key] = 7 * x
            if value in range(50, 60):
                dictn1[key] = 6 * x
            if value in range(40, 50):
                dictn1[key] = 5 * x
            if value < 40:
                dictn1[key] = 4 * x

        for key in dictn:
            if key == '15ES51':
                credit(key, dictn[key], 4)
            if key == '15EC52':
                credit(key, dictn[key], 4)
            if key == '15EC53':
                credit(key, dictn[key], 4)
            if key == '15EC54':
                credit(key, dictn[key], 4)
            if key == '15EC562':
                credit(key, dictn[key], 3)
            if key == '15EC553':
                credit(key, dictn[key], 3)
            if key == '15ECL57':
                credit(key, dictn[key], 2)
            if key == '15ECL58':
                credit(key, dictn[key], 2)
        print(dictn1)
        sum = 0
        for key in dictn1:
            sum = sum + int(dictn1[key])
        total =round((sum / (26)),2)

        dictn['SGPA'] = total
        df1 = pandas.DataFrame(dictn, index=[usn])
        lst[1]=df1
    except:
        lst[0]=1
        lst[1]=pandas.DataFrame(columns=['15ES51','15EC562','15EC52','15EC553','15EC53','15ec54','15ECL57','15ECL58','15EC561','SGPA','15ec54','15ECL57','15ECL58','15EC561','SGPA'])
        browser.back()
        pass
    return lst

for i in range(usns,usne):
    if len(str(i))==2:
        usn=usns[0:7]+'0'+str(i)
    else:
        usn=usns[0:7]+str(i)
    test(usn)
    if((len(lst[1].columns) < 11)and(lst[0]==1)):
        df2=pandas.concat([df2,lst[1]],ignore_index=False,sort=False)
browser.quit()
df2.to_csv('vturesult.csv')
print('DONE........Check the file vturesult.csv in EXEL:')


