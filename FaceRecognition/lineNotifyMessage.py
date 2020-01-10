import requests

def lineNotifyMessage( token, picURI1,picURI2):
   
    headers = {
        "Authorization": "Bearer " + token, 
        #"Content-Type" : "application/x-www-form-urlencoded"
    }
    # 修改為你要傳送的訊息內容
    msg1 = 'Hi! "kevin" login'
    msg2 = 'your face'
    msg3 = 'your body'
    msg4 = '點名成功！'
    payload1 = {'message': msg1}
    files1 = {'imageFile': open(picURI1, 'rb')}
    payload2 = {'message': msg2}
    files2 = {'imageFile': open(picURI2, 'rb')}
    payload3 = {'message': msg3}
    payload4 = {'message': msg4}

    
    session = requests.Session()
    r = session.post("https://notify-api.line.me/api/notify", headers = headers, params = payload1)
    r = session.post("https://notify-api.line.me/api/notify", headers = headers, params = payload2, files = files1)
    r = session.post("https://notify-api.line.me/api/notify", headers = headers, params = payload3, files = files2)
    r = session.post("https://notify-api.line.me/api/notify", headers = headers, params = payload4)

    return r.status_code
	
# 修改為你要傳送的訊息內容
message = 'Notify from LINE, HELLO WORLD'
# 修改為你的權杖內容
token = 'w5uwWcnzXeopwb0OLoDuwnX4XB2g1v0cQ3xWvCDSsC1'

