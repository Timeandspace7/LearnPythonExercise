import random
import words

# brief : 随机组合句子
# by    : T7
#date   : 2019.12.21
def silly_string(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)

    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    index = 0

    print(template);
    # Add a while loop here.
    while "{{noun}}" in template or "{{verb}}" in template:
        nouns_str1 = random.choice(words.nouns);
        verbs_str2 = random.choice(words.verbs);
        template = template.replace("{{noun}}", nouns_str1, 1);
        template = template.replace("{{verb}}", verbs_str2, 1);

    # After the loop has finished, join the output and return it.
    return template;

if __name__ == '__main__':
    print(silly_string(words.nouns, words.verbs,
        words.templates))


# by    : Udaciy
def silly_string(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)

    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    position = 0;

    while position < len(template):
        if template[position:position + 8] == "{{noun}}":
            output.append(random.choice(nouns))
            position += 8;
        elif template[position:position + 8] == "{{verb}}":
            output.append(random.choice(verbs))
            position += 8
        else:
            output.append(template[position])
            position += 1

    print(output)
    return "".join(output)

print(silly_string(words.nouns, words.verbs,
        words.templates))
