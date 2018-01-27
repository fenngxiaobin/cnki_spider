from selenium import webdriver
import csv
browser=webdriver.Chrome()
browser.get('http://kns.cnki.net')
browser.implicitly_wait(5)
#print(browser.page_source)

#javascript:void(0);
#<li id="SCOD" class="" onclick="CheckDBTag(this,'专利','SCOD',true);return false;"><a href="javascript:void(0);">专利</a></li>
submitElement=browser.find_element_by_id("SCOD")
submitElement.click()

textElememt=browser.find_element_by_id("txt_1_value1")
textElememt.clear()
textElememt.send_keys("2014")

submitElement1=browser.find_element_by_id("btnSearch")
submitElement1.click()
browser.implicitly_wait(10)



submitElement2014=browser.find_element_by_id("recommandconLink")
# print(len(submitElements20xx))
# submitElement2014=submitElements20xx[3]
submitElement2014.click()



browser.implicitly_wait(10)

browser.get("http://kns.cnki.net/kns/brief/brief.aspx?pagename=ASP.brief_default_result_aspx&dbPrefix=SCOD&dbCatalog=%E4%B8%AD%E5%9B%BD%E5%AD%A6%E6%9C%AF%E6%96%87%E7%8C%AE%E7%BD%91%E7%BB%9C%E5%87%BA%E7%89%88%E6%80%BB%E5%BA%93&ConfigFile=SCDBINDEX.xml&research=off&t=1507087412738&keyValue=2014&S=1")
#browser.get("http://kns.cnki.net/kns/brief/brief.aspx?pagename=ASP.brief_default_result_aspx&dbPrefix=SCOD&dbCatalog=%E4%B8%AD%E5%9B%BD%E5%AD%A6%E6%9C%AF%E6%96%87%E7%8C%AE%E7%BD%91%E7%BB%9C%E5%87%BA%E7%89%88%E6%80%BB%E5%BA%93&ConfigFile=SCDBINDEX.xml&keyValue=2014&S=1")

browser.implicitly_wait(2)
links=browser.find_elements_by_class_name("fz14")
print(len(links))
href=links[0].get_attribute("href")
print(href.split("filename=")[1])

hrefs_end=[1]*len(links)

i=0
while i < len(links) :
    hrefs_end[i]=str(links[i].get_attribute("href").split("filename=")[1])
    i=i+1


# with open("urls.csv","a") as f:
#     writer=csv.writer(f)
#     # writer.writerows(hrefs_end)
#     for x in hrefs_end:
#         writer.writerow(list(x))
#         print(x)
print(hrefs_end)




while i < len(links) :
    pre_url="http://dbpub.cnki.net/grid2008/dbpub/detail.aspx?dbcode=SCPD&dbname=SCPD2014&filename="
    patent_url=pre_url+hrefs_end[i].split("filename=")[1]
    print("patent_url",patent_url) #具体专利页面url


k=1
while True:
    browser.get("http://kns.cnki.net/kns/brief/brief.aspx?curpage=+"+str(k)+"+&RecordsPerPage=50&QueryID=4&ID=&turnpage=1&tpagemode=L&dbPrefix=SCOD&Fields=&DisplayMode=listmode&PageName=ASP.brief_default_result_aspx#J_ORDER&")
    k=k+1
    browser.implicitly_wait(4)
    links = browser.find_elements_by_class_name("fz14")
    # 没有验证码 输出20  否则0
    print(len(links))
    if len(links)==50:

        href = links[0].get_attribute("href")
        print(href.split("filename=")[1])

        hrefs_end = [1] * len(links)

        i = 0
        while i < len(links):
            hrefs_end[i] = str(links[i].get_attribute("href").split("filename=")[1])
            i = i + 1

        with open("urls.csv", "a") as f:
            writer = csv.writer(f)
            # writer.writerows(hrefs_end)
            for x in hrefs_end:
                writer.writerow(list(x))
                print(x)
        print(hrefs_end)

        while i < len(links):
            pre_url = "http://dbpub.cnki.net/grid2008/dbpub/detail.aspx?dbcode=SCPD&dbname=SCPD2014&filename="
            patent_url = pre_url + hrefs_end[i].split("filename=")[1]
            print(patent_url)  # 具体专利页面url
    else:
#         验证码处理 *_*  人眼识别 Q_Q


        print("验证码处理....")
        s = input("input code: ")
        checkCode=browser.find_element_by_id("CheckCode")
        checkCode.clear()
        checkCode.send_keys(s)
        submit_checkCode=browser.find_element_by_xpath("/html/body/p[1]/input[2]")
        submit_checkCode.click()
print(k-1)




