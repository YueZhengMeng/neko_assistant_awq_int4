from lmdeploy.serve.gradio.turbomind_coupled import run_local
from lmdeploy.messages import TurbomindEngineConfig

model_path = './neko_assistant_awq_int4'

backend_config = TurbomindEngineConfig(cache_max_entry_count=0.4)
run_local(model_path, model_name='internlm2-chat-1_8b', backend_config=backend_config, server_name="huggingface-space")