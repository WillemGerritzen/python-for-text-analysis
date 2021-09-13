def clean_text_general(text, chars_to_remove={'\n', ',', '.', '"'}):
    characters = list(chars_to_remove)

    story = text.replace(characters[0], '')

    for cha in characters[1:]:
        story = story.replace(cha, ' ')

    return story
