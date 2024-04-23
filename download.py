import os
# download model to the model_path directory using git tool
model_path = './neko_assistant_awq_int4'
os.system(f'git clone https://code.openxlab.org.cn/YueZhengMeng/neko_assistant_awq_int4.git {model_path}')
os.system(f'cd {model_path} && git lfs pull && git pull')
