from gcm import *

gcm = GCM("AIzaSyBIm4D57_9XZGiR3hKPRcOW3Z__gKWcwbY")
data = {'the_message': 'You have x new friends', 'param2': 'value2'}

reg_id = ''

gcm.plaintext_request(registration_id=reg_id, data=data)