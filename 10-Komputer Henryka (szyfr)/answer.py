from api import get_emails
from agenda import agenda

def decode_emails():
    emails = get_emails(['67', '128'])

    for email in emails:
        decoded_text = ""
        tokens = email['body'].split(' ')

        for token in tokens:
            parts = token.split('.')  # [ARTYKUŁ, PUNKT, SŁOWO]
            article_id = parts[0]
            point_index = int(parts[1]) - 1
            word_index = int(parts[2]) - 1

            sentence = agenda[article_id][point_index]
            words = sentence.split(" ")
            decoded_text += " " + words[word_index]

        print(decoded_text.strip())

    return 0


decode_emails()
