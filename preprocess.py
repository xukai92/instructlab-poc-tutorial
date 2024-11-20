import argparse
from docling.document_converter import DocumentConverter


def convert_pdf_to_markdown(pdf_path):
    """
    Convert a PDF file to Markdown format using docling.
    
    Args:
        pdf_path (str): Path to the PDF file or URL
        
    Returns:
        str: Markdown text content
    """
    # Initialize converter
    converter = DocumentConverter()
    
    # Convert document
    result = converter.convert(pdf_path)
    
    # Export to markdown
    markdown_text = result.document.export_to_markdown()
    
    return markdown_text


def main():
    # set up argument parser
    parser = argparse.ArgumentParser(description='convert pdf file to markdown')
    parser.add_argument('pdf_path', help='path to the input pdf file')
    parser.add_argument('md_path', help='path to save the output markdown file')
    
    # parse arguments
    args = parser.parse_args()
    
    # convert pdf to markdown
    markdown_text = convert_pdf_to_markdown(args.pdf_path)
    
    # save markdown to file
    with open(args.md_path, 'w', encoding='utf-8') as f:
        f.write(markdown_text)


if __name__ == '__main__':
    main()