def duplicate_count(text):
    count = 0
    used = []
    for i in range(0, len(text)):
        if text[i].lower() not in used:
            for j in range(i+1, len(text)):
                if text[i].lower() == text[j].lower():
                    count += 1
                    break
        used.append(text[i].lower())
    return count

    

#duplicate_count("1abcde")
#duplicate_count("abcdeaa")
#duplicate_count("abcdeaB")