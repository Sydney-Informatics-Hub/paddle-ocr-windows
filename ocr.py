from paddleocr import PaddleOCR
from argparse import ArgumentParser
from pathlib import Path
import json

def convert_pdf(ocr, pdf, outdir):
    result = ocr.predict(str(pdf))
    stem = pdf.stem
    textfile = outdir / Path(f'{stem}.txt')
    with open(textfile, 'w') as fh:
        for res in result:
            n = res['page_index']
            fh.write(f"{stem} page {n}\n\n")
            for line in res['rec_texts']:
                fh.write(line + "\n")
            fh.write("\n")



def main():
    ap = ArgumentParser("ocr.py")

    ap.add_argument(
        "--input",
        type=Path,
        help="Input directory",
    )
    ap.add_argument(
        "--output",
        type=Path,
        help="Output directory",
    )
    args = ap.parse_args()
    if not args.input.is_dir():
        print(f"{args.input} is not a directory")
        exit(-1)

    if not args.output.is_dir():
        print(f"{args.output} is not a directory")
        exit(-1)
    ocr = PaddleOCR(
        use_doc_unwarping=True,
        use_textline_orientation=True
    )
    for pdf in args.input.glob("*.pdf"):
        convert_pdf(ocr, pdf, args.output)


if __name__ == "__main__":
    main()
