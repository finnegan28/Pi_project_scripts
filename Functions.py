from pyfcm import FCMNotification

def sendPush():{
    push_service = FCMNotification(
        api_key="AAAATLrII80:APA91bFUNORsR6DydimlmLF1czI3xKt-yVHhwVK0i22s1B-e1ggNszmaZB29f2ACwJhn7xdiLIWMQG5DNZbZxcuIyuEQ37IStxJivtHttRovz3I6W_ldvkNlvXfnbz9j6IFIcdPLZ_Dm")
    registration_id = "eZBi5oJvcJI:APA91bE_VPHC8NOXFzwkNttdVrRujCQJZKnHmTqQGUMcc96_l7oB2NWlkzpwnGORfv6MGsEKGG6ov68mvWfeQaYF6B14sctu7e9x1JakBGBrPBSAANU2U2zLT_O0pGNV0mPaeFEnp8CN"
    message_title = 'Motion Detected!'
    message_body = 'Motion Detected!'
    sound = 'default'
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                               message_body=message_body, sound=sound)
}

def