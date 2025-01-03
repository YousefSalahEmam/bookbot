def count_characters(file_contents):
    lower_file_contents = file_contents.lower()
    chars={}
    for char in (lower_file_contents):
        if char in chars:
            chars[char] +=1
        else:
            chars[char] =1
    return chars
         

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        result = count_characters(file_contents)
        sorted_chars= sorted(result.items(), key=lambda x: x[1], reverse=True)
        print(f"-- Begin report of book/frankenstein.txt --")
        total_characters = sum(result.values())
        print(f"{total_characters} characters found in the document")
        print("Here are the character counts from most common to least common:")
        for char, count in sorted_chars:
            char_display = char
            if char == ' ':
                char_display = 'SPACE'
            elif char == '\n':
                char_display = 'NEWLINE'
            print(f"The '{char_display}' character appears {count} times")
        print("--- End of Report ---")
if __name__ == "__main__":
    main()
