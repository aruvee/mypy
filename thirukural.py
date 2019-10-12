import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
static_url = "https://www.merkol.in/wp-content/uploads/2018/12/"
suffix_url = "thirukkural-kural-value.jpg"
file_prefix = 'd:\\thirukural\\'

counter = 1

while counter < 1331:
        suffix_url_new = suffix_url.replace('value', str(counter))
        response = browser.open(static_url+suffix_url_new)
        print(static_url+suffix_url_new)
        if response.status_code == 200:
                filename = file_prefix + suffix_url_new
                print(filename)
                with open(filename, 'wb') as outfile:
                        outfile.write(response.content)
                        outfile.close()
        counter = counter + 1


