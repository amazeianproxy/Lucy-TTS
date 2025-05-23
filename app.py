from TTS.utils.synthesizer import Synthesizer
import gradio as gr

synthesizer = Synthesizer(
    tts_checkpoint="best_model.pth",
    tts_config_path="config.json"
)

def synthesize(text):
    wav = synthesizer.tts(text)
    path = "output.wav"
    synthesizer.save_wav(wav, path)
    print("Audio saved to:", path)
    return path

gr.Interface(
    fn=synthesize,
    inputs=gr.Textbox(label="Input Text"),
    outputs=gr.Audio(type="filepath"),
    title="Lucy: The Sound of the Silent (TTS)"
).launch(debug=True, share=True)
