import mechanicalsoup
import json
from Myemail import Myemail



browser = mechanicalsoup.StatefulBrowser()
#url = "https://www.amazon.in/OnePlus-Bullets-Wireless-Earphones-Black/dp/B07D3FN6QM?pd_rd_wg=I43fD&pd_rd_r=68267e74-6fbd-4246-82c6-b0b85e5b30b6&pd_rd_w=PTG2D&ref_=pd_gw_simh&pf_rd_r=0YX7F4F1KC7FSZMFKHKR&pf_rd_p=c2ebdb65-3bcd-59df-a62a-6b0e925df1af"
#url = "https://www.amazon.in/dp/B07CZ146LZ?aaxitk=pF3sdaXgz8frczquNrC3sQ"
url = "https://www.amazon.in/OnePlus-Bullets-Wireless-Earphones-Black/dp/B07D3FN6QM/ref=cm_cr_srp_d_product_top?ie=UTF8"
response = browser.open(url, headers={'User-Agent': 'Mozilla/5.0'})
strResponse = response.text
if strResponse.__contains__("Currently unavailable"):
    print("Not Available")
else:
    myemail = Myemail()
    myemail.send_email("aruna", "aruna", "Veera", "OnePlus Available", "OnePlus Available")
