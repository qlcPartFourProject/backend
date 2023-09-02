class FunctionModel:
    def __init__(self, function_def):
        self.function = function_def

    def parameter_list(self):
        parameter_list = []
        for param in self.function.args.args:
            parameter_list.append(param.arg)
        
        return parameter_list