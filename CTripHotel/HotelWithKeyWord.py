from selenium import webdriver


def cookie_optimizer(cookie):
    cookie_list = cookie.split('; ')
    cookie_map = {}
    for i in cookie_list:
        temp = i.split("=")
        cookie_map[temp[0]] = temp[1]
    # print(cookie_map)
    return cookie_map


def initialize_broswer(cookie):
    driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    # cookie_optimized = cookie_optimizer(cookie)
    # print("add cookie:" + cookie_optimized.__str__())
    # driver.add_cookie(cookie_dict=cookie_optimized)
    driver.get("https://passport.ctrip.com/user/login?BackUrl=https%3A%2F%2Fhotels.ctrip.com%2Fhotel%2Ffuzhou258%23ctm_ref%3Dhod_hp_sb_lst#ctm_ref=c_ph_login_buttom")
    return driver

if __name__ == '__main__':
    cookie = "magicid=06b/6puHHyM72HQVkmQbKOeT5abMVemBG5MKWGU+nZzBaLSQv4yIN4/TI76Mhhde; ASP.NET_SessionId=hm2yvp31i45acoo2tzz0qbc1; _abtest_userid=91587fec-8ccf-473d-b544-a7f5b3086225; hoteluuid=OT9hVAlOQdoHuXm5; OID_ForOnlineHotel=15853696478193zq35c1585369647881102002; MjAxNS8wNi8yOSAgSE9URUwgIERFQlVH=OceanBall; _RGUID=877b9294-1209-43cf-90c8-addf6b176843; _RDG=28e83b2741e6cc29ea00b44d6872f0a664; _RF1=112.44.157.40; _RSG=FFK2IGfaxT83Xs5hzTh839; MKT_CKID=1585369651683.vxe1b.m08b; MKT_CKID_LMT=1585369651683; _gid=GA1.2.801592006.1585369652; _ga=GA1.2.1804313618.1585369652; _gat=1; MKT_Pagesource=PC; login_uid=E11FB9B299ABCA2A3C9A296ABBF81EA4; login_type=0; cticket=79BA063D34CD82E9BD79A4E2737FC4CB3DD4D76EB707B71086F6AF31E932A38D; AHeadUserInfo=VipGrade=0&VipGradeName=%C6%D5%CD%A8%BB%E1%D4%B1&UserName=%B7%EE%CD%F2%D3%E0&NoReadMessageCount=1; ticket_ctrip=bJ9RlCHVwlu1ZjyusRi+ypZ7X2r4+yojVrf/o0+b13KnaFho2AejylhOclu72EXgaZ+kQx+lHl27l8AMQTvm+6jFI5TzUPcCvri1K7Qmpbxaz+KdBa3Z516CT4Kh8JHUW1mPe61U/PQyOgHyhBo1s74f4LTLOGuPLu1/xD8ThrXHSMu7n3fxQb4qKbCYkLjzQeiAhS8Z2GWiDRwGdwcSvEMC8HI7OIKrVpyNpc0lwh17b2Bc8dWJi0YI0ed/LFFx0eU9mpDb8G1q+aqmIQZMJgjgaBrh9OsGtrFF5ZxfRq0=; DUID=u=CF9DE88ABC0A3A6ED58C7617AC4CB782&v=0; IsNonUser=u=CF9DE88ABC0A3A6ED58C7617AC4CB782&v=0; IsPersonalizedLogin=T; UUID=DD0842307CE84B959944DCFCF00C7677; hoteluuidkeys=qM9enSKbLez9EOUW4YtY1cYS0EbYtYqBeT3EkUjZ4W8YFYtmj0SWT8K7Zj8YtYqOjXpr6bJN5jdYzYQUidGwTar4SrdYLYhSvTlY3BvLNjtTv0qrBSWZaj5ZRdYbYOovt6vFOYcSwF4jpDezmi1cJaYnYOYsYlbv8henUYHAiPXYBYnYaYcYh7EAZKPLwo8iOBRgmjPrOsY8cJTayZrGTYF6WnOvNTxqke1zYL5x1nxDLY4tig8wM8jF1EtzJU0WQTjDrANJMGizlw7kvftRmQj9nYntjgr1TycNi7awpnRUfEZmj5ZxdqxobEFQEN7ESMW3ge1qw0kEH6jsaed1iUhYmhrXMeB4ec7x3XisoipTxSfWh5jsce8Sw46KXswTUihXRFlj5BeNXE8hyzgvs4ibGEXnyl3vklKSPEL4KfDwFaig4Ra4jDrHZYfdJQLy4rTZjl3eMaj4LK1BjcgwgfxfpxaBx9qxGBEb0ENUE6ZWU1epDwLHEH9jS9eopiT1YSHrAHENzytqvsDi0DEz4yfzv83K9DWd7EqDjspeASxSLjarZLEPOW6geHLj69YsGjsAxBmxkUx3hxphEb4EHsEN0W1neLtw1GElGjqHeGbiS8YUPrPDeGTeg4Y6qEbUwTlWhNi00KTmE7BE9gEfgWzqeUfwMOEpdj8Uen5ioHYaTrtpeTmeGlEgBYtaEozwL1WabinY7YTdYOZik5ifUiGPjOY1YDSy9cwlSys6w0FimbjM6wA3ytYmYGDR4UJDAjqGJm5ionwp3vGlwN8yS1WD6YOoitbJ8YTYOURkqwaMv1TKDljZ0YhlW6HR3Pi1GyzNinfvlGvZZxO4ROAJaYbYq1RMGJ7hj6zJdoiBTwO3v17wPlEhQykSjFURO3vSYoY57jXNwmMvtq; _bfs=1.4; _bfa=1.1585369647819.3zq35c.1.1585369647819.1585369647819.1.4; hotelhst=2012709687; __zpspc=9.1.1585369651.1585369673.2%234%7C%7C%7C%7C%7C%23; _jzqco=%7C%7C%7C%7C1585369651868%7C1.319003963.1585369651679.1585369651679.1585369673071.1585369651679.1585369673071.undefined.0.0.2.2; _bfi=p1%3D102002%26p2%3D10320670296%26v1%3D4%26v2%3D3"
    driver = initialize_broswer(cookie)


