#coding: utf-8
import json
import urllib
import urllib2
import json
import time

f = open('config.json', 'r')
json_dict = json.load(f)

delete_url = json_dict[u'delete_url']
hist_url = json_dict[u'hist_url']
token = json_dict[u'token']
channel = json_dict[u'channel']

delete_params = {'token':token,
          'channel':channel
}
hist_params = {'token':token,
          'channel':channel,
          'count' : '20',
}

hist_params = urllib.urlencode(hist_params)

req = urllib2.Request(hist_url)
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
req.add_data(hist_params)

res = urllib2.urlopen(req)

body = res.read()
data = json.loads(body)

for m in data["messages"]:
  if m[u'bot_id'] == json_dict[u'bot_id']:
      delete_params['ts'] = m["ts"]
      enc_params = urllib.urlencode(delete_params)

      req = urllib2.Request(delete_url)
      req.add_header('Content-Type', 'application/x-www-form-urlencoded')
      req.add_data(enc_params)


      res = urllib2.urlopen(req)

      body = res.read()
      print(body)
      #連続で送りすぎるとエラーになるので1秒待機
      time.sleep(1)
