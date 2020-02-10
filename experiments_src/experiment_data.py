import json
import uuid


class DistributionData:

    def __init__(self, data: dict):
        self.distribution_type = data['distribution_type']
        self.equal_node_params = data['equal_node_params']
        self.different_node_params = data['different_node_params']


class GraphData:

    def __init__(self, data: dict):
        self.network_type = data['network_type']
        self.params = data['params']


class ExecutionModel:

    SEQUENTIAL_EXECUTION_MODEL: str = 'SEQUENTIAL_EXECUTION_MODEL'
    SIMULTANEOUS_EXECUTION_MODEL: str = 'SIMULTANEOUS_EXECUTION_MODEL'

    def __init__(self, data: dict):
        self.run_type = ExecutionModel.SIMULTANEOUS_EXECUTION_MODEL if data['run_type'] == ExecutionModel.SIMULTANEOUS_EXECUTION_MODEL else ExecutionModel.SEQUENTIAL_EXECUTION_MODEL
        self.params = data['params']


class ExperimentData: 

    def __init__(self, data: dict):
        self.id = str(uuid.uuid4())
        self.epochs_count = data['epochs_count']
        self.epoch_length = data['epoch_length']
        self.description = data['description']
        self.distribution_data: DistributionData = DistributionData(data['distribution_data'])
        self.graph_data: GraphData = GraphData(data['graph_data'])
        self.execution_model: ExecutionModel = ExecutionModel(data['execution_model'])

    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
