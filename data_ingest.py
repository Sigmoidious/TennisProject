import http.client
import pandas as pd

conn = http.client.HTTPSConnection("tennis-api-atp-wta-itf.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "b1a29caffamsh059a166b5195a38p12924cjsn979b6281b096",
    'x-rapidapi-host': "tennis-api-atp-wta-itf.p.rapidapi.com"
}

conn.request("GET", "/tennis/v2/atp/h2h/match-stats/19400/5992/677", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))