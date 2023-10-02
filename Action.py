class Action:
    def __init__(self, llm):
        self.name = ""
        self.selection_prompt = ""
        self.parameter_prompt = ""
        self.llm = llm

    def execute(self, llm, query):
        pass

    def get_single_paramter(self, llm, query):
        pass