import gradio as gr
from lmdeploy import pipeline, TurbomindEngineConfig,GenerationConfig

model_path = './neko_assistant_awq_int4'

backend_config = TurbomindEngineConfig(cache_max_entry_count=0.4)
pipe = pipeline(model_path, backend_config=backend_config, model_name='internlm2-chat-1_8b')
gen_config = GenerationConfig(top_p=0.8, top_k=40, temperature=0.8, max_new_tokens=1024)

def chat(message,history):
    response = pipe(message, gen_config = gen_config)
    return response.text

demo = gr.ChatInterface(fn = chat, title="InternLM2-Chat-1.8_4bit-self-cognition",
                        description="""InternLM is mainly developed by Shanghai AI Laboratory.  """,)
demo.queue(1).launch()