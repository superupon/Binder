import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types


from evernote.api.client import EvernoteClient

# Real applications authenticate with Evernote using OAuth, but for the
# purpose of exploring the API, you can get a developer token that allows
# you to access your own Evernote account. To get a developer token, visit
# https://sandbox.evernote.com/api/DeveloperToken.action
auth_token = "S=s1:U=91704:E=1573881852a:C=14fe0d055d0:P=1cd:A=en-devtoken:V=2:H=2a465891a2e34e1eaf4fcafada906411"

if auth_token == "your developer token":
    print "Please fill in your developer token"
    print "To get a developer token, visit " \
        "https://sandbox.evernote.com/api/DeveloperToken.action"
    exit(1)

	
developer_token = "S=s31:U=6ef7ad:E=1573ab26fc7:C=14fe3014378:P=1cd:A=en-devtoken:V=2:H=844a167e0b782fe8b18011aee5394b44"

# Set up the NoteStore client 
client = EvernoteClient(token=developer_token, sandbox = False, service_host="app.yinxiang.com")
print developer_token
user_store = client.get_user_store()
user = user_store.getUser()
print user.username
note_store = client.get_note_store()
 