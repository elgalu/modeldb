# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ...public.modeldb import DatasetService_pb2 as protos_dot_public_dot_modeldb_dot_DatasetService__pb2
from ...public.modeldb import DatasetVersionService_pb2 as protos_dot_public_dot_modeldb_dot_DatasetVersionService__pb2
from ...public.modeldb import ExperimentRunService_pb2 as protos_dot_public_dot_modeldb_dot_ExperimentRunService__pb2
from ...public.modeldb import ExperimentService_pb2 as protos_dot_public_dot_modeldb_dot_ExperimentService__pb2
from ...public.modeldb import HydratedService_pb2 as protos_dot_public_dot_modeldb_dot_HydratedService__pb2
from ...public.modeldb import ProjectService_pb2 as protos_dot_public_dot_modeldb_dot_ProjectService__pb2


class HydratedServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getHydratedProjects = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/getHydratedProjects',
        request_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedProjects.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedProjects.Response.FromString,
        )
    self.getHydratedPublicProjects = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/getHydratedPublicProjects',
        request_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedProjects.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedProjects.Response.FromString,
        )
    self.getHydratedProjectById = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/getHydratedProjectById',
        request_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedProjectById.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedProjectById.Response.FromString,
        )
    self.getHydratedExperimentsByProjectId = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/getHydratedExperimentsByProjectId',
        request_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedExperimentsByProjectId.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedExperimentsByProjectId.Response.FromString,
        )
    self.getHydratedExperimentRunsInProject = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/getHydratedExperimentRunsInProject',
        request_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedExperimentRunsByProjectId.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedExperimentRunsByProjectId.Response.FromString,
        )
    self.getHydratedExperimentRunById = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/getHydratedExperimentRunById',
        request_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedExperimentRunById.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedExperimentRunById.Response.FromString,
        )
    self.findHydratedExperimentRuns = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/findHydratedExperimentRuns',
        request_serializer=protos_dot_public_dot_modeldb_dot_ExperimentRunService__pb2.FindExperimentRuns.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryExperimentRunsResponse.FromString,
        )
    self.sortHydratedExperimentRuns = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/sortHydratedExperimentRuns',
        request_serializer=protos_dot_public_dot_modeldb_dot_ExperimentRunService__pb2.SortExperimentRuns.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryExperimentRunsResponse.FromString,
        )
    self.getTopHydratedExperimentRuns = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/getTopHydratedExperimentRuns',
        request_serializer=protos_dot_public_dot_modeldb_dot_ExperimentRunService__pb2.TopExperimentRunsSelector.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryExperimentRunsResponse.FromString,
        )
    self.findHydratedExperiments = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/findHydratedExperiments',
        request_serializer=protos_dot_public_dot_modeldb_dot_ExperimentService__pb2.FindExperiments.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryExperimentsResponse.FromString,
        )
    self.findHydratedProjects = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/findHydratedProjects',
        request_serializer=protos_dot_public_dot_modeldb_dot_ProjectService__pb2.FindProjects.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryProjectsResponse.FromString,
        )
    self.findHydratedPublicProjects = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/findHydratedPublicProjects',
        request_serializer=protos_dot_public_dot_modeldb_dot_ProjectService__pb2.FindProjects.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryProjectsResponse.FromString,
        )
    self.findHydratedProjectsByUser = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/findHydratedProjectsByUser',
        request_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.FindHydratedProjectsByUser.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryProjectsResponse.FromString,
        )
    self.findHydratedProjectsByOrganization = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/findHydratedProjectsByOrganization',
        request_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.FindHydratedProjectsByOrganization.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryProjectsResponse.FromString,
        )
    self.findHydratedProjectsByTeam = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/findHydratedProjectsByTeam',
        request_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.FindHydratedProjectsByTeam.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryProjectsResponse.FromString,
        )
    self.findHydratedDatasetsByOrganization = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/findHydratedDatasetsByOrganization',
        request_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.FindHydratedDatasetsByOrganization.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryDatasetsResponse.FromString,
        )
    self.findHydratedDatasetsByTeam = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/findHydratedDatasetsByTeam',
        request_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.FindHydratedDatasetsByTeam.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryDatasetsResponse.FromString,
        )
    self.findHydratedDatasets = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/findHydratedDatasets',
        request_serializer=protos_dot_public_dot_modeldb_dot_DatasetService__pb2.FindDatasets.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryDatasetsResponse.FromString,
        )
    self.findHydratedPublicDatasets = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/findHydratedPublicDatasets',
        request_serializer=protos_dot_public_dot_modeldb_dot_DatasetService__pb2.FindDatasets.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryDatasetsResponse.FromString,
        )
    self.findHydratedDatasetVersions = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/findHydratedDatasetVersions',
        request_serializer=protos_dot_public_dot_modeldb_dot_DatasetVersionService__pb2.FindDatasetVersions.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryDatasetVersionsResponse.FromString,
        )
    self.getHydratedDatasetByName = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/getHydratedDatasetByName',
        request_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedDatasetByName.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedDatasetByName.Response.FromString,
        )
    self.getHydratedDatasetsByProjectId = channel.unary_unary(
        '/ai.verta.modeldb.HydratedService/getHydratedDatasetsByProjectId',
        request_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedDatasetsByProjectId.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedDatasetsByProjectId.Response.FromString,
        )


class HydratedServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def getHydratedProjects(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getHydratedPublicProjects(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getHydratedProjectById(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getHydratedExperimentsByProjectId(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getHydratedExperimentRunsInProject(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getHydratedExperimentRunById(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findHydratedExperimentRuns(self, request, context):
    """queries
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def sortHydratedExperimentRuns(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getTopHydratedExperimentRuns(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findHydratedExperiments(self, request, context):
    """queries
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findHydratedProjects(self, request, context):
    """queries
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findHydratedPublicProjects(self, request, context):
    """queries
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findHydratedProjectsByUser(self, request, context):
    """queries
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findHydratedProjectsByOrganization(self, request, context):
    """queries
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findHydratedProjectsByTeam(self, request, context):
    """queries
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findHydratedDatasetsByOrganization(self, request, context):
    """queries
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findHydratedDatasetsByTeam(self, request, context):
    """queries
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findHydratedDatasets(self, request, context):
    """queries
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findHydratedPublicDatasets(self, request, context):
    """queries
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findHydratedDatasetVersions(self, request, context):
    """queries
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getHydratedDatasetByName(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getHydratedDatasetsByProjectId(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HydratedServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getHydratedProjects': grpc.unary_unary_rpc_method_handler(
          servicer.getHydratedProjects,
          request_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedProjects.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedProjects.Response.SerializeToString,
      ),
      'getHydratedPublicProjects': grpc.unary_unary_rpc_method_handler(
          servicer.getHydratedPublicProjects,
          request_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedProjects.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedProjects.Response.SerializeToString,
      ),
      'getHydratedProjectById': grpc.unary_unary_rpc_method_handler(
          servicer.getHydratedProjectById,
          request_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedProjectById.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedProjectById.Response.SerializeToString,
      ),
      'getHydratedExperimentsByProjectId': grpc.unary_unary_rpc_method_handler(
          servicer.getHydratedExperimentsByProjectId,
          request_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedExperimentsByProjectId.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedExperimentsByProjectId.Response.SerializeToString,
      ),
      'getHydratedExperimentRunsInProject': grpc.unary_unary_rpc_method_handler(
          servicer.getHydratedExperimentRunsInProject,
          request_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedExperimentRunsByProjectId.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedExperimentRunsByProjectId.Response.SerializeToString,
      ),
      'getHydratedExperimentRunById': grpc.unary_unary_rpc_method_handler(
          servicer.getHydratedExperimentRunById,
          request_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedExperimentRunById.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedExperimentRunById.Response.SerializeToString,
      ),
      'findHydratedExperimentRuns': grpc.unary_unary_rpc_method_handler(
          servicer.findHydratedExperimentRuns,
          request_deserializer=protos_dot_public_dot_modeldb_dot_ExperimentRunService__pb2.FindExperimentRuns.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryExperimentRunsResponse.SerializeToString,
      ),
      'sortHydratedExperimentRuns': grpc.unary_unary_rpc_method_handler(
          servicer.sortHydratedExperimentRuns,
          request_deserializer=protos_dot_public_dot_modeldb_dot_ExperimentRunService__pb2.SortExperimentRuns.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryExperimentRunsResponse.SerializeToString,
      ),
      'getTopHydratedExperimentRuns': grpc.unary_unary_rpc_method_handler(
          servicer.getTopHydratedExperimentRuns,
          request_deserializer=protos_dot_public_dot_modeldb_dot_ExperimentRunService__pb2.TopExperimentRunsSelector.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryExperimentRunsResponse.SerializeToString,
      ),
      'findHydratedExperiments': grpc.unary_unary_rpc_method_handler(
          servicer.findHydratedExperiments,
          request_deserializer=protos_dot_public_dot_modeldb_dot_ExperimentService__pb2.FindExperiments.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryExperimentsResponse.SerializeToString,
      ),
      'findHydratedProjects': grpc.unary_unary_rpc_method_handler(
          servicer.findHydratedProjects,
          request_deserializer=protos_dot_public_dot_modeldb_dot_ProjectService__pb2.FindProjects.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryProjectsResponse.SerializeToString,
      ),
      'findHydratedPublicProjects': grpc.unary_unary_rpc_method_handler(
          servicer.findHydratedPublicProjects,
          request_deserializer=protos_dot_public_dot_modeldb_dot_ProjectService__pb2.FindProjects.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryProjectsResponse.SerializeToString,
      ),
      'findHydratedProjectsByUser': grpc.unary_unary_rpc_method_handler(
          servicer.findHydratedProjectsByUser,
          request_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.FindHydratedProjectsByUser.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryProjectsResponse.SerializeToString,
      ),
      'findHydratedProjectsByOrganization': grpc.unary_unary_rpc_method_handler(
          servicer.findHydratedProjectsByOrganization,
          request_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.FindHydratedProjectsByOrganization.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryProjectsResponse.SerializeToString,
      ),
      'findHydratedProjectsByTeam': grpc.unary_unary_rpc_method_handler(
          servicer.findHydratedProjectsByTeam,
          request_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.FindHydratedProjectsByTeam.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryProjectsResponse.SerializeToString,
      ),
      'findHydratedDatasetsByOrganization': grpc.unary_unary_rpc_method_handler(
          servicer.findHydratedDatasetsByOrganization,
          request_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.FindHydratedDatasetsByOrganization.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryDatasetsResponse.SerializeToString,
      ),
      'findHydratedDatasetsByTeam': grpc.unary_unary_rpc_method_handler(
          servicer.findHydratedDatasetsByTeam,
          request_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.FindHydratedDatasetsByTeam.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryDatasetsResponse.SerializeToString,
      ),
      'findHydratedDatasets': grpc.unary_unary_rpc_method_handler(
          servicer.findHydratedDatasets,
          request_deserializer=protos_dot_public_dot_modeldb_dot_DatasetService__pb2.FindDatasets.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryDatasetsResponse.SerializeToString,
      ),
      'findHydratedPublicDatasets': grpc.unary_unary_rpc_method_handler(
          servicer.findHydratedPublicDatasets,
          request_deserializer=protos_dot_public_dot_modeldb_dot_DatasetService__pb2.FindDatasets.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryDatasetsResponse.SerializeToString,
      ),
      'findHydratedDatasetVersions': grpc.unary_unary_rpc_method_handler(
          servicer.findHydratedDatasetVersions,
          request_deserializer=protos_dot_public_dot_modeldb_dot_DatasetVersionService__pb2.FindDatasetVersions.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.AdvancedQueryDatasetVersionsResponse.SerializeToString,
      ),
      'getHydratedDatasetByName': grpc.unary_unary_rpc_method_handler(
          servicer.getHydratedDatasetByName,
          request_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedDatasetByName.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedDatasetByName.Response.SerializeToString,
      ),
      'getHydratedDatasetsByProjectId': grpc.unary_unary_rpc_method_handler(
          servicer.getHydratedDatasetsByProjectId,
          request_deserializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedDatasetsByProjectId.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_HydratedService__pb2.GetHydratedDatasetsByProjectId.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ai.verta.modeldb.HydratedService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))