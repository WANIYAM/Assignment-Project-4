# Mad libs Python Project

'''
The game will ask the user for different types of words (like a noun, verb, adjective, etc.) and then plug them into a story template.
'''
def mad_libs():
    print("Let's play Mad Libs!")
    
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")
    place = input("Enter a place: ")
    
    story = f"""
    Today I went to the {place} and saw a very {adjective} {noun}.
    It decided to {verb} {adverb}, which surprised everyone!
    What a weird day!
    """
    print("\nHere's your story:")
    print(story)


mad_libs()
