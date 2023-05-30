# frontend/main.py
import gradio as gr
from gradio import Interface, File
from file_handler.file_reader import read_psd

def process_file(file):
    psd = read_psd(file)
    return f"Resolution: {psd.width}x{psd.height}"

iface = Interface(
    fn=process_file,
    inputs=File(label="Upload your PSD file"),
    outputs="text",
    title="PSD Converter",
    description="Upload a PSD file to convert it."
)

if __name__ == "__main__":
    iface.launch()
