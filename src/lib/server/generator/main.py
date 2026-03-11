from pypdf import PdfReader, PdfWriter


def main():
    print("Hello from generator!")

    reader = PdfReader("./templates/coc.pdf")
    writer = PdfWriter()

    pages = reader.pages[0]
    fields = reader.get_fields()

    writer.append(reader)

    writer.update_page_form_field_values(
        writer.pages[0],
        {"comments": "sucks major ass"},
        auto_regenerate=False,
    )

    writer.write("output/out.pdf")


if __name__ == "__main__":
    main()
