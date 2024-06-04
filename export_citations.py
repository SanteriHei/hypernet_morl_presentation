import argparse
import pathlib
from typing import List

from bs4 import BeautifulSoup

def get_parser():
    parser = argparse.ArgumentParser(
            prog="export_citations",
            description="""
                Export citations from a reveal-js presentation and print the 
                bibtex keys out
            """
    )

    parser.add_argument("input_file", type=pathlib.Path)
    parser.add_argument("--output-file", type=pathlib.Path, default=None)
    return parser

def extract_citations(document: BeautifulSoup) -> List[str]:
    
    found_refs = []

    # find_all_next is ensured to keep the order of the citations same as in
    # the document
    first_elem = document.div
    for tag in first_elem.find_all_next("span", class_="ref"):
        tag_id = tag.get("id")
        if tag_id not in found_refs and tag_id is not None:
            found_refs.append(tag_id)
    return list(found_refs)

if __name__ == "__main__":

    parser = get_parser()
    args = parser.parse_args()
    
    if not args.input_file.is_file():
        raise FileNotFoundError(
                f"{str(args.input_file)!r} does not point a valid file!"
        )

    
    with args.input_file.open('r') as ifstream:
        document = BeautifulSoup(ifstream, features="html.parser")

    references = extract_citations(document)

    if args.output_file is not None:
        with args.output_file.open("w") as ofstream:
            ofstream.write("\n".join(references))
    else:
        for ref in references:
            print(ref)
