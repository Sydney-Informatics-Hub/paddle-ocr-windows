from paddleocr import PaddleOCR
from argparse import ArgumentParser


def convert_pdf(pdf, outdir):
    print(pdf)
    print(outdir)




def main():
    ap = ArgumentParser("csv_tidy.py")
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

    for pdf in args.input.glob("*.pdf")
        convert_pdf(pdf, args.output)


if __name__ == "__main__":
    main()
