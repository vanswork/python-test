from bottle import run, post
from pyngrok import ngrok

# Open a HTTP tunnel on the default port 80
public_url = ngrok.connect()
# Open a SSH tunnel
ssh_url = ngrok.connect(8080, "tcp")

#  tunnels = ngrok.get_tunnels()
#  A public ngrok URL that tunnels to port 80 (ex. http://<public_sub>.ngrok.io)
#  public_url = tunnels[0].public_url

#  https://api.telegram.org/bot1389188838:AAH8qW2LXnc6mlnzeo3x3G_q1E4jwuGam5k/setWebHook?url=https://47dad9add544.ngrok.io
#  https://api.telegram.org/bot1389188838:AAH8qW2LXnc6mlnzeo3x3G_q1E4jwuGam5k/getWebhookInfo

@post('/')  # our python function based endpoint
def main():
    return


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)