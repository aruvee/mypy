import quandl
quandl.ApiConfig.api_key = "YybtcsF7JSx7x_madGF-"
data = quandl.get("CHRIS/CME_NG1")
print(data)