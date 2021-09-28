from utils_3a import preprocess


string = """In a far away kingdom, there was a river. This river was home to many golden swans. The swans spent most of their time on the banks of the river. Every six months, the swans would leave a golden feather as a fee for using the lake. The soldiers of the kingdom would collect the feathers and deposit them in the royal treasury. 
One day, a homeless bird saw the river. "The water in this river seems so cool and soothing. I will make my home here," thought the bird. 
As soon as the bird settled down near the river, the golden swans noticed her. They came shouting. "This river belongs to us. We pay a golden feather to the King to use this river. You can not live here." 
"I am homeless, brothers. I too will pay the rent. Please give me shelter," the bird pleaded. "How will you pay the rent? You do not have golden feathers," said the swans laughing. They further added, "Stop dreaming and leave once." The humble bird pleaded many times. But the arrogant swans drove the bird away. 
"I will teach them a lesson!" decided the humiliated bird. 
She went to the King and said, "O' King! The swans in your river are impolite and unkind. I begged for shelter but they said that they had purchased the river with golden feathers." 
The King was angry with the arrogant swans for having insulted the homeless bird. He ordered his soldiers to bring the arrogant swans to his court. In no time, all the golden swans were brought to the King’s court. 
"Do you think the royal treasury depends upon your golden feathers? You can not decide who lives by the river. Leave the river at once or you all will be beheaded!" shouted the King. 
The swans shivered with fear on hearing the King. They flew away never to return. The bird built her home near the river and lived there happily forever. The bird gave shelter to all other birds in the river. """


def count(text: str) -> dict:
    """
    Takes a string and counts each word
    :param text: The string whose words are to be counted
    :return: A dictionary with each word and its count
    """

    text = preprocess(text, """()"'.,!?;:""")

    text = text.split(' ')

    counted_words = {}

    for word in text:
        if word in counted_words.keys():
            continue
        else:
            counted_words[word] = len([w for w in text if w == word])

    return counted_words


print(count(string))
