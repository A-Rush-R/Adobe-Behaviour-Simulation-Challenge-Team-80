## fine tuning using gpt3.5
def output_(prompt, content):
    
    messages = {
        "messages":[   
            {
                "role": "system",
                "content": "Meow is a descriptive agent who is very good at generating tweets given some data about that tweet"
            },
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": content
            }
        ]
    }   
    
    return messages