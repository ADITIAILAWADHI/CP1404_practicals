from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby.is_dynamic())
    print(ruby)

    print()
    ProgrammingLanguage_objects = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for i in ProgrammingLanguage_objects:
        if i.is_dynamic():
            print(i.field)


main()
