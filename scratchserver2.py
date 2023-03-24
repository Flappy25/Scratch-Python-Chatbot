#!python3

#SERVER 2

print('importing modules...')
import openai
import scratchattach as scratch3
from scratchattach import Encoding

print('imported modules')

print('starting connections...')

#start connections
session = scratch3.login("gioleung", "12131415gioleung")
conn = session.connect_cloud("824637049")
#value = scratch3.get_var("project_id", "variable")

print('connections started')

conn.set_var("serverdown", '0')

#set API key
openai.api_key = "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"

#Encoding.encode("input") #will return the encoded text
#Encoding.decode("encoded") #will decode an encoded text


def split_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Calculate the length of each segment
    segment_length = len(words) // 5

    # Calculate the remainder to distribute among the segments
    remainder = len(words) % 5

    # Split the words into five segments
    segments = []
    start = 0
    for i in range(5):
        # Calculate the end index for this segment
        end = start + segment_length

        # Add a word from the remainder to this segment if needed
        if remainder > 0:
            end += 1
            remainder -= 1

        # Join the words in this segment into a sentence
        segment = ' '.join(words[start:end])

        # Add the segment to the list of segments
        segments.append(segment)

        # Update the start index for the next segment
        start = end

    # Return the five segments as a tuple
    return tuple(segments)


#Start Message loop


print('standby...')

while True:

    conn.set_var("serverdown", '0')
    
    res = scratch3.get_var("824637049", "res")

    if res == '1':

        print('getting usermessage')
        
        usermessage = scratch3.get_var("824637049", "usermessage")
        usermessage = Encoding.decode(usermessage)

        print('usermessage recived')

        print('USERMESSAGE:')
        
        print(usermessage)
        
        print('Generating Response...')
        
        conn.set_var("status", 1)

        print('status is now = 1')

        print('Thinking...')
        
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a chatbot that likes to have conversations with users, you were made by the scratch user gioleung with python but only for internet information"},
                {"role": "user", "content": usermessage},
                    ]
                )                                                   

        print('response:')

        conn.set_var("status", 2)
        
        bot = completion.choices[0].message.content
        
        conn.set_var("status", 2)
        
        segment_1, segment_2, segment_3, segment_4, segment_5 = split_sentence(bot)

        print('RESPONSE:')
        
        print(bot)

        conn.set_var("status", 2)
        
        bot = Encoding.encode(bot)

        encode_1 = Encoding.encode(segment_1)
        encode_2 = Encoding.encode(segment_2)
        encode_3 = Encoding.encode(segment_3)
        encode_4 = Encoding.encode(segment_4)
        encode_5 = Encoding.encode(segment_5)

        
        conn.set_var("status", 2)

        
        conn.set_var("segment1", encode_1)
        conn.set_var("segment2", encode_2)
        conn.set_var("segment3", encode_3)
        conn.set_var("segment4", encode_4)
        conn.set_var("segment5", encode_5)
        
        conn.set_var("status", 2)









