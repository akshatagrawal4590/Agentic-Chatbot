from configparser import ConfigParser

class Config:
    def __init__(self, config_file_path = "./src/langgraph_agentic_ai/ui/ui_config_file.ini"):
        self.config = ConfigParser()
        self.config.read(config_file_path)

    def get_llm_options(self):
        return self.config["DEFAULT"]["LLM_OPTIONS"].split(", ")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"]["USECASE_OPTIONS"].split(", ")
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"]["GROQ_MODEL_OPTIONS"].split(", ")
    
    def get_page_title(self):
        return self.config["DEFAULT"]["PAGE_TITLE"]