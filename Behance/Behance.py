#coding:utf-8
from lxml import etree
import requests
import pymysql


cookies = {
    "bcp": "dd54f74e-3ed9-40d3-9047-c753c1563179",
    "bcp_generated": "1585281492242",
    "gk_suid": "72744919",
    "gki": "%7B%22db_semaphore%22%3Afalse%7D",
    "AMCVS_9E1005A551ED61CA0A490D45%40AdobeOrg": "1",
    "AMCV_9E1005A551ED61CA0A490D45%40AdobeOrg": "-227196251%7CMCMID%7C21730502605978059267184677494112415209%7CMCAID%7CNONE%7CMCOPTOUT-1585288694s%7CNONE%7CMCAAMLH-1585886294%7C11%7CMCAAMB-1585886294%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI",
    "sign_up_prompt": "true",
    "s_sess": "%20s_dmdbase%3D1%3B%20s_dmdbase_custom%3D1%3B%20s_sq%3Dadbadobenonacdcprod%25252Cadbadobeprototype%253D%252526c.%252526a.%252526activitymap.%252526page%25253Dbehance.net%2525253Agallery%252526link%25253Dn1a2-%252526region%25253Dother%252526pageIDType%25253D1%252526.activitymap%252526.a%252526.c%3B%20s_ppv%3D%255B%2522www.behance.net%252Fgallery%252F92260695%252FRuberoid-type-family%2522%252C7%252C0%252C1010%252C2048%252C1010%252C2048%252C1152%252C1.25%252C%2522P%2522%255D%3B%20s_cc%3Dtrue%3B",
    "s_pers": "%20s_nr%3D1585285945961-Repeat%7C1616821945961%3B%20cpn%3Dbehance.net%253Agallery%7C1743052346677%3B%20ppn%3Dbehance.net%253Agalleries%7C1743052346678%3B%20s_vs%3D1%7C1585287751419%3B",
    "s_sess": "%20s_dmdbase%3D1%3B%20s_dmdbase_custom%3D1%3B%20s_sq%3Dadbadobenonacdcprod%25252Cadbadobeprototype%253D%252526c.%252526a.%252526activitymap.%252526page%25253Dbehance.net%2525253Agallery%252526link%25253Dn1a2-%252526region%25253Dother%252526pageIDType%25253D1%252526.activitymap%252526.a%252526.c%3B%20s_cc%3Dtrue%3B%20s_ppv%3D%255B%2522www.behance.net%252F%2522%252C100%252C0%252C4565.199951171875%252C2048%252C1010%252C2048%252C1152%252C1.25%252C%2522P%2522%255D%3B",
    "sign_up_prompt": "true",
}


def parseJson(data):
    download_list = []
    for i in data["category_projects"]:
        temp = {"id": i["id"], "name": i["name"], "featured_on": i["featured_on"], "url": i["url"], }
        download_list.append(temp)
    return download_list


def fetch_ordinal(ordinal):
    url = "https://www.behance.net/v2/discover/graphic-design/typography?ordinal={0}".format(ordinal)
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Host": "www.behance.net",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36",
        "X-BCP": "dd54f74e-3ed9-40d3-9047-c753c1563179",
        "X-NewRelic-ID": "VgUFVldbGwACXFJSBAUF",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.behance.net/galleries/graphic-design/typography?ordinal=48",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }
    print("fetching download_list:" + url)
    rsp = requests.get(url=url, headers=headers, cookies=cookies)
    return rsp.json(encoding="utf-8")


def fetch_img(url):
    print("fetching url:" + url)
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Host": "www.behance.net",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        # "If-Modified-Since": "Fri, 27 Mar 2020 10:59:49 +0000",
        # "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36",
        "Referer": url
    }
    cookies["ilo0"] = "true"
    rsp = requests.get(url=url, headers=headers, cookies=cookies)
    html = rsp.content.decode("utf8")
    # print(html)
    tree = etree.HTML(html)
    container = tree.xpath('//*[@data-ut="image"]')
    for i in container[0]:
        img = i.xpath('//img/@behance')
        print(img)

    # print(rsp.json(encoding="utf-8"))


if __name__ == '__main__':
    """
    --- creative fields ---
    图形设计： graphic-design
        > typography / packaging / Branding / Editorial / Infographic / goster / graphic-design / exhibition-&-signage / logo / music-packaging
    摄影：     photography
    插图：     illustration
    交互：     interaction
    动画：     motion
    建筑：     architecture
    产品设计： product-design
    时尚：     fashion
    广告：     advertising 
    美术：     fine-arts
    手工艺：   crafts
    游戏设计： game-design 
    声音：     sound
    
    
    --- creative tools ---
    photoshop
    substance-painter
    """
    behance_categories = ("photoshop", "substance-painter", "advertising", "fine-arts")
    # fetch_json = fetch_ordinal(0)
    # download_list = parseJson(fetch_json)
    # print(download_list)

    fetch_img("https://www.behance.net/gallery/92260695/Ruberoid-type-family?tracking_source=curated_galleries_list")
    # for i in download_list:
    #     fetch_img(i["url"])