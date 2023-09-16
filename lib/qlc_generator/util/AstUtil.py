class AstUtil:
    def __init__(self):
        # add to this as needed
        self.functionDefNodes = []
        self.forNodes = []
        self.whileNodes = []
        self.ifNodes = []

        self.nodes = {"functionDef": self.functionDefNodes, "for": self.forNodes, "while": self.whileNodes}

    def addFunctionDefNode(self, node):
        self.functionDefNodes.append(node)

    def addForNode(self, node):
        self.forNodes.append(node)

    def addWhileNode(self, node):
        self.whileNodes.append(node)

    def addIfNode(self, node):
        self.ifNodes.append(node)

    def getFunctionDefNodes(self):
        return self.functionDefNodes
    
    def getForNodes(self):
        return self.forNodes
    
    def getWhileNodes(self):
        return self.whileNodes
    
    def getIfNodes(self):
        return self.ifNodes

    @staticmethod
    def get_parameter_list(node):
        parameter_list = []
        for param in node.args.args:
            parameter_list.append(param.arg)
        
        return parameter_list
    
    @staticmethod
    def get_variable_list(node):
        variable_list = []
        for line in node.body:
            if hasattr(line, 'targets'):
                variable_list.append(line.targets[0].id)
            elif hasattr(line, 'body'):
                variable_list += AstUtil.get_variable_list(line)

        return variable_list
    
    @staticmethod
    def get_lines(node):
        return node.body
    
    @staticmethod
    def get_function_call_list(node):
        function_list = []
        for line in node.body:
            if hasattr(line, 'value'):
                if hasattr(line.value, 'func'):
                    function_list.append(line.value.func.id)
            elif hasattr(line, 'body'):
                function_list += AstUtil.get_function_call_list(line)

        return function_list
    
    @staticmethod
    def get_function_call_list(node):
        function_list = []
        for line in node.body:
            if hasattr(line, 'value'):
                if hasattr(line.value, 'func'):
                    function_list.append(line.value.func.id)
            elif hasattr(line, 'body'):
                function_list += AstUtil.get_function_call_list(line)

        return function_list
    
    @staticmethod
    def get_user_defined_function_call_list(node, astUtil):
        # get list of all user defined functions called by the selected function,
        # excluding built in functions and functions from libraries
        function_calls = AstUtil.get_function_call_list(node)
        defined_functions = list(map(AstUtil.get_function_name, astUtil.getFunctionDefNodes()))
        defined_function_calls = list(set(function_calls) & set(defined_functions))

        return defined_function_calls
    
    @staticmethod
    def get_function_name(node):
        return node.name
    
    def get_loop_list(self, node):
        loop_list = []
        for line in node.body:
            if line in self.forNodes or line in self.whileNodes:
                loop_list.append(line)
            if hasattr(line, 'body'):
                loop_list += self.get_loop_list(line)

        return loop_list