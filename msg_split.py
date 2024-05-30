from bs4 import BeautifulSoup
from typing import Generator

MAX_LEN = 4096

def split_message(source: str, max_len=MAX_LEN) -> Generator[str, None, None]:
    soup = BeautifulSoup(source, 'html.parser')
    current_length = 0
    fragment = ''
    for element in soup.recursiveChildGenerator():
        if isinstance(element, str):
            part_length = len(element)
            if current_length + part_length > max_len:
                yield fragment
                fragment = ''
                current_length = 0
            fragment += element
            current_length += part_length
        else:
            part_length = len(str(element))
            if current_length + part_length > max_len:
                yield fragment
                fragment = ''
                current_length = 0
            fragment += str(element)
            current_length += part_length

    if fragment:
        yield fragment

if __name__ == "__main__":
    import click

    @click.command()
    @click.argument('file', type=click.File('r'))
    @click.option('--max-len', default=MAX_LEN, help='Maximum length of each fragment')
    def main(file, max_len):
        content = file.read()
        for i, fragment in enumerate(split_message(content, max_len), start=1):
            print(f"fragment #{i}: {len(fragment)} chars\n{fragment}\n")

    main()
